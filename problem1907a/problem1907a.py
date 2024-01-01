import sys

# https://codeforces.com/problemset/problem/1907/A

# Build the codeset lists for the possible letters and numbers in positions
ALL_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ALL_NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8']

def main(input_stream):
    input = input_stream.readline

    # Retrieve the expected number of testcases
    nbcases = int(input())

    for _ in range(nbcases):
        # Retrieve the rook current position
        rook_pos = input()

        letter = rook_pos[0]
        number = rook_pos[1]

        # Output squares within the same column as the current position
        squares_col = [letter + x for x in ALL_NUMBERS if x != number]
        # Output squares within the same row as the current position
        squares_row = [x + number for x in ALL_LETTERS if x != letter]

        # Print response
        print('\n'.join(squares_col + squares_row))


if __name__ == "__main__":
    main(sys.stdin)
