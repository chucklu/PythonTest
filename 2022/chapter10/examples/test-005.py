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
rows =[['1', '清华大学', '北京', '综合', '999.4', '37.6'], ['2', '北京大学', '北京', '综合', '912.5', '34.4'], ['3', '浙江大学', '浙江', '综合', '825.3', '34.1'], ['4', '上海交通大学', '上海', '综合', '783.3', '35.5'], ['5', '复旦大学', '上海', '综合', '697.8', '35.9'], ['6', '南京大学', '江苏', '综合', '683.4', '37.7'], ['7', '中国科学技术大学', '安徽', '理工', '609.9', '40.0'], ['8', '华中科技大学', '湖北', '综合', '609.3', '32.3'], ['9', '武汉大学', '湖北', '综合', '607.1', '32.8'], ['10', '西安交通大学', '陕西', '综合', '570.2', '34.2'], ['11', '四川大学', '四川', '综合', '561.7', '32.0'], ['12', '中山大学', '广东', '综合', '559.4', '31.4'], ['13', '哈尔滨工业大学', '黑龙江', '理工', '549.8', '32.7'], ['14', '同济大学', '上海', '理工', '548.4', '32.8']]

# Iterate over the rows and find the longest value in each column
max_lengths = [max([value_length(row[i]) for row in rows]) for i in range(len(rows[0]))]
print(max_lengths)

# Iterate over the rows and print them with the correct field lengths
for row in rows:
    print("{:{}}|{:{}}|{:{}}|{:{}}|{:{}}|{:{}}".format(
        row[0], max_lengths[0], row[1], max_lengths[1],
        row[2], max_lengths[2], row[3], max_lengths[3],
        row[4], max_lengths[4], row[5], max_lengths[5]
    ))