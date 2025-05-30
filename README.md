# Image Captioning using ViT + GPT-2

This project demonstrates how to generate captions for images and videos using a Vision Transformer (ViT) and GPT-2 model from HuggingFace. It provides an interactive Gradio user interface for easy image and video captioning.

## Features
- Generate captions for images using a state-of-the-art transformer model
- Generate captions for videos by extracting a representative frame
- Modern, wide Gradio web interface with tabs for image and video

## Demo
![Demo Screenshot](Sample.jpg)

## Installation
1. Clone this repository:
   ```sh
   git clone <your-repo-url>
   cd "Image Caption Generation using HuggingFace"
   ```
2. Install required packages:
   ```sh
   pip install transformers gradio torch pillow opencv-python
   ```

## Usage
1. Run the Jupyter notebook `caption.ipynb`.
2. Follow the notebook cells to load the model and launch the Gradio interface.
3. Use the web UI to upload images or videos and get captions.

## File Structure
```
├── caption.ipynb        # Main notebook with code and Gradio UI
├── Sample.jpg           # Example image for testing
├── README.md            # Project documentation
```

## Model
- [nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning)

## Credits
- HuggingFace Transformers
- Gradio
- PyTorch
- OpenCV

## License
This project is licensed under the MIT License.
