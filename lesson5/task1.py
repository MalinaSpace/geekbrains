f_obj = open("text_files/file1.txt","w")

string = " "
print("Enter some text")
while string != "":
    string = input()
    f_obj.write("{0} ".format(string))
