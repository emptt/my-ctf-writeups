# eat.py — Reverse Engineering Writeup

## Tools
- Neovim
- Python 3
- Custom decoding script

## Analysis

The file `eat.py` takes an input string `eat` (length 9) and runs it through a chain of functions:
- `aten(eat)`
- `aTE(...)`
- `Ate(...)`
- `eaT(eat)`
- `EAt(..., ...)`

Finally, it compares the result with the hardcoded string:
- `E10a23t9090t9ae0140`

If they match, the flag is printed as `CTFlearn{eaten_ + eat}`.

## The Obfuscation

The transformation is not a simple reversible cipher. It mutates the string by:

- Splitting characters into two streams based on their index
- Swapping or discarding some characters
- Adding metadata (like length info) that is **not** preserved in the final encoded string

## The Key Insight

When decoding back from `E10a23t9090t9ae0140`, one of the original digits — the first one `3` — is completely missing from the encoded form. It is **not** recoverable by purely reversing the character shuffling.

Instead, the missing `3` must be inferred manually. In this case, observing the pattern of the partially decoded string and knowing that the original flag was 9 characters long leads to the conclusion that `3` belongs at the beginning.


## Reversing Process

1. Write a script that redistributes characters from the encoded string into two temporary strings based on index parity (or a fixed pattern).
2. Reassemble the two parts in the correct order.
3. Identify the missing digit by context (length, expected format).
4. Prepend the missing digit to form the original `eat` value.
