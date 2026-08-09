# Flora_AI Project

Welcome to the **Flora_AI** team repository!

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
3. Installs all required packages listed in [requirements.txt](file:///c:/Data%20Science%20and%20Gen%20Ai%20projects/Flora_AI/requirements.txt).
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

---

## 📌 GitHub Initialization & Pushing (Repository Admin)

If you have not added this project to GitHub yet, run the following commands in your project root terminal:

### 1. Initialize Git Repository
```bash
git init
```

### 2. Stage All Project Files
*(Note: [.gitignore](file:///c:/Data%20Science%20and%20Gen%20Ai%20projects/Flora_AI/.gitignore) ensures `venv`, `db.sqlite3`, and `__pycache__` are excluded automatically).*
```bash
git add .
```

### 3. Commit the Setup Files & Project
```bash
git commit -m "Initial commit: Add project core, requirements, and setup scripts"
```

### 4. Link to GitHub and Push
Create a new repository on GitHub (e.g. `Flora_AI`), then execute:
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Flora_AI.git
git push -u origin main
```
