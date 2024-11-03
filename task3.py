import sys
import re
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    """Парсить рядок лоґу і повертає словник з компонентами."""
    parts = line.split(" ", 3)  # Розділяємо на дату, час, рівень і повідомлення
    if len(parts) < 4:
        return None  # Якщо рядок не має достатньо частин, повертаємо None
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> list:
    """Завантажує лоґи з файлу."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує лоґи за рівнем лоґування."""
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """Підраховує записи за рівнем лоґування."""
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

def display_log_counts(counts: dict):
    """Виводить результати підрахунку в читабельній формі."""
    print("Рівень лоґування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях до файлу лоґів> [рівень лоґування]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДеталі лоґів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"Немає записів для рівня '{level.upper()}'.")

if __name__ == "__main__":
    main()