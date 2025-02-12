from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
header={"user-Agent":"Mozilla/5.0"}
r=requests.get(url,headers=header)
soup=BeautifulSoup(r.text,"html.parser")
ans=[]
cnt=0
for i in soup.find_all("h3",class_="ipc-title__text"):
    if cnt<5:
        ans.append(i.text.split(". ",1)[-1])
    cnt+=1
print(ans)