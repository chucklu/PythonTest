import requests
from bs4 import BeautifulSoup
allUniv = []


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(r.status_code)
        print(e)
        return ""


def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        singleUniv = []
        for td in ltd:
            str = td.string
            if (str == None):
                a = td.find("a", class_="name-cn")
                if (a == None):
                    # <!-- -->
                    str = td.get_text()
                else:
                    str = a.string

            str = str.replace("\n", "")
            str = str.replace(" ", "")
            singleUniv.append(str)
        allUniv.append(singleUniv)

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

def get_chinese_character_count(my_string):
  # Initialize a counter to 0
  chinese_character_count = 0

  # Iterate through each character in the string
  for character in my_string:
    # Check if the character is a Chinese character and increment the counter if it is
    if any(u'\u4e00' <= c <= u'\u9fff' for c in character):
      chinese_character_count += 1

  # Return the number of Chinese characters
  return chinese_character_count
    
    
def getColumnWidth(value,max_length):
    width = max_length-get_chinese_character_count(value)
    #print(f'{value} width is {width}')
    return width

def get_column_max_lengths(data):
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

  # Return the list of maximum lengths for each column
  return max_lengths


def printUnivList(num):
    print('12345678901234567890123456789012345678901234567890123456789012345678901234567890')
    #print("{:^2}|{:^15}|{:^2}|{:^2}|{:^6}|{:^4}".format(
    #    "排名", "学校名称", "省市", "类型", "总分","办学层次"))
    allUniv.insert(0,["排名", "学校名称", "省市", "类型", "总分","办学层次"])
    # Iterate over the rows and find the longest value in each column
    #print(allUniv)
    max_lengths = get_column_max_lengths(allUniv)
    print(max_lengths)
    print('12345678901234567890123456789012345678901234567890')
    for i in range(num):
        u = allUniv[i]
        len0=getColumnWidth(u[0],max_lengths[0])
        len1=getColumnWidth(u[1],max_lengths[1])
        len2=getColumnWidth(u[2],max_lengths[2])
        len3=getColumnWidth(u[3],max_lengths[3])
        len4=getColumnWidth(u[4],max_lengths[4])
        len5=getColumnWidth(u[5],max_lengths[5])
        print("{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}".format(
        u[0], len0, u[1], len1,
        u[2], len2, u[3], len3,
        u[4], len4, u[5], len5
    ))


def main():
    url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(10)


main()
