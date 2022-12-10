# Import the BeautifulSoup4 library
from bs4 import BeautifulSoup

# Read the file content
# parse the HTML file using BeautifulSoup
with open("university.html", encoding='utf-8') as f:
    soup = BeautifulSoup(f, "html.parser")

# Find all the <li> elements that contain the information we want to extract
li_elements = soup.find_all("li", class_="item-list__ListItemStyled-sc-18yjqdy-1 boZDDO")

    # Create an empty list to store the extracted information
university_list = []

# Loop through each li element with class "item-list__ListItemStyled-sc-18yjqdy-1 boZDDO"
for li in soup.find_all('li', class_="item-list__ListItemStyled-sc-18yjqdy-1 boZDDO"):
    # Extract the university name from the li element
    temp_university_name=li.find("h3").find("a", class_="Anchor-byh49a-0 Card__StyledAnchor-sc-1ra20i5-8 PlBer kijIJB card-name").text
    #print(temp)
    university_name = temp_university_name.replace("\n","").replace("  ",'')
    
    # Extract the rank from the li element
    rank = li.find("div", class_="RankList__Rank-sc-2xewen-2 fxzjOx ranked has-badge").strong.text.strip().replace('#', '').replace("\n", "")
    
    # Extract the tuition and fees from the li element
    tuition_and_fees = li.find("dd", class_="QuickStatHug__Description-hb1bl8-1 eXguFl").text.strip().replace("\n", "")
    
   # Extract the undergraduate enrollment
    undergraduate_enrollment_dd = li.find_all("dd", class_="QuickStatHug__Description-hb1bl8-1 eXguFl")[1]
    undergraduate_enrollment_p = undergraduate_enrollment_dd.find("p")
    undergraduate_enrollment_p.extract()
    undergraduate_enrollment = undergraduate_enrollment_dd.text.replace("\n","")
    
    # Append the extracted information to the university_list
    university_list.append({
        'rank': rank,
        'university': university_name,
        'tuition_and_fees': tuition_and_fees,
        'undergraduate_enrollment': undergraduate_enrollment
    })

# Loop through the items in the university_list and print them
for item in university_list:
    print(item)