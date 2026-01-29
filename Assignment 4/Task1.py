try:
    with open('sample.txt', 'rt') as fileObject:
        line1 = fileObject.readline()
        line2 = fileObject.readline()

        print("Reading file content:")
        print(f"Line 1 : {line1}")
        print(f"Line 2 : {line2}")

except FileNotFoundError:
    print("The file 'sample.txt' was not found")