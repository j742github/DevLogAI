from datetime import datetime

def format_entry(text: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"### {now}\n- {text}\n"
