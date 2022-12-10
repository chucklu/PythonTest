from bs4 import BeautifulSoup

html = """
<td data-v-3fe7d390="">
    <div>
        北京
    </div>
    <!-- --></td>"""

soup = BeautifulSoup(html, "html.parser")

# Extract the text content of the <td> element using the string attribute
td_string = soup.td.string

# Extract the text content of the <td> element using the get_text() method
td_text = soup.td.get_text()

# Print the text content of the <td> element
print("string attribute:", td_string)
print("get_text() method:", td_text)
