# 🧮 IP Calculator Web App

A small Flask-based web app that wraps around `ipcalc` to calculate network info from an IP address and CIDR mask.

## 🧪 Features

- Enter any IP and CIDR (e.g. 192.168.1.0/24)
- See the full output of `ipcalc` (network, broadcast, hosts, etc.)
- Very beginner-friendly and expandable!

## 🚀 Getting Started

1. Install Flask:  
   `pip install flask`

2. Install ipcalc:  
   Linux: `sudo apt install ipcalc`  
   macOS: `brew install ipcalc`

3. Run the app:  
   `python app.py`

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 💡 To improve

- Input validation
- Styling with CSS
- Version without `ipcalc` (pure Python)