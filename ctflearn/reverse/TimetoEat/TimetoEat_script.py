def decode(code):
    eat = ""
    eats = ""
    i = 0
    while i < len(code):
        if i%3 == 0:
            eats += code[i] 
        else:
            eat += code[i]
        i += 1

    print(eat, eats)

print("code")
val = input()
decode(val)
