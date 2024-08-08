import sys
import re
from collections import defaultdict


def parse_log_line(line):
    pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) ([A-Z]+) (.*)$'
    match = re.match(pattern, line)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    return None


def load_logs(file_path):
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs, level):
    return list(filter(lambda log_line: log_line['level'] == level, logs))


def count_logs_by_level(logs):
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts


def display_log_counts(counts):
    keys = [counts.keys(), 'Рівень логування']
    max_level_len = max(len(level) for level in keys)
    print(f"{'Рівень логування':<{max_level_len}} | Кількість")
    print('-' * (max_level_len + 12))
    for level, count in counts.items():
        print(f"{level:<{max_level_len}} | {count}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [optional_level]")
        sys.exit(1)

    log_file = sys.argv[1]
    logs = load_logs(log_file)

    if len(sys.argv) == 3:
        level_to_filter = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level_to_filter)
        filtered_counts = count_logs_by_level(filtered_logs)

        print("\nЗагальна статистика:")
        display_log_counts(count_logs_by_level(logs))

        print(f"\nДеталі логів для рівня '{level_to_filter}':")
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
