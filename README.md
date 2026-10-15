# THDC-IHET Python Learning Assignment

## Student Progress
**Program:** Python Fundamentals and Mini-Project Preparation  
**Status:** In progress — update the checklist as work is completed.

## 1. Mini-Project Proposal

### Title
**NetGuard Lite: Basic Network Intrusion Detection Using Python**

### Real-world problem statement
Computer networks can be targeted by suspicious activity such as repeated failed login attempts, port scanning, and unusually frequent connection attempts. Small teams may not have dedicated security-monitoring tools. This project proposes a basic Python program that analyses structured network-event records and flags patterns that may deserve investigation.

### Who faces this problem?
Small businesses, college labs, student project teams, and administrators of small networks who need a simple introduction to monitoring suspicious activity.

### Why is it important?
Early identification of unusual activity can help an administrator investigate potential security incidents. The project is educational and will not claim to replace professional security tools or detect every attack.

### Possible Python / AI / ML approach
1. Start with Python lists and dictionaries to represent network-event records.
2. Use functions to count failed logins and repeated connection attempts.
3. Read sample events from a CSV file using Python's `csv` module.
4. Apply transparent threshold-based rules to flag suspicious patterns.
5. Later, explore a labelled public dataset and evaluate a machine-learning classifier using precision, recall, and a confusion matrix.

### What I need to learn
- Python fundamentals, functions, lists, dictionaries, sets, and file handling
- CSV processing and data cleaning
- Basic statistics and exploratory data analysis
- Networking and common security-event concepts
- Later: pandas and scikit-learn, train/test split, model evaluation, and responsible handling of security data

### Initial scope
For the first version, analyse a small, synthetic CSV file. Do not collect real users' network traffic or claim that synthetic examples prove real-world accuracy.

## 2. Assignment Progress Checklist

### Program and environment
- [ ] Enroll at https://thdcihet.spiders.co.in
- [ ] Install/verify Python
- [ ] Run a `.py` file from terminal/Command Prompt
- [ ] Open Git Bash and run basic commands
- [ ] Install/open VS Code

### Git and GitHub
- [ ] Create a GitHub repository
- [ ] Add `gauravbhatt19` as mentor/reviewer (if the account can be found and repository settings allow it)
- [ ] Invite a peer reviewer
- [ ] Push this work to GitHub
- [ ] Commit progress regularly

### Python fundamentals
- [ ] Variables and data types
- [ ] Conditions
- [ ] Loops
- [ ] Functions
- [ ] Data structures
- [ ] Searching and sorting
- [ ] Practice problems

### Mini-project and presentation
- [x] Write a mini-project proposal in README
- [ ] Update checklist honestly
- [ ] Prepare a live demo
- [ ] Present completed work, current work, repository, learning, and pending items

> Only mark an item complete after you have actually done it. This README is a starting point, not proof that every task is finished.

## 3. Run the Python Practice File

```bash
python main.py
```

On some Windows installations, use:

```bash
py main.py
```

## 4. Repository Contents
- `main.py` — examples of Python fundamentals, searching, sorting, and practice problems
- `README.md` — project proposal and progress checklist
- `PRESENTATION_NOTES.md` — concise presentation outline
- `SETUP_AND_GIT.md` — terminal, Git, and GitHub steps
