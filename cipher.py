def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)

def main():
    print("=== Caesar Cipher Tool ===")
    mode = input("Choose mode: (1) Encrypt or (2) Decrypt? ")
    text = input("Enter text: ")
    try:
        shift = int(input("Enter shift value (1-25): "))
        is_decrypt = mode == "2"
        output = caesar_cipher(text, shift, decrypt=is_decrypt)
        print(f"Result: {output}")
    except ValueError:
        print("Invalid shift value. Please enter an integer between 1 and 25.")

if __name__ == "__main__":
    main()