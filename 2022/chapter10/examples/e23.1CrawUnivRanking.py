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
    

def printUnivList(num):
    print('12345678901234567890123456789012345678901234567890123456789012345678901234567890')
    print("{:^2}|{:^15}|{:^2}|{:^2}|{:^6}|{:^4}".format(
        "排名", "学校名称", "省市", "类型", "总分","办学层次"))
    # Iterate over the rows and find the longest value in each column
    max_lengths = [max([value_length(row[i]) for row in allUniv]) for i in range(len(allUniv[0]))]
    for i in range(num):
        u = allUniv[i]
        print("{:^4}|{:^10}|{:^2}|{:^2}|{:^6}|{:^4}".format(
            u[0], u[1], u[2], u[3], u[4],u[5]))


def main():
    url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(10)


main()
