import os
import subprocess

def list_files(directory: str = ".") -> str:
    """Lists files in the directory tree ignoring hidden and venv files."""
    results = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
        for f in files:
            if not f.startswith("."):
                rel_path = os.path.relpath(os.path.join(root, f), directory)
                results.append(rel_path)
    return "\n".join(results[:50])

def read_file_lines(file_path: str, start_line: int, end_line: int) -> str:
    """Reads specific line ranges from a source file."""
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found."
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    selected = lines[max(0, start_line - 1):end_line]
    return "".join(selected)

def apply_patch(file_path: str, old_code: str, new_code: str) -> str:
    """Replaces target code with updated code."""
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found."
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if old_code not in content:
        return "Error: old_code target block not found."
    updated = content.replace(old_code, new_code, 1)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated)
    return f"Success: Patched {file_path}."

def run_test_suite(test_command: str = "pytest") -> str:
    """Runs tests locally in sandbox/workspace."""
    try:
        proc = subprocess.run(
            test_command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        return proc.stdout or proc.stderr
    except Exception as e:
        return f"Execution error: {str(e)}"