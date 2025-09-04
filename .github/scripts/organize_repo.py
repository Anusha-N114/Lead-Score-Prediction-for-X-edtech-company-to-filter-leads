import os, glob, shutil, subprocess
from datetime import datetime

TARGETS = {
    "*.csv": "data/raw", "*.tsv": "data/raw", "*.xlsx": "data/raw",
    "*.xls": "data/raw", "*.parquet": "data/raw", "*.json": "data/raw",
    "*.ipynb": "notebooks",
    "*.py": "src",
    "*.sql": "sql",
    "*.png": "reports/figures", "*.jpg": "reports/figures",
    "*.jpeg": "reports/figures", "*.svg": "reports/figures", "*.gif": "reports/figures",
    "*.pdf": "docs", "*.pptx": "docs", "*.ppt": "docs", "*.docx": "docs",
    "*.pbix": "reports", "*.pbit": "reports",
}
IGNORE_DIRS = {".git", ".github", "venv", ".venv", "__pycache__", ".idea", ".vscode",
               ".mypy_cache", ".pytest_cache", "env", "node_modules"}
TARGET_ROOTS = {"data", "notebooks", "src", "reports", "sql", "docs"}
LOG_PATH = ".github/auto-structure-log.txt"

def log(msg):
    print(msg)
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def already_sorted(p):
    parts = os.path.normpath(p).split(os.sep)
    return parts and parts[0] in TARGET_ROOTS

def ignored(p):
    parts = set(os.path.normpath(p).split(os.sep))
    return bool(parts & IGNORE_DIRS)

def git_mv(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    base, ext = os.path.splitext(os.path.basename(dst))
    final = dst
    i = 1
    while os.path.exists(final):
        final = os.path.join(os.path.dirname(dst), f"{base}_{i}{ext}")
        i += 1
    try:
        subprocess.run(["git", "mv", src, final], check=True)
        log(f"✅ git mv: {src} -> {final}")
    except subprocess.CalledProcessError:
        shutil.move(src, final)
        log(f"✅ move:   {src} -> {final}")

def main():
    log(f"=== Auto-Structure DEBUG @ {datetime.utcnow().isoformat()}Z ===")
    for d in ["data/raw","data/processed","notebooks","src","reports/figures","sql","docs"]:
        os.makedirs(d, exist_ok=True)

    log("\nRoot contents:")
    for item in sorted(os.listdir(".")):
        log(f" - {item}")

    moved = 0
    for pattern, dest in TARGETS.items():
        log(f"\n🔎 Pattern: {pattern} -> {dest}")
        matches = sorted(glob.glob(f"**/{pattern}", recursive=True))
        if not matches:
            log("  (no matches)")
            continue
        for path in matches:
            if os.path.isdir(path): continue
            if ignored(path):
                log(f"⏭️  Ignored: {path}"); continue
            if already_sorted(path):
                log(f"📂 Already sorted: {path}"); continue
            if os.path.basename(path).lower() == "readme.md":
                log(f"⏭️  Keep README: {path}"); continue
            git_mv(path, os.path.join(dest, os.path.basename(path)))
            moved += 1

    if moved == 0:
        log("\nℹ️  No files moved (either none matched or already organized).")
    else:
        log(f"\n✅ Done. Files moved: {moved}")

if __name__ == "__main__":
    main()
