# Original author: Yukio Nozawa (GitHub: @yncat)
# MIT license
# A script to handle hearthstone translation files
# Merges the new keys to existing key.
# format: key, text, description. Separated by a tab.
# Usage: merge.py existing_file new_file
# Directly updates existing_file with merged result.
# Writes untranslated lines into stdout

import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: merge.py existing_file new_file")
        return
    existing_file = sys.argv[1]
    new_file = sys.argv[2]
    with open(existing_file, 'r', encoding='utf-8') as f:
        existing = f.readlines()
    with open(new_file, 'r', encoding='utf-8') as f:
        new = f.readlines()
    # extract keys from existing, as a dictionary of key:line
    existing_keys = {}
    for line in existing:
        if line == "":
            continue
        key = line.split('\t')[0]
        existing_keys[key] = line
    merged_lines = []
    for line in new:
        if line == "":
            merged_lines.append(line)
        key = line.split('\t')[0]
        if key in existing_keys:
            merged_lines.append(existing_keys[key])
        else:
            merged_lines.append(line)
            print(line)
    with open(existing_file, 'w', encoding='utf-8') as f:
        f.writelines(merged_lines)


if __name__ == '__main__':
    main()
