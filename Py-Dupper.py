import random
import string
import subprocess

def main():
    # Generate a random filename
    output_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ".py"

    # Open the current file for reading
    with open(__file__, "r") as input_file:
        # Read the entire contents of the file into a string
        input_contents = input_file.read()

    # Open the output file for writing
    with open(output_filename, "w") as output_file:
        # Write the contents of the input file to the output file
        output_file.write(input_contents)

    # Run the output file using the Python interpreter
    subprocess.run(["python", output_filename])

if __name__ == "__main__":
    main()
