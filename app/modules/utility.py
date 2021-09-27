import hashlib
import time

def generate_md5_hash(string: str = str(time.time())) -> str:
    return hashlib.md5(string.encode('UTF-8')).hexdigest()

def generate_sha256_hash(string: str = str(time.time())) -> str:
    return hashlib.sha256(string.encode('UTF-8')).hexdigest()
