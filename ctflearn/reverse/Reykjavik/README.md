# Reykjavik — Reverse Engineering Writeup

## Tools
- Neovim
- Ghidra
- Python / PyGhidra

## Analysis

The binary stores an obfuscated flag using **XOR encryption** with a hardcoded key.

### The Obfuscation

Each flag character is XORed with a constant before being stored:

`stored[i] = real_flag[i] ^ key`

### Finding the Key

From Ghidra, the XOR instruction in the comparison loop reveals the key. The key is a single byte.

### Reversing

Applying XOR with the key to every stored byte recovers the flag.
