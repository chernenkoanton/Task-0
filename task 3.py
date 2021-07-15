import http.client
from tkinter import *
import re
import os
import sys

# оиск информации по стране, ключ-слову в tmp
def search_info(country,tmp,key_word):
    result_country = re.search(country, tmp)
    end_country = result_country.end() #поиск начала поиска по стране
	@@ -18,7 +19,7 @@ def search_info(country,tmp,key_word):
                s += tmp[end_search+i+end_country]
                i+=1
            return s
        else: break 


conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
	@@ -35,16 +36,16 @@ def search_info(country,tmp,key_word):
#Show
root = Tk()
root.title("Covid Asia")
root.geometry("600x850")
for i in range(len(lst_country)):
    lab_country = Label(root, text = lst_country[i],font ="Arial 14",fg = "black" )
    lab_country.place(x = 20, y = 50*i*3.5)
    for j in range (len(lst_search)):
        lab_search = Label(root, text = search_info(lst_country[i],tmp,lst_search[j]),font ="Arial 14",fg = "green" )
        lab_search.place(x = 20, y = 50*i*3.5+25*(j+1))
#Перезапуск программы для обновления данных 
def restartProgram():
    os.execl(sys.executable, os.path.abspath('civid.py'), *sys.argv)         
restartButton = Button(text = "RESTART", command = restartProgram)
restartButton.place(x = 400, y = 100, width = 200, height = 40)
root.mainloop()
