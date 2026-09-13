import hashlib
import sys

def sha256_hash(text: str) -> str:
    """Generate SHA-256 hash for plain text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def sha256_file(file_path: str) -> str:
    """Generate SHA-256 hash for a file, reading in blocks."""
    sha = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha.update(block)
    return sha.hexdigest()

def main():
    print("=== SHA-256 Integrity Verification Tool ===")
    choice = input("Hash (1) Text String or (2) File Path? ")

    if choice == "1":
        text = input("Enter Text: ")
        print(f"SHA-256 Hash: {sha256_hash(text)}")
    elif choice == "2":
        path = input("Enter File Path: ")
        try:
            print(f"File SHA-256 Hash: {sha256_file(path)}")
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
2
