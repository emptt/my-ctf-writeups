# @runtime PyGhidra

def run():
    base = currentProgram.getImageBase().add(0x2170)
    flag = ""
    
    for i in range(20):
        val = currentProgram.getMemory().getInt(base.add(i * 4))
        flag += chr(int(round(val ** (1.0 / 3.0))))
    
    print("CTFLearn{" + flag + "}")

run()
