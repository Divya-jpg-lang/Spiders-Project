# Setup and Git/GitHub Quick Guide

## A. Verify Python in the terminal
Open Windows Command Prompt or Git Bash and run:

```bash
python --version
```

If that does not work on Windows, try:

```bash
py --version
```

Create a file named `hello.py` containing:

```python
print("Hello from Python terminal")
```

Navigate to the folder containing the file and run `python hello.py` (or `py hello.py`). This proves you can execute Python without relying on the IDE run button.

## B. Git Bash
Open Git Bash and try:

```bash
pwd
ls
cd path/to/your/project
git --version
```

Replace `path/to/your/project` with your actual folder path.

## C. Create and push a GitHub repository
1. Sign in at https://github.com and create a **public** repository, for example `thdcihet-python-assignment` (use private only if instructed).
2. Do not initialize it with a README if you are pushing this existing folder with its README.
3. In Git Bash, move to this project folder and run:

```bash
git init
git add .
git commit -m "Add Python fundamentals and mini-project proposal"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/thdcihet-python-assignment.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username and use the repository URL GitHub actually gives you. If Git asks you to identify yourself, configure:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

Then repeat the commit if it previously failed. Authenticate through Git Credential Manager/browser when prompted; do not put passwords or tokens directly in commands.

## D. Add reviewers
On your repository page, open **Settings → Collaborators** (wording may vary) and invite your peer and `gauravbhatt19`. Confirm the correct account before inviting. If the account cannot be found or permissions are unavailable, report that as pending rather than claiming it is done.

## E. Final verification
- Refresh the GitHub repository page and confirm `main.py`, `README.md`, `SETUP_AND_GIT.md`, and `PRESENTATION_NOTES.md` appear.
- Make a small edit, then run `git add .`, `git commit -m "Update progress checklist"`, and `git push`.
- Keep the README checklist honest.
