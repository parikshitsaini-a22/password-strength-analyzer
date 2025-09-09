# Password Strength Analyzer with Custom Wordlist Generator

A Python tool that evaluates password strength and generates custom wordlists.

## Features
- Password strength analysis using `zxcvbn`.
- Custom wordlist generation (names, pets, years, leetspeak).
- Exports `.txt` wordlists for use in cracking tools.
- CLI and GUI interface (Tkinter + Streamlit optional).

## Installation
```bash
git clone https://github.com/<your-username>/password-strength-analyzer.git
cd password-strength-analyzer
pip install -r requirements.txt
```

## Usage

### CLI
```bash
python -m src.cli --password "P@ssw0rd123" --name "John" --pet "rex" --years 2000-2005 --out wordlist.txt
```

### GUI
```bash
python -m src.gui_tk
```

### Streamlit (optional live demo)
```bash
streamlit run src/app_streamlit.py
```

