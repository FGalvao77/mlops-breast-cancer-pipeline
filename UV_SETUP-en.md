# `uv` SETUP AND USAGE GUIDE

---
---

`uv` is an extremely fast Python package and project manager written in _Rust Lang_. It serves as a drop-in replacement for tools like `pip`, `pip-tools`, `venv`, and `poetry`.

---

## 1. Installation (Linux/macOS)

If you haven't installed it yet, the official command is:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*Ensure that `~/.local/bin` is in your PATH.*

---

## 2. Setting up in an existing project

### Case 1: Project already has a `pyproject.toml`

Simply sync the dependencies to create the virtual environment:

```bash
uv sync
```

### Case 2: Project does **NOT** have a `pyproject.toml` (scripts only)

Initialize `uv` support in the directory:

```bash
uv init
```

This will create the base files (`pyproject.toml`, `.python-version`).

### Case 3: Migrating from `requirements.txt`

If you already have a list of dependencies:

```bash
uv add -r requirements.txt
```

---

## 3. Daily workflow

### Managing dependencies

- **Add a package:** `uv add requests`
- **Add for development:** `uv add --dev pytest`
- **Remove a package:** `uv remove requests`

### Running the project

`uv` automatically manages the virtual environment through the `run` command:

```bash
uv run your_script.py
```

*This ensures the script uses the libraries installed in the project's `.venv`.*

---

## 4. Git and GitHub integration

### What to commit?

- ✅ **`pyproject.toml`**: Defines dependencies and metadata.
- ✅ **`uv.lock`**: Ensures all developers use the **exact** same versions.

### What to ignore?

Add this to your `.gitignore`:

```text
.venv/
```

---

## 5. Extra Tips

- **Pin Python version:** `uv python pin 3.12`
- **Clear cache:** `uv cache clean`
- **Update all packages:** `uv lock --upgrade`