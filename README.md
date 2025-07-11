# password-strength-analyzer
A Python tool to evaluate password strength and generate custom wordlists (GUI + CLI)

# 🔐 Password Strength Analyzer with Custom Wordlist Generator

A cybersecurity project that analyzes password strength and generates custom wordlists using user input patterns. Built with Python, supporting both CLI and GUI interfaces.

---

## 📌 Features

- ✅ Password strength analysis using `zxcvbn`
- ✅ GUI (Tkinter) and CLI support
- ✅ Generates custom wordlists based on:
  - Name
  - Date of Birth
  - Pet Name
- ✅ Adds variations using:
  - Leetspeak substitutions
  - Common year patterns
- ✅ Exports wordlist in `.txt` format (compatible with cracking tools like Hydra or John)

---

## 🧰 Tools & Libraries Used

- Python 3.13
- `zxcvbn-python` – password strength estimator
- `argparse` – CLI interface
- `tkinter` – GUI interface
- `nltk` *(optional)* – for future natural language processing enhancements

---

## 📸 Screenshots

<img src="screenshots/gui1.png" width="400"/>  
<img src="screenshots/gui2.png" width="400"/>

---

## 🧪 How to Run

### ✅ Step 1: Set up virtual environment
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

Step 2: Run in CLI mode

python3 cli.py -p "Tiger@2025" --name Tiger --dob 2000-01-01 --pet Bruno

Step 3: Run GUI
python3 gui.py
