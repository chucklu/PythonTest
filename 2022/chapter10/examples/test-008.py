# Import the BeautifulSoup4 library
from bs4 import BeautifulSoup

# Read the file content
# parse the HTML file using BeautifulSoup
with open("university.html", encoding='utf-8') as f:
    soup = BeautifulSoup(f, "html.parser")

# Find all the <li> elements that contain the information we want to extract
li_elements = soup.find_all("li", class_="item-list__ListItemStyled-sc-18yjqdy-1 boZDDO")

# initialize the list that will hold the extracted information
university_list = []

# Create an empty list to store the extracted data
university_list = []

# Find all the <li> elements in the HTML
li_elements = soup.find_all("li", class_="item-list__ListItemStyled-sc-18yjqdy-1 boZDDO")

# Loop through each <li> element
for li in li_elements:
    # Extract the university name
    university_name = li.find("a", class_="Anchor-byh49a-0 Card__StyledAnchor-sc-1ra20i5-8 PlBer kijIJB card-name").text

    # Extract the rank
    rank = li.find("div", class_="RankList__Rank-sc-2xewen-2 fxzjOx ranked has-badge").text.replace("#", "")

    # Extract the tuition and fees
    tuition_fees = li.find_all("dd", class_="QuickStatHug__Description-hb1bl8-1 eXguFl")[0].text

    # Extract the undergraduate enrollment
    undergraduate_enrollment_dd = li.find_all("dd", class_="QuickStatHug__Description-hb1bl8-1 eXguFl")[1]
    undergraduate_enrollment_p = undergraduate_enrollment_dd.find("p")
    undergraduate_enrollment_p.extract()
    undergraduate_enrollment = undergraduate_enrollment_dd.text

    # Create a dictionary to store the extracted data for this university
    university = {
        "name": university_name,
        "rank": rank,
        "tuition_fees": tuition_fees,
        "undergraduate_enrollment": undergraduate_enrollment,
    }

    # Append the dictionary to the university_list
    university_list.append(university)

# Print the university_list
for university in university_list:
    print(university["name"])
    print(university["rank"])
    print(university["tuition_fees"])
    print(university["undergraduate_enrollment"])