from bs4 import BeautifulSoup
html = """
<div class="channel-item">
    <div class="likes">48<br>喜欢</div>
    <div class="bd"></div>
</div>

"""
# soup = BeautifulSoup(html, 'lxml')
# text = soup.select('div.likes, br')
# soup2 = text[0].prettify().split(text[1].prettify())
# soup2 = BeautifulSoup(soup2[0], 'lxml')
# text = soup2.select('div.likes')[0].get_text().strip()
# print(text)

soup = BeautifulSoup(html, 'lxml')
text = soup.select('div.likes, br')
soup2 = text[0].prettify().split(text[1].prettify())
soup2 = BeautifulSoup(soup2[0], 'lxml')
text = soup2.select('div.likes')[0].get_text().strip()
print(text)

