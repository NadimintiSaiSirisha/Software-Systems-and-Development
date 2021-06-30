from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv
row_list=[]
fields = ['Name', 'URL', 'Author', 'Price','Number of ratings','Average ratings']  
my_url = "https://www.amazon.in/gp/bestsellers/books/"
url_client = urlopen(my_url)
page_html = url_client.read()
url_client.close()
#print(page_html)

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("span", {"class":"aok-inline-block zg-item"})
#print(containers[0].prettify())

for container in containers:
    try:
        name = container.find("div",{"class":"p13n-sc-truncate p13n-sc-line-clamp-1 p13n-sc-truncate-desktop-type2"}).string.strip()
    except AttributeError:
        name = "Not available"
    
    try:
        author = container.find("a",{"class":"a-size-small a-link-child"}).string.strip()
    except AttributeError:
        author = "Not available"
    try:
        price = container.find("span",{"class":"p13n-sc-price"}).string.strip()
    except AttributeError:
        price = "Not available"
    try:
        ratingsNo = container.find("a",{"class":"a-size-small a-link-normal"}).string.strip()
    except AttributeError:
        ratingsNo = "Not available"
    try:
        avgRatings = container.find("span",{"class":"a-icon-alt"}).string.strip()
    except AttributeError:
        avgRatings = "Not available"
    try:
        for link in container.find_all('a', href=True):
            halflink = link['href']
            amazon = "https://www.amazon.in"
            url = amazon+halflink
    except AttributeError:
        url = "Not available"
    row = [name,url,author,price,ratingsNo,avgRatings]
    row_list.append(row)

# Second URL for getting 100 books
my_url = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=2"
url_client = urlopen(my_url)
page_html = url_client.read()
url_client.close()
#print(page_html)

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("span", {"class":"aok-inline-block zg-item"})
#print(containers[0].prettify())

for container in containers:
    try:
        name = container.find("div",{"class":"p13n-sc-truncate p13n-sc-line-clamp-1 p13n-sc-truncate-desktop-type2"}).string.strip()
    except AttributeError:
        name = "Not available"
    
    try:
        author = container.find("a",{"class":"a-size-small a-link-child"}).string.strip()
    except AttributeError:
        author = "Not available"
    try:
        price = container.find("span",{"class":"p13n-sc-price"}).string.strip()
    except AttributeError:
        price = "Not available"
    try:
        ratingsNo = container.find("a",{"class":"a-size-small a-link-normal"}).string.strip()
    except AttributeError:
        ratingsNo = "Not available"
    try:
        avgRatings = container.find("span",{"class":"a-icon-alt"}).string.strip()
    except AttributeError:
        avgRatings = "Not available"
    try:
        for link in container.find_all('a', href=True):
            halflink = link['href']
            amazon = "https://www.amazon.in"
            url = amazon+halflink
    except AttributeError:
        url = "Not available"
    row = [name,url,author,price,ratingsNo,avgRatings]
    row_list.append(row)

with open('output/in_book.csv', 'w') as csvfile:  
    csvwriter = csv.writer(csvfile,delimiter=';')  
    csvwriter.writerow(fields)   
    csvwriter.writerows(row_list) 
