import omdb
import re
with open('Baza', 'r') as myfile:
	data=myfile.read()



def txt():
	mtext = ment.get()	
	[print(ment.get()) if mtext == data else print("false")]

def txt2():
	[print(ment.get()) if ment.get() in open('Baza').read() else print("false")]


def txt3():
	movie=omdb.get(title=ment.get(), year=ment1.get(), tomatoes=True, fullplot=True)
	print(movie)
	

from tkinter import *
from tkinter import ttk
root=Tk()
ment=StringVar()
ment1=StringVar()
ment2=StringVar()
ment3=StringVar()
ment4=StringVar()
ment5=StringVar()

sortvar = StringVar()
sort = ttk.Combobox(root, textvariable=sortvar)

Title = Label(root, text="Find your movie!")
Title1 = Label(root, text="Full title")
Title2 = Label(root, text="Part of the title")
Genre = Label(root, text="Genre")
Rating = Label(root, text="Rating")
Popularity = Label(root, text="Popularity")
Profit = Label(root, text="Profit")
Sort = Label(root, text="Sort by")

Title.grid(row=0, columnspan=2)
Title1.grid(row=1, sticky=E)
Title2.grid(row=2, sticky=E)
Genre.grid(row=3, sticky=E)
Rating.grid(row=4, sticky=E)
Popularity.grid(row=5, sticky=E)
Profit.grid(row=6, sticky=E)
Sort.grid(row=7, sticky=E)

entry1 = Entry(root, textvariable=ment)
entry2 = Entry(root, textvariable=ment1)
entry3 = Entry(root, textvariable=ment2)
entry4 = Entry(root, textvariable=ment3)
entry5 = Entry(root, textvariable=ment4)
entry6 = Entry(root, textvariable=ment5)
entry7 = ttk.Combobox(root, textvariable=sortvar)
sort['values'] = ('Rating', 'Title', 'Release date', 'Popularity', 'Profit')

entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
entry3.grid(row=3, column=1)
entry4.grid(row=4, column=1)
entry5.grid(row=5, column=1)
entry6.grid(row=6, column=1)
sort.grid(row=7, column=1)

Image = PhotoImage(file="camera.png")
label = Label(root, image=Image)
label.grid(row=1, column=2, columnspan=2, rowspan=6, sticky= W+E+N+S)

button1=Button(text="OK", command=txt3, fg="red")
#button1=Button(text="OK", command=txt2, fg="red")
button1.grid(columnspan=3)



root.mainloop()
