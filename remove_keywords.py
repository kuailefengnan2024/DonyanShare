
import os

def remove_keywords():
    file_path = r"d:\DonyanShare\标杆样本库.txt"
    keywords = ["bijie", "jinsha"]
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Read all lines
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Filter lines
    new_lines = []
    removed_count = 0
    
    for line in lines:
        # Check if any keyword is present in the line (case insensitive)
        line_lower = line.lower()
        if any(keyword.lower() in line_lower for keyword in keywords):
            removed_count += 1
        else:
            new_lines.append(line)

    # Write back to file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Successfully processed file.")
        print(f"Total lines: {len(lines)}")
        print(f"Removed lines: {removed_count}")
        print(f"Remaining lines: {len(new_lines)}")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    remove_keywords()
