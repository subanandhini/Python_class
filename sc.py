from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
import requests

# res=requests.get("https://www.google.com/search?q=chennai+weather&rlz=1C1CHBF_enIN993IN993&oq=&aqs=chrome.1.69i59i450l8.237389514j0j15&sourceid=chrome&ie=UTF-8")
# print(res)
# variable=res.text
def weather(city):
    city=city+" weather"
    city=city.replace(" ","+")
    # city=input("city name= ")
    res=requests.get(f"https://www.google.com/search?q={city}&oq={city}&aqs=chrome.1.69i59i450l8.237389514j0j15&sourceid=chrome&ie=UTF-8")
    print("searching in google......\n")
    jerry=res.text
    soup=BeautifulSoup(res.text,"html.parser")

    location=soup.select('#wob_loc')[1].getText().strip()    #wob_loc
    time=soup.select("#wob_dts")[1].getText().strip()
    info=soup.select("#wob_dc")[1].getText().strip()             #wob_dts
    weather=soup.select("#wob_tm")[1].getText().strip()

    condition=time+"\n"+info
    lblcondition["text"]=condition
    metric=weather+"°C"
    lblmetric["text"]=metric
    
def chkweather():
    print("hii")
    city=cmbcity.get()
    weather(city)

root=Tk()
root.geometry("1000x500")
lblcity=Label(root,text="select a city:")
lblcity.grid(row=0,column=0)
cities=("madhurai","chennai","erode","salem","namakkal","coimbatore")
cmbcity=ttk.Combobox(root,values=cities) 
cmbcity.grid(row=0,column=1)                           
btnchk=Button(root,text="find",command=chkweather)
btnchk.grid(row=0,column=2)
lblcondition=Label(root,text="          ") 
lblmetric=Label(root,text="             ")     
lblcondition.grid(row=1,column=0)
lblmetric.grid(row=1,column=1)
root.mainloop()


