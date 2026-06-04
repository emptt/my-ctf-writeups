# Reykjavik — Reverse Engineering Writeup

## Tools
- Neovim
- Ghidra
- Python / PyGhidra

## Analysis

The binary stores an obfuscated flag using **XOR encryption** with a hardcoded multi-byte key.

### The Obfuscation

The encrypted flag is XORed with a repeating key. The decryption is applied to the entire block at once, not character by character.

### Reversing

Applying XOR with the key to the encrypted data recovers the full flag.
