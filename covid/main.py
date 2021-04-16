import requests
import tkinter as tk
import bs4 

def html(url):
    data = requests.get(url)
    return data

def listtostring(s):
    strcon = ""
    for i in s:
        strcon += i
    return strcon

def load():
    updated_data = covid_19_data()
    pagelabel['text'] = updated_data

def covid_19_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = html(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    real_data = ""
    lst = []
    for item in div:
        text = item.find("h1", class_=None).get_text()
        count = item.find('span', class_=None).get_text()
        total_data = real_data + text + " " + count + "\n"
        lst.append(total_data)
        if len(lst) < 3:
            continue
        lst = listtostring(lst)
    return lst
covid_19_data()

def country_data():
    name = textfield.get
    url ="https://www.worldometers.info/coronavirus/country/"+name
    html_data = html(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    real_data = ""
    lst = []
    for item in div:
        text = item.find("h1", class_=None).get_text()
        count = item.find('span', class_=None).get_text()
        total_data = real_data + text + " " + count + "\n"
        lst.append(total_data)
        if len(lst) < 3:
            continue
        lst = listtostring(lst)
    pagelabel['text'] = lst


base = tk.Tk()
base.geometry("1300x700")
base.title("Covid Data")
f = ('sans-serif', 25, "bold")
pagelabel = tk.Label(base, text=covid_19_data(), font=f)
pagelabel.pack()
textfield = tk.Entry(base, width= 40)
textfield.pack()

button = tk.Button(base, text="Reload", font=f, relief='solid', command=load)
button.pack()

button = tk.Button(base, text="Get Data", font=f, relief='solid', command=country_data)
button.pack()

base.mainloop()
