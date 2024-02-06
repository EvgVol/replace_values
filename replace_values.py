import sys


def read_config(config_file):
    config_pairs = {}
    with open(config_file, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            config_pairs[key] = value
    return config_pairs


def process_text(text_file, config_pairs):
    modified_lines = []
    with open(text_file, 'r') as f:
        for line in f:
            symbols_replaced = 0
            modified_line = line
            for key, value in config_pairs.items():
                count = modified_line.count(key)
                modified_line = modified_line.replace(key, value)
                symbols_replaced += count * len(value)
            modified_lines.append((modified_line, symbols_replaced))
    return modified_lines


def sort_lines(modified_lines):
    sorted_lines = sorted(modified_lines, key=lambda x: x[1], reverse=True)
    return sorted_lines


def main(config, text):
    config_pairs = read_config(config)
    modified_lines = process_text(text, config_pairs)
    sorted_lines = sort_lines(modified_lines)
    
    for line, _ in sorted_lines:
        print(line)


if __name__=='__main__':
    main(sys.argv[1], sys.argv[2])
