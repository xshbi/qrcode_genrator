

---

# 📱 QR Code Generator for Links

This repository contains a simple and efficient tool for generating QR codes from any URL. Built with Python, this project allows users to easily create QR codes that can be scanned to quickly access links.

## ✨ Features
- **Easy to Use**: Input any URL and generate a QR code with a single click.
- **Customizable**: Adjust the size and color of the QR code to fit your needs.
- **Responsive Design**: Works seamlessly on both desktop and mobile devices.
- **Downloadable**: Save the generated QR codes as image files for later use.

## 🛠️ Installation

### Prerequisites
- Python 3.x
- `virtualenv` package

### Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/xshbi/qrcode_generator.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd qrcode_generator
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Requirements
Create a `requirements.txt` file with the following content:
   ```
   qrcode
   pillow
   pyzbar
   ```

## 🚀 Usage
1. **Run the script**:
   ```bash
   python generate_qr.py
   ```
2. **Enter the URL** you want to convert into a QR code.
3. **Customize the appearance** if needed.
4. **Generate and download** the QR code image for use.

