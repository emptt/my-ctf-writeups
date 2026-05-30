# Raspberry — Reverse Engineering Writeup

## Tools
- Neovim
- Ghidra
- Python / PyGhidra

## Analysis

The binary stores an obfuscated flag. The stored bytes are not the actual flag — they are transformed.

### The Obfuscation

Each flag character is XORed with a constant before being stored:

`stored[i] = real_flag[i] ^ constant`

### Finding the Constant

The flag starts with `CTFLearn{`. By XORing the first stored byte with `'C'`, I recover the constant.

### Reversing

Applying XOR with the constant to every stored byte recovers the flag.
