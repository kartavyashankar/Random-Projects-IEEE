#!/usr/bin/env python
# coding: utf-8

# In[34]:


import requests as rq
from bs4 import BeautifulSoup
import re
from tkinter import *

window=Tk()
e_val=StringVar()
def get_info():
    query = e_val.get()
    payload = {'q' : query}
    header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    r = rq.get("https://www.flipkart.com/search", params=payload, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    results_div = soup.find_all('div', attrs={'class' : re.compile('_1HmYoV _35HD7C'), 'style' : re.compile('flex-grow:1;overflow:auto')})
    links = []
    names = []
    prices = []
    for rd in results_div:
        results_div_deep = rd.find_all('div', attrs = {'class' : re.compile('bhgxx2 col-12-12')}, style = False)
    for rdd in results_div_deep:
        link = rdd.find_all('a', title=True) 
        for l in link:
            links.append("https://www.flipkart.com"+l['href'])
            names.append(l['title'])
        price = rdd.find_all('div', attrs = {'class' : '_1vC4OE'})
        for p in price:
            prices.append(p.string)
    t1.delete('0.0', 'end')
    t1.insert(END, links[0])
    l1 = Label(window, text="Name : ")
    l2 = Label(window, text="Price : "+prices[0])
    l3 = Label(window, text="Link : ")
    l4 = Label(window, text=names[0])
    l1.grid(row=1, column=0)
    l4.grid(row=1, column=1)
    l2.grid(row=2, column=0)
    l3.grid(row=3, column=0)
    t1.grid(row=3, column=1)
e1 = Entry(window, textvariable=e_val)
b1 = Button(window, text="Flipkart Search", command=get_info)
t1 = Text(window)
e1.grid(row=0, column=0, columnspan=4)
b1.grid(row=0, column=4, columnspan=2)
window.mainloop()


# In[ ]:




