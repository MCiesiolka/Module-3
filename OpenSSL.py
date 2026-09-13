import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Role-Based Access Control (RBAC) User Storage
# Demonstrates outcome 3.1: Passwords hashed with PBKDF2 and random salts
USERS = {
    "admin": (hashlib.pbkdf2_hmac('sha256', b'admin123', b'random_salt_123', 100000), "admin"),
    "user":  (hashlib.pbkdf2_hmac('sha256', b'user123',  b'random_salt_456', 100000), "user")
}

def login():
    print("=== System Authentication ===")
    u = input("Username: ")
    p = input("Password: ")
    salt = b'random_salt_123' if u == 'admin' else b'random_salt_456'
    
    user_data = USERS.get(u)
    if user_data and hashlib.pbkdf2_hmac('sha256', p.encode(), salt, 100000) == user_data[0]:
        print(f"[+] Authenticated as [{user_data[1].upper()}]\n")
        return user_data[1]
    
    print("[!] Access Denied: Invalid credentials.")
    return None

def main():
    role = login()
    if not role:
        return

    # Generate RSA 2048-bit key pair (OpenSSL abstraction)
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    signature = None
    signed_data = None

    while True:
        print("--- Digital Signature Tool ---")
        print("1. Sign Message (Admin Only)")
        print("2. Verify Signature (All Roles)")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            if role != "admin":
                print("[!] ACCESS DENIED: Only 'admin' role can sign messages.\n")
                continue
            signed_data = input("Enter message to sign: ").encode()
            signature = private_key.sign(
                signed_data,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
            print(f"[+] Message signed successfully!\nHex Signature: {signature.hex()[:32]}...\n")

        elif choice == "2":
            if not signature:
                print("[!] No active signature found. Sign a message first.\n")
                continue
            test_data = input("Enter message to verify: ").encode()
            try:
                public_key.verify(
                    signature,
                    test_data,
                    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                    hashes.SHA256()
                )
                print("[+] VERIFIED: Signature matches payload integrity.\n")
            except InvalidSignature:
                print("[!] INVALID: Message altered or signature mismatched.\n")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()