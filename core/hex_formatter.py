"""Module: hex_formatter"""

def format_hex_view(data: bytearray) -> str:
    """Format binary data into a structured hex + ASCII view."""
    lines = []
    for i in range(0, len(data), 16):
        offset = f"{i:08x}:"

        hex_chunk = ' '.join(f"{b:02x}" for b in data[i:i+16])
        hex_chunk = hex_chunk.ljust(48)  # ensure spacing

        ascii_chunk = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in data[i:i+16])

        line = f"{offset} {hex_chunk}  |{ascii_chunk}|"
        lines.append(line)
    return '\n'.join(lines)

def decode_ascii(data: bytearray) -> str:
    """Decode binary data to ASCII, replacing undecodable chars."""
    try:
        return data.decode('ascii')
    except UnicodeDecodeError:
        return data.decode('ascii', errors='replace')

