from matplotlib import pyplot as plt
import sys
import math


def split_text(clear_text):
    """ Splits the cleartext into two parts. Either two distinct words if there are, or on word in two halfs."""
    if len(clear_text) == 1:
        half = math.trunc(len(clear_text[0])/2)
        y = clear_text[0][:half]
        x = clear_text[0][half:]
    else:
        y = clear_text[0]
        x = clear_text[1]
    return y, x


def add_pre_zeros(binary_in):
    """ Fits the binary numbers into 8-bit shape of ASCII-characters by adding 0 in front."""
    return '0'*(8-len(binary_in))+binary_in


def create_pattern(clear_text):
    """ Generates the pattern and plots it. """
    text_y, text_x = split_text(clear_text)
    # getting binary values for the side
    binary_y = ''.join([add_pre_zeros(bin(ord(char))[2:]) for char in text_y])
    # getting binary values for the top
    binary_x = ''.join([add_pre_zeros(bin(ord(char))[2:]) for char in text_x])

    binary_pattern = []
    current_value = 1   # keeps track of the first value of the last row to apply changes in y-axis
    # goes through binary_y in reverse, because it is written from the bottom up
    for y in range(len(binary_y), -1, -1):

        # calculating the next row
        row = [current_value]
        for x in range(len(binary_x)):
            # if there is a line, it changes value, otherwise it keeps the one  from before
            # '%2' alternates between value 0 and 1 having a line
            if y % 2 == int(binary_x[x]):
                row.append(row[x])
            else:
                row.append(abs(row[x]-1))
        binary_pattern.append(row)
        if y != 0:
            current_value = abs(row[0]-int(binary_y[y-1]))

    # plotting the pattern with the colours white and red
    plt.imshow(binary_pattern, cmap='Reds')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()


def main() -> None:
    if len(sys.argv) < 2:
        raise Exception("No text to convert.")
    elif len(sys.argv) > 3:
        raise Exception("This program can only create patterns from a maximum of two words.")
    clear_text = [sys.argv[i] for i in range(1, len(sys.argv))]
    create_pattern(clear_text)
    print("All done!")


if __name__ == '__main__':
    main()
