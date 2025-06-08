"""Module: file_handler"""

def load_file(file_path: str) -> bytearray:
    """Load file content into memory."""
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return bytearray(content.encode())
    else:
        with open(file_path, 'rb') as f:
            return bytearray(f.read())

def save_file(file_path: str, data: bytearray) -> None:
    """Save binary content to a file."""
    with open(file_path, 'wb') as f:
        f.write(data)

def save_as_text(file_path: str, text: str) -> None:
    """Save plain text to a file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

