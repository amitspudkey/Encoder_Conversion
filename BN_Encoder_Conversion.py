import io
from selection import *
from file_handling import *


def main():
    print("Program: Encoder Conversion")
    print("Release: 1.0.1")
    print("Date: 2019-12-09")
    print("Author: Brian Neely")
    print()
    print()
    print("This program reads a file and converts from one encoder to another.")
    print()
    print()

    # Open file
    file_in = select_file_in()

    # Open output file
    file_out = select_file_out_csv(file_in)

    # Attempt to auto find encoder?
    if y_n_question("Attempt to auto find encoding (y/n): "):
        encoder_in = encoder_finder(file_in, ",")
    else:
        # Ask for input encoder
        encoder_in = encoding_selection("Select encoding of input file.")

    # Ask for output encoder
    encoder_out = encoding_selection("Select encoding of output file.")

    # Read and write file
    try:
        with io.open(file_in, 'r', encoding=encoder_in) as f:
            text = f.read()
        with io.open(file_out, 'w', encoding=encoder_out) as f:
            f.write(text)

        input("Program Complete, Press [Enter] to continue.")
    except UnicodeEncodeError:
        print("An error has occurred encoding text into " + encoder_out + ". This typically occurs when a character in"
                                                                          "present in the input encoder, but doesn't"
                                                                          "exists in the output encoder.")
        print("Please try again with a different output encoder.")
        input("Press [Enter] to continue.")
    except UnicodeDecodeError:
        print("An error has occurred decoding the input file using" + encoder_in + ".")
        print("Please try again with another input encoder.")
        input("Press [Enter] to continue.")
    except:
        print("An unexpected error has occured.")
        input("Press [Enter] to continue.")


if __name__ == '__main__':
    main()
