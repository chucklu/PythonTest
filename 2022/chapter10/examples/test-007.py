import requests

# Set the User-Agent header to the value of a Chrome browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

# Make a GET request to the URL of the HTML page with the User-Agent header
response = requests.get('https://www.usnews.com/best-colleges/rankings/national-universities', headers=headers)

# Get the data from the response
data = response.text

# Encode the data using the utf-8 encoding
encoded_data = data.encode('utf-8')

# Open a local file for writing
with open('university.html', 'wb', encoding='utf-8') as file:
  # Write the encoded data to the file
  file.write(encoded_data)

# Find all li elements with the class "item-list__ListItemStyled-sc-18yjqdy-1 boZDDO"
for li in soup.find_all('li', class_='item-list__ListItemStyled-sc-18yjqdy-1 boZDDO'):
    # Extract the rank using the strong element with the class "RankList__Rank-sc-2xewen-2 fxzjOx ranked has-badge"
    rank = li.find('div', class_='RankList__Rank-sc-2xewen-2 fxzjOx ranked has-badge').strong.text
    # Extract the university name using the a element with the class "Anchor-byh49a-0 Card__StyledAnchor-sc-1ra20i5-8 PlBer kijIJB card-name"
    university = li.find('a', class_='Anchor-byh49a-0 Card__StyledAnchor-sc-1ra20i5-8 PlBer kijIJB card-name').text
    # Extract the TUITION AND FEES using the dd element with the class "QuickStatHug__Description-hb1bl8-1 eXguFl"
    tuition_and_fees = li.find('dd', class_='QuickStatHug__Description-hb1bl8-1 eXguFl').text
    # Extract the UNDERGRADUATE ENROLLMENT using the dd element with the class "QuickStatHug__Description-hb1bl8-1 eXguFl"
    undergraduate_enrollment = li.find_all('dd', class_='QuickStatHug__Description-hb1bl8-1 eXguFl')[1].text

    # Print the results
    print(rank, university, tuition_and_fees, undergraduate_enrollment)