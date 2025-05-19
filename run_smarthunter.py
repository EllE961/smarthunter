import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.smarthunter.cli import app
from src.smarthunter.core import scan

# Run directly
if __name__ == "__main__":
    # Process the sample.bin file directly
    sample_path = "sample.bin"
    
    print(f"Scanning {sample_path}...")
    hits = list(scan(sample_path, minlen=4, maxlen=120))
    hits.sort(key=lambda h: (-h.score, h.offset))
    
    if not hits:
        print("No hits found!")
    else:
        print(f"Found {len(hits)} hits:")
        for h in hits:
            print(f"{h.offset:08x} [{h.codec}] {h.text!r}")
    
    print("Done!") 