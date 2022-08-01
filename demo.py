import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


url = 'https://www.pararius.com/apartments/amsterdam/page-'


title = []
loc = []
price = []
area = []
rooms = []


def scrapingFunc(webpage, page_number):
   next_page = webpage + str(page_number)
   result = requests.get(str(next_page))
   doc = BeautifulSoup(result.content, "html.parser")

   items = doc.find_all("section", class_="listing-search-item")


   for item in items:
        title.append(item.find("a", class_="listing-search-item__link--title").text) 
        loc.append(item.find("div", class_="listing-search-item__location").text.strip()) 
        price.append(item.find("div", class_="listing-search-item__price").text.strip())
        area.append(item.find("li", class_="illustrated-features__item illustrated-features__item--surface-area").text)
        rooms.append(item.find("li", class_="illustrated-features__item illustrated-features__item--number-of-rooms").text)

 #Generating the next page url
   if page_number < 16:
      page_number = page_number + 1
      scrapingFunc(webpage, page_number)
      
#calling the function with arguments
scrapingFunc(url, 1)


#creating the data frame and populating its data into the csv file
data = { 'Title': title, 'Loc': loc, 'Price': price, 'Area': area, 'Rooms': rooms}
df = DataFrame(data, columns = ['Title', 'Location', 'Price', 'Area', 'Rooms'])
df.to_csv(r'C:\Users\wled3\par4.csv')