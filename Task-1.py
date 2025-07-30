try:
    with open("sample.txt", 'r') as f1:
        line1 = f1.readline().strip()
        line2 = f1.readline().strip()
        print(f"Line 1: {line1}")
        print(f"Line 2: {line2}")
except FileNotFoundError:
    print(f"Error: The file {'sample.txt'} was not found.")