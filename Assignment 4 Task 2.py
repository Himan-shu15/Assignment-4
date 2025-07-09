newdata = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(newdata + "\n")

newdata = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(newdata + "\n")

print("\nFinal content of output.txt:")
try:
    with open("output.txt", "r") as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
