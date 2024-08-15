#Chap09_클리앙중고장터검색.py
from bs4 import BeautifulSoup
import urllib.request
import re 

for n in range(0,10):
        #클리앙의 중고장터 주소 
        url ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(url)
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        # <span class="subject_fixed" data-role="list-title-text" title="맥북에어 m2 16g 판매합니다.">
		# 		맥북에어 m2 16g 판매합니다. 
		# </span>
        for item in list:
            title = item.text.strip()
            print(title)


