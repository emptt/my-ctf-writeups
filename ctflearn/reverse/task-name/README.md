# Ramada — Reverse Engineering Writeup

## Tools
- Neovim
- Ghidra
- Python / PyGhidra

## Analysis

The binary checks:
- Flag length = `0x1f` (31 chars)
- Last character = `}` (ASCII `0x7d`)

The author obfuscated the flag by splitting it into 5 separate data blocks.  
`InitData()` copies these blocks into one array.

Each value in the array is a 32-bit integer.  
Every integer is the cube of a character's ASCII value.

## Solution

Extract integers from `0x00102170`, take cube root, convert to chars.
