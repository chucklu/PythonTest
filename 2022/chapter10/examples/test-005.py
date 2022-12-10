# Define a function to calculate the length of a value
def value_length(value):
    # If the value is a string, calculate the number of characters in the string
    if isinstance(value, str):
        # Count the number of Chinese characters in the string and multiply by 2
        return len([c for c in value if '\u4e00' <= c <= '\u9fff']) * 2
    # If the value is an integer or floating-point number, convert it to a string and return the length
    elif isinstance(value, (int, float)):
        return len(str(value))
    # Otherwise, return the length of the value
    return len(value)

# Create a list of lists containing the values in each row of the table
rows = [
    [1, "清华大学", "北京", "综合", 999.4, 37.6],
    [2, "北京大学", "上海", "理工", 500.0, 24.8],
    [3, "南京大学", "广州", "师范", 200.0, 12.4],
    [4, "复旦大学", "深圳", "农林", 100.0, 6.2]
]

# Iterate over the rows and find the longest value in each column
max_lengths = [max([value_length(row[i]) for row in rows]) for i in range(len(rows[0]))]

# Print the maximum lengths of each column as a list
print(max_lengths)