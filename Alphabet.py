import re

# Define the mapping of letters
letter_map = {
    'A': '一', 'B': '二', 'C': '三', 'D': '四', 'E': '五',
    'F': '六', 'G': '七', 'H': '八', 'I': '九', 'J': '十',
    'K': '口', 'L': '目', 'M': '耳', 'N': '手', 'O': '足',
    'P': '木', 'Q': '山', 'R': '川', 'S': '田', 'T': '日',
    'U': '月', 'V': '火', 'W': '水', 'X': '金', 'Y': '土', 'Z': '人'
}

def transform_string(input_string):
    # Transform each letter in the string
    transformed = ''.join(letter_map.get(char, char) for char in input_string.upper())
    return transformed

def replace_outside_tags(text):
    if '<' not in text and '>' not in text:
        return transform_string(text)
    
    def replace(match):
        return transform_string(match.group(1))
    
    # This regex finds text outside of HTML tags
    pattern = re.compile(r'>([^<]+)<')
    return pattern.sub(lambda m: '>' + replace(m) + '<', text)

# Get multi-line input from the user
print("Enter a string to transform (end with an empty line):")
input_lines = []
while True:
    line = input()
    if line == "":
        break
    input_lines.append(line)

input_text = "\n".join(input_lines)
transformed_text = replace_outside_tags(input_text)
print("Transformed text:")
print(transformed_text)
