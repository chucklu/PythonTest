data = [["排名", "学校名称", "省市", "类型", "总分","办学层次"],
['1', '清华大学', '北京', '综合', '999.4', '37.6'], 
['2', '北京大学', '北京', '综合', '912.5', '34.4'],
['8', '华中科技大学', '湖北', '综合', '609.3', '32.3']]

# Initialize a list to keep track of the maximum length for each column
max_lengths = [0] * len(data[0])

# Iterate through each list in the data
for row in data:
  # Iterate through each element in the list
  for i, element in enumerate(row):
    # Get the length of the element and multiply it by 2 if it contains Chinese characters
    element_length = len(element) * 2 if any(u'\u4e00' <= c <= u'\u9fff' for c in element) else len(element)
    # Update the maximum length for the corresponding column
    max_lengths[i] = max(max_lengths[i], element_length)

# Print the maximum length for each column
print(max_lengths)