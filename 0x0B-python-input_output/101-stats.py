#!/usr/bin/python3

import sys


def print_metrics(metrics):
    """Print the computed metrics."""
    print("File size: {}".format(metrics['total_size']))
    for code in sorted(metrics['status_codes']):
        count = metrics['status_codes'][code]
        print("{}: {}".format(code, count))


def parse_line(line):
    """Parse a line in the specified input format."""
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        size = int(parts[-1])
        return status_code, size
    return None, 0


def main():
    metrics = {'total_size': 0, 'status_codes': {}}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, size = parse_line(line)
            if status_code:
                metrics['total_size'] += size
                if status_code in metrics['status_codes']:
                    metrics['status_codes'][status_code] += 1
                else:
                    metrics['status_codes'][status_code] = 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics(metrics)

    except KeyboardInterrupt:
        print_metrics(metrics)


if __name__ == '__main__':
    main()
