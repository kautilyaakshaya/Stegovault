# 🔐 StegoVault Ultimate

A modern **steganography + cryptography** tool that allows you to securely hide and retrieve data inside images with a professional graphical interface.

---

# 📌 Overview

**StegoVault Ultimate** combines two powerful security techniques:

```
1. Hides data (Steganography)
2. Protects data (Cryptography)
```

It enables users to embed secret messages or files inside images in a way that is **invisible to the human eye**, while also encrypting the data so it cannot be accessed without the correct password.

---

# 🚀 Features

## 🔐 Core Features

* Hide **text messages** inside images
* Hide **files (any format)** inside images
* Extract hidden data securely
* AES-GCM encryption (strong, authenticated encryption)
* Password-based security (PBKDF2 key derivation)

---

## 🧬 Advanced Steganography

* LSB (Least Significant Bit) embedding
* Randomized pixel selection (password-based)
* Multi-file container system
* Filename preservation during extraction

---

## 🧠 Security & Analysis

* 🔍 Steganography detection (basic analysis)
* 🔥 Heatmap visualization of hidden regions
* 🧪 Wrong password detection (safe failure, no crash)

---

## 🎨 User Interface

* Modern GUI using CustomTkinter
* Drag & Drop image support
* Image preview (original vs stego)
* Password strength indicator
* Alerts and status messages
* Reset and Exit controls

---

# 🛠 Installation

## 1. Clone the Repository

```bash
git clone <your-repo-link>
cd StegoVault
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run the Application

```bash
python main.py
```

---

# 📁 Project Structure

```
StegoVault/
│
├── main.py                # Entry point
├── requirements.txt
│
├── core/                 # Core functionality
│   ├── crypto.py         # Encryption logic
│   ├── stego_engine.py   # Data hiding & extraction
│   ├── container.py      # Multi-file handling
│
├── analysis/             # Advanced tools
│   ├── detector.py       # Hidden data detection
│   ├── heatmap.py        # Visualization
│
├── ui/                   # User Interface
│   └── gui.py
│
├── utils/                # Utility functions
│   └── capacity.py
```

---

# 📖 User Manual

## 🔹 Step 1: Select Image

* Click **“Select Image”** or drag & drop an image
* Supported formats: PNG, BMP, TIFF

---

## 🔹 Step 2: Add Data

### Option A: Add File

* Click **“Add File”**
* Select any file to hide

### Option B: Enter Text

* Type your message in the text box
* It will be stored as a file internally

---

## 🔹 Step 3: Enter Password

* Provide a secure password
* This will be used to encrypt and protect the data

---

## 🔹 Step 4: Hide Data

* Click **“Hide Data”**
* Choose output image location
* A new image will be created with hidden data

---

## 🔹 Step 5: Extract Data

* Select the stego image
* Enter correct password
* Choose folder to save extracted files

---

## 🔹 Additional Tools

### 🔍 Analyze Image

* Detects if image may contain hidden data

### 🔥 Heatmap

* Shows visual differences between original and stego image

### 🔄 Reset

* Clears all inputs

### ❌ Exit

* Closes application

---

# 📊 Data Capacity

The amount of data you can hide depends on image size.

### Approximate limits:

| Image Size | Data Capacity |
| ---------- | ------------- |
| 512×512    | ~50–80 KB     |
| 1024×1024  | ~200–300 KB   |
| 2048×2048  | ~1–2 MB       |

---

# ⚠️ Limitations

## 📦 Data Size Limit

* Large files require large images
* Exceeding capacity causes failure

---

## 🖼 Image Restrictions

* Only lossless formats supported (PNG, BMP)
* JPEG is **not safe** (data loss due to compression)

---

## 🔍 Detectability

* Advanced steganalysis tools may detect hidden data
* Built-in detector is **not 100% accurate**

---

## 🧪 Fragility

Hidden data may be lost if image is:

* Resized
* Compressed
* Edited
* Re-saved

---

## 🔐 Security Limitations

* Weak passwords reduce security
* Not resistant to advanced forensic attacks

---

## 📦 File Limitations

* File metadata (timestamps, permissions) not preserved
* Folder structure not maintained

---

# 🎯 Use Cases

* Secure communication
* Digital watermarking
* Privacy protection
* Cybersecurity learning
* Data hiding experiments

---

# 🏆 Project Strength

```
✔ Strong academically
✔ Strong for interviews
❌ Not production-secure (yet)
```

---

# 🧠 Future Improvements

* Data compression (increase capacity)
* Stronger anti-detection techniques
* Web-based interface
* AI-based steganalysis
* Folder structure preservation

---

# 📜 License

This project is for educational and research purposes.

---

# 💬 Final Summary

StegoVault Ultimate is a complete system that:

* Hides data inside images
* Encrypts it securely
* Allows safe retrieval
* Provides analysis and visualization tools

All in a single, easy-to-use application.

---
