#!/usr/bin/env python3
"""Write test_sample.bin: a few short messages, each in a different encoding,
so `smarthunter test_sample.bin` has something to find. Used for the README image."""
import base64, binascii, pathlib

def region(tok: bytes) -> bytes:
    # 0xff/0x00 around each token so the regex passes don't run them together
    return b"\xff\x00" + tok + b"\x00\xff\n"

blob = b""
blob += region(base64.b64encode(b"flag{h1dd3n_1n_pl41n_s1ght}"))   # base64
blob += region(base64.b32encode(b"CTF{d3c0d3_m3_1f_y0u_c4n}"))     # base32
blob += region(b"%66%6c%61%67%7b%75%72%6c%5f%65%6e%63%6f%64%65%64%7d")  # url -> flag{url_encoded}
blob += region(binascii.hexlify(b"secret_key_found_in_binary"))    # hex
blob += region(base64.a85encode(b"api_token=demo_not_a_real_key")) # base85
blob += b"\xff\x00build=release channel=stable user=root\x00\xff\n" # cleartext

out = pathlib.Path(__file__).resolve().parent.parent / "test_sample.bin"
out.write_bytes(blob)
print(f"wrote {out} ({len(blob)} bytes)")
