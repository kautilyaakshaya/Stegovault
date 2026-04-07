# 🔐 StegoVault Ultimate

StegoVault Ultimate is a secure steganography desktop application that allows users to hide encrypted data inside images while keeping them visually unchanged.

It combines cryptography (AES-GCM) and steganography (LSB embedding) to provide both data secrecy and invisibility.

---

## 🚀 Key Features

### 🔐 Security
- AES-GCM encryption (confidentiality + integrity)
- Password-based key derivation (PBKDF2)
- Safe extraction with wrong-password detection
- No partial or corrupted data leaks

---

### 📦 Data Handling
- Hide text messages
- Hide any type of file
- Multi-file support
- Original filename restoration
- Built-in compression (zlib for higher capacity)

---

### 🧬 Steganography Engine
- 2-bit LSB embedding (higher capacity)
- Deterministic pixel shuffling using SHA-256
- Length-header encoding (prevents corruption)
- Exact bit-level extraction

---

### 🎨 User Interface
- Modern GUI using CustomTkinter
- Drag & Drop support
- Image preview before and after embedding
- Alerts after completion
- Reset and Exit buttons

---

### 🧠 Analysis Tools
- Basic steganography detection
- Heatmap visualization of modified pixels

---

## ⚙️ How It Works

User Data  
↓  
Compression (zlib)  
↓  
AES-GCM Encryption  
↓  
Length Header Added  
↓  
Bitstream Conversion  
↓  
Pixel Shuffling (password-based)  
↓  
2-bit LSB Embedding  
↓  
Stego Image  

---
## 📁 Project Structure

```
StegoVault/
│
├── main.py
├── requirements.txt
├── README.md
│
├── core/
│   ├── crypto.py        # Encryption + compression (AES-GCM)
│   ├── stego_engine.py  # Data hiding & extraction logic
│   ├── container.py     # File packing/unpacking
│
├── analysis/
│   ├── detector.py      # Steganography detection
│   ├── heatmap.py       # Visualization of modified pixels
│
├── ui/
│   └── gui.py           # Graphical User Interface
```

## 🛠 Installation

1. Clone repository
git clone https://github.com/YOUR_USERNAME/StegoVault.git
cd StegoVault

2. Install dependencies
pip install -r requirements.txt

3. Run application
python main.py

---

## 📖 User Guide

### Hide Data
1. Select an image (PNG/BMP)
2. Add text or files
3. Enter password
4. Click "Hide"
5. Save output image

### Extract Data
1. Select stego image
2. Enter password
3. Choose output folder
4. Extract files

### Additional Tools
- Analyze → detect hidden data
- Heatmap → visualize changes
- Reset → clear fields
- Exit → close application

---

## 📊 Capacity

512×512 image → ~100–150 KB  
1024×1024 image → ~400–600 KB  
2048×2048 image → ~2–3 MB  

---

## ⚠️ Limitations

- Works best with PNG or BMP images
- JPEG is not supported (compression destroys data)
- Resizing or editing the image corrupts hidden data
- Large data requires larger images
- Not resistant to advanced forensic tools
- Password cannot be recovered if forgotten

---

## 🎯 Use Cases

- Secure communication
- Privacy protection
- Cybersecurity learning
- Data hiding experiments
- Academic projects

---

## 🏆 Highlights

- Combines cryptography + steganography
- Handles corruption and wrong-password cases safely
- Modular and clean architecture
- High-capacity embedding system

---

## 🧠 Future Improvements

- Error correction (Reed-Solomon)
- Anti-detection techniques
- Web version
- AI-based steganalysis
- Video/audio support

---

## 📜 License

For educational and research purposes only.

---

## 💬 Summary

StegoVault Ultimate is a powerful project demonstrating how encrypted data can be securely hidden inside images, making it highly relevant for cybersecurity and software engineering.
