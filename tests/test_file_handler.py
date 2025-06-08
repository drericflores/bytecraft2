"""Test file_handler module. This uses pytest to validate the basic behavior of your core.file_handler functions."""

import os
import tempfile
from core.file_handler import load_file, save_file, save_as_text

def test_load_and_save_binary():
    """Test binary file save and reload produces identical data."""
    original_data = bytearray(b'\x00\x01\x02ABCxyz')

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        save_file(tmp.name, original_data)
        tmp_path = tmp.name

    try:
        reloaded_data = load_file(tmp_path)
        assert original_data == reloaded_data
    finally:
        os.remove(tmp_path)

def test_save_as_text_and_reload():
    """Test saving and reading a text file."""
    text = "Hello ByteCraft!\nASCII mode test."

    with tempfile.NamedTemporaryFile(suffix=".txt", mode='w+', delete=False) as tmp:
        save_as_text(tmp.name, text)
        tmp_path = tmp.name

    try:
        loaded_data = load_file(tmp_path)
        assert loaded_data.decode() == text
    finally:
        os.remove(tmp_path)

