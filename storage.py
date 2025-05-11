import os
from datetime import datetime

def save_entry(content: str):
    date = datetime.now().strftime("%Y-%m-%d")
    os.makedirs("logs", exist_ok=True)
    with open(f"logs/{date}.md", "a") as file:
        file.write(content + "\n")
