# 1.download the page
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 1.1 open connection
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

# 1.2 Read data
raw_data = conn.read()
# 1.3 Decode data
content = raw_data.decode ("utf8")
# print (content)
f = open ("apple.html", "wb")
f.write(raw_data)
f.close ()
# 2 Find ROI
soup = (BeautifulSoup(content, "html.parser"))
# print (soup)
ul_news = soup.find("ul", "")
# print(ul_news.prettify())

# Copy n Save
li_list = ul_news.find_all("li")
name= {
"names" : "",
}
song = {
"artists" : "",
}
for i in range (100):
    li = li_list[i]
# print (li.prettify)
# walking
    h4 = li.h4
    a = h4.a
    name[i] = a.string
for j in range (i,100):
    h3 = li.h3
    a = h3.a
    song[i] = a.string
    break
for i in range (100):
    print ()
    print ("Bai hat thu ", i+1, " la: ")
    print (song[i])
    print (name[i])
# pyexcel.save_as(records=li_list, dest_file_name="apple.xlsx")
