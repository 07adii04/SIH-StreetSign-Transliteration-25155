Here’s your **final, professional README.md** — fully formatted for GitHub and optimized for showcasing in your resume or portfolio 🌟

It highlights your **technical depth**, **project purpose (SIH 25155)**, and **deployability**, making it stand out for recruiters or hackathon judges.

---

```markdown
# 🛣️ Street Sign Transliteration Tool  
*A Smart India Hackathon 2025 Project — Problem Statement #25155*

---

## 📘 Overview

The **Street Sign Transliteration Tool** is an open-source web application designed to detect and transliterate multilingual **Indian street signboards** into user-selected Indic scripts.

Built using **Streamlit**, **EasyOCR**, and **Indic-Transliteration**, this tool demonstrates how AI and NLP can bridge linguistic barriers across India’s diverse language landscape.

---

## 🧠 Features

✅ **Multilingual OCR**  
- Detects and reads text in **English**, **Hindi**, **Tamil**, and **Telugu** using EasyOCR.

✅ **Intelligent Transliteration**  
- Automatically identifies the script and transliterates only Indic lines into your chosen target script.

✅ **Fast & Optimized**  
- Uses `st.cache_resource` to cache OCR models and prevent memory crashes or reload delays.

✅ **User-Friendly Streamlit UI**  
- Upload or test with a sample image.
- Choose your target script.
- Instantly view and copy the transliterated output.

✅ **Deployment-Ready**  
- Lightweight dependencies.
- Fully compatible with **Streamlit Cloud** and **Hugging Face Spaces**.

---

## ⚙️ Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Frontend** | Streamlit |
| **OCR Engine** | EasyOCR (with PyTorch backend) |
| **Transliteration** | Indic-Transliteration |
| **Image Processing** | Pillow (PIL) |
| **Languages Supported** | English, Hindi, Tamil, Telugu |

---

## 🧩 How It Works

1. **Upload a street sign image** (or use the built-in example).  
2. The app runs **EasyOCR** to extract all visible text.  
3. A logic filter detects which lines are in Indic scripts.  
4. These lines are **transliterated** into your selected script (e.g., Tamil → Devanagari).  
5. The output text is displayed with a **copy-to-clipboard** button.

---

## 🧠 Architecture

```

┌────────────────────┐
│   User Uploads     │
│   Image (JPG/PNG)  │
└────────┬───────────┘
│
▼
┌────────────────────┐
│   EasyOCR Engine    │
│  (Text Extraction)  │
└────────┬───────────┘
│
▼
┌────────────────────┐
│  Script Detection   │
│ (Indic vs English)  │
└────────┬───────────┘
│
▼
┌────────────────────┐
│ Indic-Transliteration│
│   (Target Script)    │
└────────┬───────────┘
│
▼
┌────────────────────┐
│ Streamlit Interface │
│ (Display + Copy)    │
└────────────────────┘

````

---

## 🧮 Example Output

| Input Sign | Extracted Text | Transliterated Text |
|-------------|----------------|---------------------|
| देवनागरी स्ट्रीट | देवनागरी स्ट्रीट | devanāgarī strīṭ |
| தமிழ்நாடு | தமிழ்நாடு | tamilnāḍu |
| తెలుగు వీధి | తెలుగు వీధి | telugu vīdhi |

---

## 💻 Run Locally

Clone the repository and run the app:

```bash
git clone https://github.com/07adii04/SIH-StreetSign-Transliteration-25155
cd StreetSign-Transliteration
pip install -r requirements.txt
streamlit run app.py
````

Then open the app in your browser at:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🧩 Project Structure

```
StreetSign-Transliteration/
│
├── app.py                        # Streamlit web interface
├── requirements.txt               # Dependencies
│
├── src/
│   └── transliterator.py          # OCR + Transliteration logic
│
├── assets/
│   └── sample_sign.jpg            # Optional local test image
│
└── .streamlit/
    └── config.toml                # UI theme settings
```

---

## 🌐 Deployment

This project can be deployed easily on:

* [Streamlit Cloud](https://share.streamlit.io/)
* [Hugging Face Spaces](https://huggingface.co/spaces)
* [Render](https://render.com)

### Streamlit Cloud Steps

1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Click **“New App” → Select your repo → Main file = `app.py`**.
4. Deploy and get your public link! 🌍

---

## 🧰 Dependencies

```
streamlit==1.38.0
easyocr==1.7.2
Pillow==10.4.0
indic-transliteration==2.4.0
streamlit-copy-button==0.3.3
requests==2.31.0
torch==2.3.0
torchvision==0.18.0
```

---

## 📜 License

This project is open-source under the **MIT License**.
You are free to use, modify, and distribute it with attribution.

---

## 👨‍💻 Author

**Aditya Tiwari**
📍 *India*
💼 *Smart India Hackathon 2025 Participant*
🚀 *Focus Areas: AI, Cybersecurity, and Applied Machine Learning*

🔗 [GitHub Profile](https://github.com/07adii04)
🔗 [LinkedIn Profile](https://www.linkedin.com/in/aditya-tiwari-b2866a333/)

---

## 🏁 Status

✅ Stable & Optimized
🧩 Ready for Deployment
📦 Ideal for Resume & Portfolio Showcase

> “Bridging India’s languages, one signboard at a time.” 🇮🇳

```

---


```
