myFile = open("my_file.txt", "w")


print(myFile.closed)
print(myFile.mode)
print(myFile.name)

# myFile.write("hello ziay you can do this")
# myFile.close()
mf = open("my_file.txt", "a")
mf.write("hello ziay you can do this")
mf.write("\nand you can make grater than this too")
mf.close()

mf = open("my_file.txt", "r+")

# sen_ay = mf.read(15)
text1 = mf.readlines()
print(text1[0], type(text1))
