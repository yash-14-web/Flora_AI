# Flora_AI

Flora AI is an AI-powered plant health platform that detects plant diseases from leaf images using CNNs and provides actionable treatment advice. Built for farmers and agronomists, it aims to grow into a broader agricultural intelligence suite with localized weather insights, nutrient detection, and offline support.

---

## 🚀 Quick Setup for Team Members

Follow these instructions to set up your local development environment.

### 1. Run the Setup Script

Choose the script for your operating system:

#### **Windows Users (PowerShell / Command Prompt):**
Double-click `setup.bat` or run:
```cmd
.\setup.bat
```

#### **Mac / Linux Users (Terminal):**
Make script executable and run:
```bash
chmod +x setup.sh
./setup.sh
```

#### **Cross-Platform (Python):**
```bash
python setup.py
```

---

### 🛠 What the Setup Script Automatically Does
1. Creates a Python virtual environment (`venv`) if one doesn't exist.
2. Upgrades `pip` to the latest version.
3. Installs all required packages listed in [requirements.txt](requirements.txt).
4. Runs database migrations (`python manage.py migrate`).

---

## 💻 Running the Application Locally

After running setup, activate your virtual environment and start the Django development server:

### Windows:
```cmd
.\venv\Scripts\activate
python manage.py runserver
```

### Mac / Linux:
```bash
source venv/bin/activate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.
