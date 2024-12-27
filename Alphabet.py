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

# Get input from the user
input_text = input("Enter a string to transform: ")
transformed_text = transform_string(input_text)

# Display the transformed text
print("Transformed string:", transformed_text)
