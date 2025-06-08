"""Test hex_formatter module."""

from core.hex_formatter import format_hex_view, decode_ascii

def test_format_hex_view_basic():
    data = bytearray(b"ABCDEF")
    output = format_hex_view(data)

    assert "41 42 43 44 45 46" in output  # hex for ABCDEF
    assert "|ABCDEF|" in output          # ASCII output

def test_format_hex_view_spacing():
    data = bytearray(range(32))  # ensure at least 2 rows
    output = format_hex_view(data)

    lines = output.splitlines()
    assert len(lines) >= 2
    assert all(":" in line and "|" in line for line in lines)

def test_decode_ascii_valid():
    data = bytearray(b"Hello World!")
    result = decode_ascii(data)
    assert result == "Hello World!"

def test_decode_ascii_invalid():
    data = bytearray([0x80, 0x81, 0x82])  # invalid ASCII
    result = decode_ascii(data)
    assert "�" in result or "." in result  # fallback decoding

