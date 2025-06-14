# Image Caption Generator Web App

A modern web application that uses a Hugging Face Vision Transformer (ViT) + GPT-2 model to generate captions for uploaded images. Built with FastAPI (Python backend), Jinja2 templates, and Tailwind CSS for a beautiful, responsive frontend. Upload an image and instantly get an AI-generated caption!

---

## 🚀 Live Demo

[View the app online](https://your-demo-url.com) <!-- Replace with your deployed URL if available -->

---

## 🖼️ Demo Screenshot

![Demo Screenshot](image-caption-app/demo.png)

---

## 🛠️ Technologies Used

- **FastAPI** – High-performance Python web framework
- **Hugging Face Transformers** – Pretrained ViT-GPT2 image captioning model
- **Torch** – Deep learning backend
- **Pillow** – Image processing
- **Jinja2** – HTML templating
- **Tailwind CSS** – Modern, utility-first CSS framework (via CDN)
- **Uvicorn** – ASGI server for running FastAPI

---

## 📦 Project Structure

```text
image-caption-app/
├── app/
│   ├── main.py          # FastAPI application (routes, server)
│   ├── model.py         # Model loading and captioning logic
│   └── templates/
│       └── index.html   # Frontend HTML (Jinja2 + Tailwind)
├── static/
│   └── styles.css       # (Optional) Custom CSS
├── uploads/             # Stores uploaded images (must exist or be created)
├── requirements.txt     # Python dependencies
├── demo.png             # UI screenshot for README
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Running Locally

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd image-caption-app
```

### 2. Create a virtual environment (recommended)

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Ensure the `uploads/` folder exists

If not present, create it manually:

```sh
mkdir uploads
```

### 5. Run the FastAPI app

```sh
uvicorn app.main:app --reload
```

### 6. Open your browser

Go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the app.

---

## 💡 Example Usage

1. On the homepage, click the file upload area and select an image.
2. Click "Generate Caption".
3. The app will display your image and an AI-generated caption below it.

---

## 🐍 Requirements

- Python 3.8+
- See `requirements.txt` for all Python dependencies

---

## 📢 Notes

- The `uploads/` directory is required for saving uploaded images. Create it if it doesn't exist.
- The app uses the [nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) model from Hugging Face.
- Tailwind CSS is included via CDN in the HTML template (no build step needed).

---

## 🤝 Credits

- [Hugging Face](https://huggingface.co/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 📄 License

MIT License
