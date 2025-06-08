"""Module: search_engine"""

def perform_search(data: bytearray, query: str, is_hex_mode: bool) -> int:
    """Search for query in data. Returns index or -1."""
    try:
        if is_hex_mode:
            query_bytes = bytearray.fromhex(query.replace(" ", ""))
        else:
            query_bytes = query.encode()
    except ValueError:
        return -1

    return data.find(query_bytes)

def find_and_replace(data: bytearray, find_str: str, replace_str: str, is_hex_mode: bool) -> bytearray:
    """Find and replace all matches of find_str with replace_str in the data."""
    try:
        find_bytes = bytearray.fromhex(find_str.replace(" ", "")) if is_hex_mode else find_str.encode()
        replace_bytes = bytearray.fromhex(replace_str.replace(" ", "")) if is_hex_mode else replace_str.encode()
    except ValueError:
        return data

    return data.replace(find_bytes, replace_bytes)

