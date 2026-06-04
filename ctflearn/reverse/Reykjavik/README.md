Reykjavik — Reverse Engineering Writeup

Tools

Neovim
Ghidra
Python / pyghidra
Analysis

The binary implements XOR encryption with a hardcoded key:

Flag length = 32 bytes (determined from comparison loop)
XOR key = single byte 0x42 (found in main at instruction xor eax, 0x42)
Encrypted data stored at DAT_00104020
The program:

Reads user input
XORs each character with 0x42
Compares result against encrypted array
Prints flag if match
