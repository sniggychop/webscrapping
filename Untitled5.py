#!/usr/bin/env python
# coding: utf-8

# In[57]:


from bs4 import BeautifulSoup
import requests

url=("https://www.flipkart.com/search?q=camera&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_2_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_2_na_na_na&as-pos=6&as-type=RECENT&suggestionId=camera&requestId=3c065780-86aa-4e6f-83b3-4df71fb7d686&as-searchtext=ca")

response=requests.get(url)
htmlcontent=response.content
soup=BeautifulSoup(htmlcontent)

titles=[]
prices=[]
images=[]

for d in soup.find_all('div',attrs={'class':'_1YokD2 _3Mn1Gg'}):
    title=d.find('div',attrs={'class':'_4rR01T'})
    print(title.string)
    
    price=d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    print(price.string)
    
    image=d.find('img',attrs={'class':'_396cs4'})
    print(image.get('src'))

   
    
    


# In[ ]:





# In[ ]:




