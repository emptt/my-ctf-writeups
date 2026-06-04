#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra

result = ((int("VALUE", 16)) ^ int("KEY", 16)) & 0xFFFFFFFFFFFFFFFF
byte_result = result.to_bytes(8, "little")
decode_result = byte_result.decode('ascii', errors='ignore')
print(decode_result)
