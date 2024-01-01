import sys

# https://codeforces.com/problemset/problem/1902/A

def main(input_stream):
    input = input_stream.readline

    # Retrieve the expected number of testcases
    nbcases = int(input())

    for _ in range(nbcases):
        # For each test case, the first input is the size of the binary string.
        # We don't need that.
        _ = input()
        binary_string = input()

        # If the string only contains "0", obviously we have more "0"s than "1"s.
        # If there is at least a "0" inside the string, we are sure to find
        # at least one "01" or "10" substring.
        # So it will be possible to add as much "0"s as needed in front or after the "1".
        if '0' in binary_string:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main(sys.stdin)
