assignment4_file = open("sample.txt", 'wt')
assignment4_file.write("Reading file content: ")
assignment4_file.write("\nLine 1 : This is a sample text line.\n")
assignment4_file.write("Line 2 : It contains multiple lines.")
assignment4_file.close()


#Reading file contents
assignment4_file = open("sample.txt", 'rt')
content = assignment4_file.readlines()
for line in content:
    print(line.rstrip('\n'))
assignment4_file.close()

# handling errors gracefully
try:
    with open("sample.txt",'rt') as fh:
        data = fh.read()
    print("Sample.txt file exists.")
except FileNotFoundError:
    print(f"Error: The file you are looking for does not exist")



