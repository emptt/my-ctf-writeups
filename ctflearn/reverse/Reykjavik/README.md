# Reykjavik — Reverse Engineering Writeup

## Tools
- Neovim
- Ghidra
- Python / PyGhidra

## Analysis

The binary stores an obfuscated flag using **XOR encryption** with a hardcoded single-byte key.

### The Obfuscation

Each flag character is XORed with a constant before being stored:

`stored[i] = real_flag[i] ^ key`

### Finding the Key

From Ghidra, the XOR instruction in the comparison loop uses `0x42`. This is the key.

**XOR Key:** `0x42`

### Reversing

Applying XOR with `0x42` to every stored byte recovers the flag.
