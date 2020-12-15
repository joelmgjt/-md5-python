import hashlib #md5 pyhthon lib
input = input("Enter text: ")   #Input text
cipher = hashlib.md5(input.encode()) #Encode md5
print("Md5 text:",cipher.hexdigest()) #Print result hexdigest