#!/usr/bin/python3
import sys

"""A script that reads stdin line by line and computes metrics"""


def main():
    """Programs entry point"""
    file_size = cnt = 0
    status_codes = {}
    valid_status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]

    try:
        for line in sys.stdin:
            if cnt == 10:
                print_metrics(file_size, status_codes)
                cnt = 1
            else:
                cnt += 1
            line = line.strip().split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_status_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise


def print_metrics(file_size, status_codes):
    """Prints the metrics"""
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    main()
