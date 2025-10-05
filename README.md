# 🛣️ SIH Street Sign Transliteration Tool

> **Problem Statement ID:** SIH #25155

A powerful web application that performs Optical Character Recognition (OCR) on street signs featuring Devanagari script and seamlessly transliterates the text into multiple major Indic scripts, making street navigation accessible across linguistic boundaries.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sih-streetsign-transliteration-25155-kzqk38xsgm64zhkivjqm69.streamlit.app/)

---

## ✨ Features

- **📸 Image Upload & Processing** - Upload street sign images in common formats (JPG, PNG, JPEG)
- **🔤 Multi-Script Transliteration** - Convert Devanagari text to Telugu, Tamil, Bengali, Gurmukhi, and Gujarati scripts
- **🤖 AI-Powered OCR** - Leverages EasyOCR with PyTorch for accurate text extraction from images
- **🎨 Intuitive Interface** - Clean, user-friendly design built with Streamlit
- **💾 Export Functionality** - Download transliterated results as `.txt` files
- **⚡ Real-Time Processing** - Get instant results with minimal latency

---

## 🎯 Use Cases

- **Tourism & Navigation** - Help travelers understand street signs in unfamiliar scripts
- **Urban Planning** - Assist in creating multilingual signage systems
- **Language Learning** - Educational tool for understanding script relationships
- **Accessibility** - Make street navigation more inclusive across India's linguistic diversity

---

## 🖼️ Demo

### Application Interface
![App Screenshot](https://i.imgur.com/your-screenshot-url.png)
*Replace with your actual screenshot URL*

### Try It Live
Visit the [live demo](https://sih-streetsign-transliteration-25155-kzqk38xsgm64zhkivjqm69.streamlit.app/) to see the application in action.

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Frontend Framework** | Streamlit |
| **OCR Engine** | EasyOCR (PyTorch-based) |
| **Transliteration Library** | indic-transliteration |
| **Language** | Python 3.9+ |
| **Deployment** | Streamlit Community Cloud |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.9 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads/)
- **pip** - Python package installer (included with Python)

### Installation

Follow these steps to set up the project locally:

#### 1. Clone the Repository

```bash
git clone https://github.com/07adii04/SIH-StreetSign-Transliteration-25155.git
cd SIH-StreetSign-Transliteration-25155
```

#### 2. Create a Virtual Environment

Creating a virtual environment keeps your project dependencies isolated:

```bash
# Create virtual environment
python -m venv venv
```

Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal prompt.

#### 3. Install Dependencies

Install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

> **Note:** Installation may take several minutes as it downloads large libraries like PyTorch for the EasyOCR engine.

#### 4. Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
SIH-StreetSign-Transliteration-25155/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── [other project files]
```

---

## 🎮 How to Use

1. **Launch the Application** - Open the app in your browser
2. **Upload an Image** - Click the upload button and select a street sign image
3. **Wait for Processing** - The app will extract text using OCR
4. **View Results** - See the original Devanagari text and transliterations in multiple scripts
5. **Download** - Export the results as a text file if needed

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project was developed for Smart India Hackathon 2025. Please check the repository for license information.

---

## 👥 Team

**Developer:** Aditya Tiwari  
**Institution:** Maharana Institute of Professional Studies
**SIH Edition:** 2025

---

## 📧 Contact

For questions, feedback, or support:

- **GitHub Issues:** [Report an issue](https://github.com/07adii04/SIH-StreetSign-Transliteration-25155/issues)
- **Email:** [adityatiwari0at.adi@gmail.com]

---

## 🙏 Acknowledgments

- Smart India Hackathon organizers
- EasyOCR development team
- Streamlit community
- Contributors to the `indic-transliteration` library

---

**Made with ❤️ for Smart India Hackathon 2025**