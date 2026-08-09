import os
import sys
import subprocess
import venv

def run_command(command, venv_python=None):
    """Run a shell command using virtual environment python if available."""
    if venv_python and os.path.exists(venv_python):
        # Replace 'python' in command with venv python path
        if command.startswith("python "):
            command = f'"{venv_python}" ' + command[7:]
        elif command.startswith("pip "):
            pip_path = os.path.join(os.path.dirname(venv_python), "pip")
            command = f'"{pip_path}" ' + command[4:]
    
    print(f"\n[EXEC] Running: {command}")
    res = subprocess.run(command, shell=True)
    if res.returncode != 0:
        print(f"[ERROR] Command failed with exit code {res.returncode}")
        sys.exit(res.returncode)

def main():
    print("=" * 60)
    print("      Flora_AI Project Local Environment Setup")
    print("=" * 60)

    project_dir = os.path.abspath(os.path.dirname(__file__))
    venv_dir = os.path.join(project_dir, "venv")

    # Determine OS specific paths
    if sys.platform == "win32":
        venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
        venv_pip = os.path.join(venv_dir, "Scripts", "pip.exe")
        activate_cmd = r".\venv\Scripts\activate"
    else:
        venv_python = os.path.join(venv_dir, "bin", "python")
        venv_pip = os.path.join(venv_dir, "bin", "pip")
        activate_cmd = "source venv/bin/activate"

    # Step 1: Create Virtual Environment
    if not os.path.exists(venv_dir):
        print("\n[1/4] Creating virtual environment ('venv')...")
        venv.create(venv_dir, with_pip=True)
        print("✔ Virtual environment created successfully.")
    else:
        print("\n[1/4] Virtual environment ('venv') already exists.")

    # Step 2: Upgrade pip
    print("\n[2/4] Upgrading pip...")
    run_command(f'"{venv_python}" -m pip install --upgrade pip')

    # Step 3: Install dependencies from requirements.txt
    req_file = os.path.join(project_dir, "requirements.txt")
    if os.path.exists(req_file):
        print("\n[3/4] Installing requirements from requirements.txt...")
        run_command(f'"{venv_pip}" install -r "{req_file}"')
    else:
        print("\n[3/4] WARNING: requirements.txt not found!")

    # Step 4: Run Django Migrations
    manage_py = os.path.join(project_dir, "manage.py")
    if os.path.exists(manage_py):
        print("\n[4/4] Applying Django database migrations...")
        run_command(f'"{venv_python}" "{manage_py}" migrate')
    else:
        print("\n[4/4] WARNING: manage.py not found!")

    print("\n" + "=" * 60)
    print(" SUCCESS! Environment setup is complete.")
    print("=" * 60)
    print("\nTo start working on the project:")
    print(f"1. Activate virtual environment:  {activate_cmd}")
    print("2. Run the development server:     python manage.py runserver")
    print("=" * 60)

if __name__ == "__main__":
    main()
