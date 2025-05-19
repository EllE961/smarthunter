import base64
import tempfile
import os

def test_with_sample():
    # Create a sample binary file with a base64 encoded flag
    sample_flag = b"flag{test_smarthunter_works}"
    encoded_flag = base64.b64encode(sample_flag)
    
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(encoded_flag)
        temp_path = temp.name
    
    # Run the command to test
    cmd = f"pip install -e . && smarthunter hunt {temp_path}"
    print(f"Running: {cmd}")
    try:
        os.system(cmd)
    finally:
        os.unlink(temp_path)

if __name__ == "__main__":
    test_with_sample() 