import hashlib as hl
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """ Hash pada Block. Renturn string representation of it 
    
    Arguments: 
        :block: The block that should be hashed
    """
    # pakai SHA256 buat bkin hash | .hexdigest --> ngubah data hash (byte) jadi string
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
