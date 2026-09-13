# Module-3

SHA-256.py
- This program calculates 256-bit SHA-256 cryptographic hashes for plain text strings or binary files.
- This will also verifie data integrity by ensuring any altered byte alters the output hash.

Cipher.py
- This program implements a Caesar substitution cipher with configurable shifts for encryption and decryption.
- This will demonstrate classic symmetric character substitution mechanics.

OpenSSL.py
- This program uses PBKDF2 salted password hashing (showing the impact of randomness/entropy on security). It has role-based checks restrict signing capabilities exclusively to administrative users.
- This also uses OpenSSL RSA 2048-bit key pairs with standard PSS padding to sign messages via private key and publicly verify them with the public key.
