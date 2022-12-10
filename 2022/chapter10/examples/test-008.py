# Import the BeautifulSoup4 library
from bs4 import BeautifulSoup

# Read the file content
# parse the HTML file using BeautifulSoup
with open("university.html", encoding='utf-8') as f:
    soup = BeautifulSoup(f, "html.parser")

# find all <li> elements
li_elements = soup.find_all('li')

# initialize the list that will hold the extracted information
university_list = []
# find all <li> elements with class "item-list__ListItemStyled-sc-18yjqdy-1 boZDDO"
for li in soup.find_all("li", class_="item-list__ListItemStyled-sc-18yjqdy-1 boZDDO"):
    # find the <a> element with class "Anchor-byh49a-0 Card__StyledAnchor-sc-1ra20i5-8 PlBer kijIJB card-name"
    # that is under a <h3> element, and the <h3> element is under the current <li> element
    a = li.find("h3").find("a", class_="Anchor-byh49a-0 Card__StyledAnchor-sc-1ra20i5-8 PlBer kijIJB card-name")

    # find the <div> element with class "RankList__Rank-sc-2xewen-2 fxzjOx ranked has-badge"
    # that is under the current <li> element
    div = li.find("div", class_="RankList__Rank-sc-2xewen-2 fxzjOx ranked has-badge")

    # find all <dd> elements with class "QuickStatHug__Description-hb1bl8-1 eXguFl"
    # that are under the current <li> element
    dds = li.find_all("dd", class_="QuickStatHug__Description-hb1bl8-1 eXguFl")

    # extract the rank, university name, tuition and fees, and undergraduate enrollment
    # by accessing the text of the corresponding elements
    rank = div.strong.text.replace("#", "")
    university = a.text
    tuition_and_fees = dds[0].text.replace("\n", "")
    undergraduate_enrollment = dds[1].text.replace("\n", "")

    # append the data as a tuple to the university_list
    university_list.append((rank, university, tuition_and_fees, undergraduate_enrollment))

# print the university_list
print(university_list)