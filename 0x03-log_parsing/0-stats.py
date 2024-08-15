#!/usr/bin/env python3
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Check if the line has the correct format
        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Accumulate the total file size
            total_size += file_size

            # Count the status codes if they are one of the expected ones
            if status_code in status_codes:
                status_codes[status_code] += 1

        except ValueError:
            continue  # Skip lines where file_size or status_code is not an integer

        # Print the stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
