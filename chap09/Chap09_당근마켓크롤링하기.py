#Chap09_당근마켓크롤링하기.py
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
page = urllib.request.urlopen(url).read() 

soup = BeautifulSoup(page, 'html.parser')

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
   titleElem = post.find("h2", attrs={"class":"card-title"})
   priceElem = post.find("div", attrs={"class":"card-price"})
   addrElem = post.find("div", attrs={"class":"card-region-name"})
   title = titleElem.text.strip() 
   price = priceElem.text.strip() 
   addr = addrElem.text.strip() 
   print("{0} , {1} , {2}".format(title, price, addr))

#선택한 영역을 주석처리하기: ctrl + / 
# <div class="card-desc">
#       <h2 class="card-title">위닉스제습기  10L</h2>
#       <div class="card-price ">
#         20,000원
#       </div>
#       <div class="card-region-name">
#         경기도 성남시 분당구 서현1동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 16
#           </span>
#         ∙
#         <span>
#             채팅 57
#           </span>
#       </div>
#     </div>

