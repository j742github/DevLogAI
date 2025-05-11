from devlogai.formatter import format_entry

def test_format_entry():
    text = "Fixed bug and wrote tests"
    formatted = format_entry(text)
    assert "Fixed bug and wrote tests" in formatted
