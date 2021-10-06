from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/p/pl?N=100007709%20601194948%20601202919%20601203901%20601203927%20601205646%20601294835%20601295933%20601296377%20601301599%20601305993%20601321572%20601323902%20601326374%20601331379%20601341679%20601357282%20601359511&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_2'
uclient=uReq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})

filename = 'products.csv'
f=open(filename, "w")
headers = "brand, product_name, shipping, product_price\n" 
f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container=container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    price=container.findAll("div",{"class":"item-action"})
    price_text=price[0].findAll("strong")
    product_price= price_text[0].text.strip()
    
    #print("brand" + brand)
    #print("product_name" + product_name)
    #print("shipping"+ shipping)
    #print("product_price" + product_price)

    f.write(brand + "," + product_name.replace("," , "|") + "," + shipping + "," + product_price.replace("," , "|") + "\n")
f.close()
