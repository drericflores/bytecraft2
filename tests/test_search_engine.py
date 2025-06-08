"""Test search_engine module."""

from core.search_engine import perform_search, find_and_replace

def test_perform_search_ascii_found():
    data = bytearray(b"The quick brown fox")
    index = perform_search(data, "quick", is_hex_mode=False)
    assert index == 4

def test_perform_search_ascii_not_found():
    data = bytearray(b"The quick brown fox")
    index = perform_search(data, "jumps", is_hex_mode=False)
    assert index == -1

def test_perform_search_hex_found():
    data = bytearray(b"\x00\x01\x02ABC")
    index = perform_search(data, "41 42 43", is_hex_mode=True)
    assert index == 3  # ASCII 'A' = 0x41, starts at byte 3

def test_perform_search_hex_invalid():
    data = bytearray(b"ABC")
    index = perform_search(data, "ZZ", is_hex_mode=True)
    assert index == -1

def test_find_and_replace_ascii():
    data = bytearray(b"ByteCraft is cool.")
    modified = find_and_replace(data, "cool", "awesome", is_hex_mode=False)
    assert b"awesome" in modified
    assert b"cool" not in modified

def test_find_and_replace_hex():
    data = bytearray(b"\x01\x02\x03\xFF\xFE")
    modified = find_and_replace(data, "ff fe", "aa bb", is_hex_mode=True)
    assert modified[-2:] == bytearray([0xAA, 0xBB])
    assert bytearray([0xFF, 0xFE]) not in modified

def test_find_and_replace_invalid_hex():
    data = bytearray(b"ABC")
    modified = find_and_replace(data, "ZZ", "00", is_hex_mode=True)
    assert modified == data  # unchanged due to parse failure

