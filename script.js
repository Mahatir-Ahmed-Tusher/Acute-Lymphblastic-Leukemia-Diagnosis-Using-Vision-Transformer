document.addEventListener("DOMContentLoaded", function () {
  // Add project title, subtitle, logo, and contributors
  const titleContainer = document.createElement("div");
  titleContainer.className = "project-title";

  titleContainer.innerHTML = `
    <img src="static/vit.png" alt="VIT Logo" class="logo">
    <h1>Detection of Lymphocytic Leukemia</h1>
    <h3>Capstone Project</h3>
    <div class="contributors">
      <p>Contributors:</p>
      <ul>
        <li>Mahatir Ahmed Tusher (21BCE8971)</li>
        <li>SAKET CHOUDARY KONGARA (21BCE7918)</li>
        <li>KOCHERLAKOTA LAKSHMIPATHI RAO (21BCE8552)</li>
        <li>SREE NIKHIL VELICHETI (21BCE7775)</li>
      </ul>
    </div>
  `;

  // Prepend the title container to the body
  document.body.prepend(titleContainer);

  // Drag-and-Drop and File Upload Logic
  const dropArea = document.getElementById("drop-area");
  const inputFile = document.getElementById("input-file");
  const imageView = document.getElementById("img-view");
  const predictButton = document.querySelector(".button");
  const errorMessage = document.getElementById("error-message");

  inputFile.addEventListener("change", uploadImage);

  function uploadImage() {
    const file = inputFile.files[0];
    if (!file) {
      alert("Please upload an image to predict.");
      return;
    }

    const allowedTypes = ["image/jpeg", "image/png", "image/jpg"];
    if (!allowedTypes.includes(file.type)) {
      alert("Please upload a valid image file (JPEG or PNG).");
      return;
    }

    const imgLink = URL.createObjectURL(file);
    imageView.style.backgroundImage = `url(${imgLink})`;
    imageView.textContent = "";
    imageView.style.border = 0;
  }

  dropArea.addEventListener("dragover", function (e) {
    e.preventDefault();
  });

  dropArea.addEventListener("drop", function (e) {
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadImage();
  });

  predictButton.addEventListener("click", function (e) {
    if (!inputFile.files.length) {
      e.preventDefault();
      errorMessage.style.display = "block";
    } else {
      errorMessage.style.display = "none";
      console.log("File uploaded, proceeding with prediction...");
    }
  });
});
