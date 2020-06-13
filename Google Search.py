#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests as rq
from bs4 import BeautifulSoup
from tkinter import *
window = Tk()
def findlink():
    query = e_val.get()
    payload = {"q": query, 'num' : '20'}
    header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    r = rq.get("https://www.google.co.in/search", params=payload, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    result_div = soup.find_all('div', attrs = {'class': 'r'})
    links = []
    for r in result_div:
        try:
            link = r.find('a')
            if link != '': 
                links.append(link['href'])
        except:
            continue
    t = links[0]
    l1 = Label(window, text="Search Result:")
    t1 = Text(window)
    t1.delete('0.0', 'end')
    t1.insert(END, t)
    l1.grid(row=1, column=0)
    t1.grid(row=2, column=0, columnspan=5)
e_val = StringVar()
e1 = Entry(window, textvariable = e_val)
b1 = Button(window, text="Search", command=findlink)
e1.grid(row=0, column=0, columnspan=3)
b1.grid(row=0, column=3)
window.mainloop()


# In[ ]:




