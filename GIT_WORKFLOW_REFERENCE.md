# 🚀 GIT WORKFLOW REFERENCE — MOHAN
> Save this file in your GitHub repo as `GIT_WORKFLOW_REFERENCE.md` for future reference

---

## 📌 REPO DETAILS
- **GitHub Repo:** https://github.com/mohanmuthuraja/GenAI
- **Home Laptop Path:** `C:\Gen AI - SE\python-projects`
- **Office Laptop Path:** `D:\python-practice`
- **Virtual Env (Home):** `pyautoenv` → `C:\Gen AI - SE\python-projects\pyautoenv`
- **Virtual Env (Office):** `virenv` → `D:\python-practice\virenv`

---

## 🔄 DAILY WORKFLOW

### START OF DAY (any device)
```
VS Code → Source Control → ... → Pull
```
or in terminal:
```cmd
git pull origin main
```

### DURING WORK (save progress)
```
VS Code → Source Control → + (stage) → type message → ✔ Commit
```
or in terminal:
```cmd
git add .
git commit -m "feat: describe what you did"
```

### END OF DAY (before switching device)
```
VS Code → Source Control → Sync Changes
```
or in terminal:
```cmd
git push origin main
```

---

## 💻 DEVICE SYNC FLOW

```
HOME LAPTOP ──push──► GITHUB ──pull──► OFFICE LAPTOP
OFFICE LAPTOP ──push──► GITHUB ──pull──► HOME LAPTOP
```

---

## 🛠️ ONE TIME SETUP (New Device)

### Step 1 — Configure Git Identity
```cmd
git config --global user.name "mohanmuthuraja"
git config --global user.email "your-email@gmail.com"
```

### Step 2 — Clone Repo
```cmd
git clone https://github.com/mohanmuthuraja/GenAI.git
```

### Step 3 — Create Virtual Environment
```cmd
python -m venv virenv
virenv\Scripts\activate
```

### Step 4 — Install All Packages
```cmd
pip install -r requirements.txt
```

### Step 5 — Select Interpreter in VS Code
```
Ctrl+Shift+P → Select Interpreter → choose virenv
```

---

## ⚡ ACTIVATE VIRTUAL ENVIRONMENT

### Home Laptop
```cmd
cd "C:\Gen AI - SE\python-projects"
pyautoenv\Scripts\activate
```

### Office Laptop
```cmd
cd D:\python-practice
virenv\Scripts\activate
```

---

## 📦 PACKAGE MANAGEMENT

### Install all packages (from requirements.txt)
```cmd
pip install -r requirements.txt
```

### Add new package and update requirements.txt
```cmd
pip install package-name
pip freeze > requirements.txt
git add requirements.txt
git commit -m "feat: add new package"
git push origin main
```

---

## 🔧 USEFUL GIT COMMANDS

| Command | What it does |
|---------|-------------|
| `git status` | Check current state |
| `git log --oneline` | See commit history |
| `git pull origin main` | Get latest from GitHub |
| `git push origin main` | Send changes to GitHub |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit with message |
| `git commit -am "msg"` | Stage + commit together |
| `git stash` | Temporarily save changes |
| `git stash pop` | Bring back stashed changes |
| `git branch` | Check current branch |
| `git remote -v` | Check connected repo |

---

## ⚠️ GOLDEN RULES

1. **Always PULL before starting work**
2. **Always PUSH before switching devices**
3. **Never work on both laptops simultaneously**
4. **Never push virtual environments** (virenv, pyautoenv are in .gitignore)
5. **Write meaningful commit messages**
6. **Never commit .env or credentials**

---

## 🗂️ FOLDER STRUCTURE

```
GenAI/
├── pyautogui/           ← PyAutoGUI projects
│   ├── flask_demo/
│   ├── playwright/
│   ├── streamlit/
│   └── *.py files
├── Python_tutorial1/    ← Python tutorials
├── python/              ← Python practice files
├── .gitignore           ← Ignores virenv, pyautoenv, __pycache__
├── requirements.txt     ← All package dependencies
└── README.md
```

---

## 🔴 IF CONFLICT HAPPENS

```cmd
git pull origin main --allow-unrelated-histories
```
Then in VS Code → open conflicted file → click **Accept Both Changes** → save

```cmd
git add .
git commit -m "fix: resolve merge conflict"
git push origin main
```

---

## 🔀 SWITCHING BETWEEN REPOS IN VS CODE

```
Finish current repo work → push
File → Open Folder → select other project folder
VS Code auto-connects to that repo!
```

Or use: **File → Open Recent** to quickly switch

---

## 📝 COMMIT MESSAGE FORMAT

```
feat: add new feature
fix: fix a bug
docs: update documentation
chore: update packages or config
refactor: restructure code
```

---

*Last Updated: February 2026*
