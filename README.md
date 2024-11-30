# Acute-Lymphblastic-Leukemia-Diagnosis-Using-Vision-Transformer
A deep learning project for diagnosing Acute Lymphoblastic Leukemia (ALL) using Vision Transformer (ViT) models. Includes an interactive web application showcasing the model’s predictions for PBS images. The project leverages Python, PyTorch, and web technologies (CSS &amp; JS) for a robust and user-friendly interface.


# Introduction
Acute Lymphoblastic Leukemia (ALL) diagnosis using Peripheral Blood Smear (PBS) images often requires time-consuming and expensive laboratory tests. This project provides a cost-effective and automated diagnostic solution using Vision Transformers (ViT). The system classifies PBS images into four categories: Benign, Early Pre-B ALL, Pre-B ALL, and Pro-B ALL. An accompanying web interface enables user-friendly interaction with the model for real-time predictions.

# Dataset

Source: Blood Cells Cancer (ALL) dataset, prepared in Taleqani Hospital, Tehran, Iran.
Images: 3256 PBS images classified into benign and malignant (3 ALL subtypes).
Preprocessing: Images resized, normalized, and augmented for better generalization.
Model

# Architectural Overview
Architecture: Vision Transformer (ViT-B_16) with transfer learning from ImageNet.
Modifications: Output layer customized for four-class classification.
Why ViT?: ViT captures global dependencies within images better than CNNs, crucial for recognizing subtle patterns in medical imaging.

# Web Application
Built using CSS, and JavaScript to demonstrate predictions in real-time.
Users upload PBS images and receive cancer stage predictions with visual highlights.
Code Features

Training and Fine-Tuning: PyTorch-based pipeline for data loading, training, and validation.
Visualization: Dataset distribution charts, model accuracy plots, and heatmaps.
Model Deployment: Includes API integration for serving predictions.
Installation

Clone the repository:

# Requirements
Install dependencies:
pip install -r requirements.txt
### To run the web application:
fastapi==0.103.2 \
torch==2.4.1 \
torchvision==0.19.1 \
numpy==1.24.3 \
Pillow==10.4.0 \
jinja2==3.1.4 \

# How to Diagnose:
Upload an image via the web interface.

View predictions and class probabilities in real-time.
Results

Achieved 98.81% accuracy on the test dataset.
High performance in differentiating ALL subtypes, showcasing the efficacy of Vision Transformers for medical imaging.

# Acknowledgments
Based on the dataset published by Ghaderzadeh et al. in their paper:
"A fast and efficient CNN model for B-ALL diagnosis and its subtypes classification using peripheral blood smear images."
