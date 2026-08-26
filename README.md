# Data Analytics Learning Workspace (NumPy, Pandas, Matplotlib, Seaborn)

Repository for learning NumPy, Pandas, Matplotlib, and Seaborn, building foundations towards Data Science and AI Agent Automation Development.

---

## 🚀 Virtual Environment Setup & Usage

### 1. Activate the Virtual Environment

- **PowerShell (Windows)**:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(If you get a script execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once in PowerShell).*

- **Command Prompt (cmd)**:
  ```cmd
  venv\Scripts\activate.bat
  ```

- **Git Bash / Bash**:
  ```bash
  source venv/Scripts/activate
  ```

---

### 2. VS Code Configuration
VS Code is automatically configured via [`.vscode/settings.json`](file:///d:/4th%20sem%20summer/data%20analytics/.vscode/settings.json) to use the project virtual environment (`venv\Scripts\python.exe`) and auto-activate it in new terminals.

To manually select the Python interpreter in VS Code:
1. Press `Ctrl + Shift + P`
2. Search and select `Python: Select Interpreter`
3. Choose the one marked `('venv': venv) .\venv\Scripts\python.exe`

---

### 3. Installed Packages
The environment includes all core data analytics libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `openpyxl` (for reading and writing Excel `.xlsx` files)
- `scipy` & `statsmodels` (statistical functions and modeling)
- `scikit-learn` (machine learning and preprocessing)
- `ipykernel` (Jupyter notebook and interactive window support)
- `tabulate` (DataFrame pretty-printing)

To reinstall or replicate in a new environment:
```bash
pip install -r requirements.txt
```

