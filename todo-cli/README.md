# Todo CLI 📝

A sleek, lightweight, and efficient Command Line Interface (CLI) application built with Python to manage your daily tasks seamlessly from the terminal. 

---

## 🚀 Features

*   **Task Management:** Easily add, view, update, and delete tasks.
*   **Persistent Storage:** All tasks are saved securely in a local `todo.json` file.
*   **Fast & Lightweight:** Powered by `uv` for lightning-fast environment setup and dependency management.
*   **Clean CLI Interface:** Simple and intuitive commands designed for developers who love the terminal.

---

## 🛠️ Tech Stack & Prerequisites

*   **Language:** Python 3.12+
*   **Package Manager:** [uv](https://github.com/astral-sh/uv) (Astral's ultra-fast Python bundler)

---

## 📥 Installation & Setup

Follow these steps to get the project running locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/zyanshykh/todo-list.git](https://github.com/zyanshykh/todo-list.git)

cd todo-list/todo-cli

Bash
# Sync dependencies and set up the virtual environment
uv sync

uv run todo.py add "Finish writing the project documentation"

uv run todo.py list

uv run todo.py complete <task_id>

uv run todo.py delete <task_id>
```

## 📂 Project Structure

todo-cli/
├── .python-version  # Target Python version
├── pyproject.toml   # Project metadata and dependencies
├── uv.lock          # Locked versions for reproducible builds
├── todo.py          # Main CLI application logic
├── todo.json        # Data storage file (generated automatically)
└── README.md        # Documentation
