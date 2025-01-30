import emoji

name = input("Input: ")
output = emoji.emojize(name,language="alias")
print("Output: ",output)
