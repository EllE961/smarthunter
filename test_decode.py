from smarthunter.main import decode_string

def test_url_decode():
    input_str = "%66%6c%61%67%7b%68%69%64%64%65%6e%5f%69%6e%5f%75%72%6c%5f%65%6e%63%6f%64%69%6e%67%7d"
    results = decode_string(input_str)
    for result in results:
        print(f"[{result['codec']}] (score: {result['score']:.2f}) {result['text']}")

def test_hex_decode():
    input_str = "73 65 63 72 65 74 5f 6d 65 73 73 61 67 65 5f 69 6e 5f 68 65 78 5f 66 6f 72 6d 61 74"
    results = decode_string(input_str)
    for result in results:
        print(f"[{result['codec']}] (score: {result['score']:.2f}) {result['text']}")

def test_base64_decode():
    input_str = "ZmxhZ3t0aGlzX2lzX2FfdGVzdF9iYXNlNjRfZmxhZ30="
    results = decode_string(input_str)
    for result in results:
        print(f"[{result['codec']}] (score: {result['score']:.2f}) {result['text']}")

if __name__ == "__main__":
    print("Testing URL decode:")
    test_url_decode()
    
    print("\nTesting HEX decode:")
    test_hex_decode()
    
    print("\nTesting Base64 decode:")
    test_base64_decode() 