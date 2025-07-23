# file = open("textfile.txt")
#
# content = file.read()
# print(content)
# file.close()

with open("textfile.txt",mode="r") as f:
    text = f.read()
    print(text)

with open("textfile.txt",mode="a") as f: # w: write, a: append
    # text = f.read()
    # print(text)

    f.write("\nThis is a code added line")



