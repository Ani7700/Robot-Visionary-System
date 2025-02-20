# Robot-Visionary-System

This repository contains a script for performing inference using a pre-trained ResNet-50 model. The model is used to classify objects in images based on the ImageNet dataset.

## Requirements

Before running the inference script, make sure you have the following dependencies installed:

```bash
pip install torch torchvision
```

## Files in this Repository

- `objdetection_inference.py`: The main inference script.
- `resnet50.pth`: Pre-trained model weights (ensure this file is present in the directory).
- `demo.jpg`: Sample image for testing the inference script.

## How to Run

1. **Prepare the Model and Image**
   - Ensure `resnet50.pth` is in the same directory as the script.
   - Place the test image (e.g., `demo.jpg`) in the directory.

2. **Run the Inference Script**

   ```bash
   python objdetection_inference.py
   ```

3. **Expected Output**
   The script will output the top 5 predicted classes along with their confidence scores. Example output:

   ```
   Top Predictions:
   Labrador retriever: 85.2%
   Golden retriever: 7.4%
   Flat-coated retriever: 3.2%
   ```

## Code Explanation

1. **Load the Pre-trained Model**
   - The script loads the ResNet-50 architecture.
   - The model weights are loaded from `resnet50.pth`.
   - The model is set to evaluation mode to disable gradient updates.

2. **Preprocess the Input Image**
   - The image is read using `torchvision.io.read_image()`.
   - Image resizing and normalization are applied using `torchvision.transforms`.
   - The image is converted into a tensor suitable for ResNet.

3. **Perform Inference**
   - The processed image is passed through the model.
   - Softmax is applied to get class probabilities.
   - The top 5 predictions are displayed with confidence scores.

## Notes
- If you encounter errors with missing model weights, ensure `resnet50.pth` is downloaded correctly.
- Modify `image_path` in `objdetection_inference.py` to test with different images.
- The model is based on ImageNet categories.

## License
This project is for educational purposes only. The ResNet-50 model is provided by PyTorch under its respective license.

## Contact
For any questions or issues, feel free to reach out via GitHub or email.

