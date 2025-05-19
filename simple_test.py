"""
Simple test script to scan for encoded strings in a binary file.
"""
import base64
import re
import binascii
from pathlib import Path

def printable_ratio(bs):
    """Return ratio of printable ASCII characters."""
    return sum(32 <= b <= 126 for b in bs) / len(bs) if bs else 0

def scan_file(path):
    """Scan a file for encoded strings."""
    results = []
    
    # Load the file
    with open(path, 'rb') as f:
        content = f.read()
    
    # Look for base64
    base64_pattern = rb'(?:[A-Za-z0-9+/]{4}\s*){3,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
    for match in re.finditer(base64_pattern, content):
        try:
            raw = b''.join(match.group(0).split())  # Remove whitespace
            decoded = base64.b64decode(raw)
            if printable_ratio(decoded) > 0.8:
                results.append({
                    'offset': match.start(),
                    'codec': 'base64',
                    'text': decoded.decode(errors='ignore'),
                    'score': 0.9
                })
        except Exception:
            pass
    
    # Look for hex encoded
    hex_pattern = rb'(?:[0-9A-Fa-f]{2}\s*){4,}'
    for match in re.finditer(hex_pattern, content):
        try:
            raw = b''.join(match.group(0).split())  # Remove whitespace
            decoded = binascii.unhexlify(raw)
            if printable_ratio(decoded) > 0.8:
                results.append({
                    'offset': match.start(),
                    'codec': 'hex',
                    'text': decoded.decode(errors='ignore'),
                    'score': 0.7
                })
        except Exception:
            pass
    
    # Look for URL encoded
    url_pattern = rb'(?:%[0-9A-Fa-f]{2}){2,}'
    for match in re.finditer(url_pattern, content):
        try:
            raw = match.group(0)
            # Simple URL decoding
            decoded = bytes([
                int(raw[i+1:i+3], 16) for i in range(0, len(raw), 3) if i+2 < len(raw)
            ])
            if printable_ratio(decoded) > 0.8:
                results.append({
                    'offset': match.start(),
                    'codec': 'url',
                    'text': decoded.decode(errors='ignore'),
                    'score': 0.8
                })
        except Exception:
            pass
    
    # Sort by score and offset
    results.sort(key=lambda x: (-x['score'], x['offset']))
    return results

if __name__ == "__main__":
    results = scan_file("sample.bin")
    
    if not results:
        print("No encoded strings found!")
    else:
        print(f"Found {len(results)} encoded strings:")
        for result in results:
            print(f"{result['offset']:08x} [{result['codec']}] {result['text']!r}")
            
    print("Done!") 