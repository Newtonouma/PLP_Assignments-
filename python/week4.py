def read_and_modify_file(input_filename, output_filename):
    try:
        infile = open(input_filename, 'r')
        content = infile.read()
        modified_content = content.upper()
        infile.close()

        outfile = open(output_filename, 'w')
        outfile.write(modified_content)
        outfile.close()

        print(f"File has been successfully modified and saved as '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    
    except IOError:
        print(f"Error: There was an issue with reading or writing the file.")

def main():
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the new file to save the modified content: ")
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
