from devlogai.formatter import format_entry
from devlogai.storage import save_entry

def capture_entry():
    print("What did you work on today?")
    entry = input("> ")
    formatted = format_entry(entry)
    save_entry(formatted)
    print("✅ Entry saved!")
