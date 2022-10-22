
#===========================================================
#Получить bs4 текст по классу
#-----------------------------------------------------------
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.text, 'lxml')
data = soup.find_all(class_ = "username")
for x in data:
    print (x)
#===========================================================