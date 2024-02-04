from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://islamqa.info/en/answers/128927/it-is-essential-to-acquire-and-take-possession-of-items-before-selling-them"
response=requests.get(url)
print(response)
soup=BeautifulSoup(response.content,"lxml")
print(soup)

title=soup.find(class_="title is-4 is-size-5-touch")
print(title.text)

question=soup.find(class_="single_fatwa__question text-justified")
print(question.text)

answer=soup.find(class_="single_fatwa__answer")
print(answer.text)

data=[[title,question,answer]]
df=pd.DataFrame(data,columns=["title","question","answer"])
print(df)
df.to_csv("Ashu.csv")
print("ok")