import torch
import torchvision
from torch import nn
import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import os
from torch.utils.data import DataLoader
import random
from pathlib import Path
import numpy as np
from PIL import Image
import base64
import io



model_path = "./models/model.pt"


DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

def setAllSeeds(seed):
  os.environ['MY_GLOBAL_SEED'] = str(seed)
  random.seed(seed)
  np.random.seed(seed)
  torch.manual_seed(seed)
  torch.cuda.manual_seed_all(seed)


def getViT(seed,classNames,DEVICE):
  setAllSeeds(seed)
  vitWeights = torchvision.models.ViT_B_16_Weights.DEFAULT
  vitTransforms = vitWeights.transforms()
  vit = torchvision.models.vit_b_16(weights=vitWeights).to(DEVICE)
  for param in vit.parameters():
    param.requires_grad = False
  vit.heads = nn.Linear(in_features=768, out_features=classNames).to(DEVICE)
  return vit,vitTransforms



model, transformers = getViT(42,4, DEVICE)

#loading the model
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))


def img_transform(input_img):
    mean = [0.5, 0.5, 0.5]
    std = [0.5, 0.5, 0.5]

    img_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomRotation(10),
        transforms.ToTensor(),
        transforms.Normalize(torch.Tensor(mean), torch.Tensor(std))
    ])

    # If input is a FastAPI UploadFile, read the bytes
    if hasattr(input_img, "file"):
        img_bytes = input_img.file.read()
        img = Image.open(io.BytesIO(img_bytes))
    else:  # If input is a PIL Image
        img = input_img

    # Encode the image for rendering in the response
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    encoded_string = base64.b64encode(buffered.getvalue()).decode('utf-8')
    encoded_img = f'data:image/jpeg;base64,{encoded_string}'

    tensor_img = img_transforms(img).unsqueeze(0)
    return encoded_img, tensor_img



# image classes
classes = ['NOCANCER', 'EARLY', 'PRE', 'PRO']


def get_prediction(input_img, is_api=False):
    encoded_img, tensor_img = img_transform(input_img)  # Corrected unpacking
    model.eval()
    with torch.no_grad():
        preds = model(tensor_img)  # Pass the tensor_img to the model
        probabilities = torch.softmax(preds, dim=1)
        predicted_class = torch.argmax(preds)
        predicted_class_prob = probabilities[0, predicted_class].item()
        class_name = classes[predicted_class]

    pred_results = {
        "class_name": class_name,
        "class_probability":predicted_class_prob*100
    }



    # Conditionally add image data to the result dictionary
    if not is_api:
        pred_results["org_encoded_img"] = encoded_img

    print(pred_results)

    return pred_results




