# 📡 GitHub Portfolio Fetcher

This is a simple CLI application written in Python that connects to the GitHub API and prints a list of repositories marked for portfolio use.

The purpose of the script is to **quickly display only those GitHub projects** that are meant to be presented publicly (e.g. to recruiters or on a portfolio website).

---

## 🛠️ Technologies Used

- Python 3.10+
- `requests` library
- GitHub REST API v3
- `python-dotenv` (for reading `.env` variables)

---

## 🚀 How It Works

The script:
1. Authenticates via a GitHub token stored in `.env`
2. Fetches all public repositories
3. Filters only those that include the word `"portfolio"` in their description or topics
4. Prints them directly to the console

---

## ▶️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Yushikuni/GitHub_Fetch.git
cd GitHub_Fetch
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```
### 3. Add a .env file with your GitHub token:
```bash
GITHUB_TOKEN=ghp_yourtokenhere
```
### 4. Run the script:
```bash
python3 github_fetch.py
```

✅ Output will look like this:<br/>
🔹 TheWitcherMechanic — C++ AI logic system<br/>
🔹 TODO_CLI — Console-based task manager in C++<br/>
🔹 GitHub_Fetch — This Python script<br/>
<br/>

🧪 Example Use Case<br/>
You can use this script to:<br/>
🔹Dynamically update your portfolio content<br/>
🔹Show your most relevant projects during interviews<br/>
🔹List repositories in Node.js, React or static websites via file export (e.g. JSON, MD)<br/>

📦 TODOs future ideas<br/>
🔹Export list to JSON or Markdown<br/>
🔹Option to sort by stars or date<br/>
🔹GUI or web version<br/>
🔹Support for private repos<br/>
