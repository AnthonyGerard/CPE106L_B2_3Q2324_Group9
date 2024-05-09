def read_lines_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
 
def main():
    filename = input("Enter the filename: ")
    lines = read_lines_from_file(filename)
 
    if not lines:
        return
 
    print(f"Total number of lines in '{filename}': {len(lines)}")
 
    while True:
        try:
            line_number = int(input("Enter a line number (1 to quit, 0 to quit): "))
            if line_number == 0:
                break
            elif 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print("Invalid line number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid line number.")
 
if __name__ == "__main__":
    main()
