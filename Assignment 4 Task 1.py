try:
    with open("sample.txt", "r") as file:
        for ln, Line in enumerate(file, start=1):
            print(f"Line{ln}: {Line}", end='')
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
