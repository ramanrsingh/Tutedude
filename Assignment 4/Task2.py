with open("output.txt", "wt") as fileObject:
    line1 = input("Enter text to write to the file: ")
    fileObject.write(line1 + "\n")
    print("Data successfully written to output.txt.")

with open("output.txt", "at") as fileObject:
    line2 = input("Enter additional text to append: ")
    fileObject.write(line2 + "\n")
    print("Data successfully appended.")

with open("output.txt", "rt") as fileObject:
    content = fileObject.read()
    print("Final content of output.txt:")
    print(content)

