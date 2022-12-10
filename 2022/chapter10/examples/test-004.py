rows = [    [" 排名", " 学校名称", " 省市", " 类型", " 总分", " 办学层次"],
    [" 1", " 清华大学", " 北京", " 综合", " 999.4", " 37.6"],
    [" 2", " 北京大学", " 北京", " 综合", " 912.5", " 34.4"],
    [" 3", " 浙江大学", " 浙江", "综合", " 825.3", " 34.1"],
[" 4", " 上海交通大学", " 上海", " 综合", " 783.3", " 35.5"],
[" 5", " 复旦大学", " 上海", " 综合", " 697.8", " 35.9"],
[" 6", " 南京大学", " 江苏", " 综合", " 683.4", " 37.7"],
[" 7", " 中国科学技术大学", " 安徽", " 理工", " 609.9", " 40.0"],
[" 8", " 华中科技大学", " 湖北", " 综合", " 609.3", " 32.3"],
[" 9", " 武汉大学", " 湖北", " 综合", " 607.1", " 32.8"],
[" 10", " 西安交通大学", " 陕西", " 综合", " 570.2", " 34.2"],
]

print("12345678901234567890")
print("{:^4}".format("排名"))
print("{:^4}".format("1"))

print("12345678901234567890")
print("{:^5}".format("排名"))
print("{:^5}".format("1"))

print("123456789012345678901")
#print("学校名称")#占8个字符
#print("中国科学技术大学")#占16个字符
print("{:^16}|".format("学校名称"))#(16-4)/2，前面6个字符，后面6个字符，文字本身占有4个字符。总长度20个字符
print("{:^16}|".format("清华大学"))
print("{:^12}|".format("中国科学技术大学"))#(20-16)/2=2，所以前面2个字符，后面2个字符。文字本身占有16个字符。

print("123456789012345678901")
print("{:^14}|".format("学校名称"))#(18-4*2)+4=14个字符
print("{:^14}|".format("清华大学"))
print("{:^10}|".format("中国科学技术大学"))#文字本身占有8*2=16个字符，前面一个字符，后面一个字符，总长度是18个字符。8+2=10

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
    
# Iterate over the rows and find the longest value in each column
max_lengths = [max([value_length(row[i]) for row in rows]) for i in range(len(rows[0]))]

# Print the maximum lengths of each column as a list
print(max_lengths)