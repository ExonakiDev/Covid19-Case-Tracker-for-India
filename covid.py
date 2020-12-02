from tkinter import *
import os, sys
from PIL import ImageTk, Image
import requests
import urllib.request, urllib.parse, urllib.error
import json

global count
count = 0

#api
api_url = 'https://api.covid19india.org/state_district_wise.json'
# api_requests = requests.get('https://api.covid19india.org/state_district_wise.json')


#intializing root window
root=Tk()
#window title
root.title('India Covid-19 Tracker')
#window icon
if 'nt' == os.name:
	root.iconbitmap(bitmap = 'icon.ico')
else:
	root.iconbitmap(bitmap = '@icon1.xbm')
#window size
root.geometry('1000x500')

banner_img = ImageTk.PhotoImage(Image.open('images/banner3.png'))
banner_lbl = Label(image = banner_img)
banner_lbl.grid(row = 0, column = 0, columnspan = 10)



def fetch_live_cases():
	uh = urllib.request.urlopen(api_url)
	data = uh.read().decode()
	try:
		api = json.loads(data)
	except:
		api=None
	st_pass = state_select.get()
	ct = city_entrymenu.get().lower()
	ct_pass = ct.capitalize()
	rb = r.get()
	for state in api:
		if state == st_pass:
			to_display = api[state]['districtData'][ct_pass][rb]

	myLabel.config(text = 'The number of ' + rb + ' cases in '+ ct_pass + ', '+ st_pass + ' at the moment is ' + str(to_display), font = ('Helvetica', 15), background = 'green')




def set_radio_btn(value):
	r.set(value)

# def popup():
# 	response = messagebox.showerror("Place not found!")
# 	Label(root, text = response).pack()
# 	Label(root, text = e).pack()





#states list
states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 
	'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
	'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 
	'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
	'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
	]

state_select = StringVar()
state_select.set(states[0])



#types of cases
TYPES = [('Active', 'active'), ('Total', 'confirmed')
		, ('Deceased', 'deceased'), ('Recovered', 'recovered')]
r = StringVar()
r.set('active')




#Location Selection
state_label = Label(root, text = 'Select State: ')
state_label.grid(row = 1, column = 0, padx = (10,0), pady = 20)

state_dropmenu = OptionMenu(root, state_select, *states)
state_dropmenu.grid(row = 1, column = 1, pady = 10)

city_label = Label(root, text = 'Select City: ')
city_label.grid(row = 2, column = 0, pady = 10)

city_entrymenu = Entry(root, width = 35, borderwidth = 4)
city_entrymenu.grid(row = 2, column = 1 , pady = 10)

#types of cases radio buttons
types_label = Label(root, text= 'Select type of cases: ')
types_label.grid(row = 1, column = 2, padx = 10, pady = 10)

#create radio buttons

active_rbtn = Radiobutton(root, text="Active", variable=r, value='active', command=lambda: set_radio_btn('active'))
total_rbtn = Radiobutton(root, text="Total", variable=r, value='confirmed', command=lambda: set_radio_btn('confirmed'))
deceased_rbtn = Radiobutton(root, text="Deceased", variable=r, value='deceased',command=lambda: set_radio_btn('deceased'))
recovered_rbtn = Radiobutton(root, text="Recovered", variable=r, value='recovered', command=lambda: set_radio_btn('recovered'))

#display radio buttons
active_rbtn.grid(row = 1, column = 3)
total_rbtn.grid(row = 2, column = 3)
deceased_rbtn.grid(row = 3, column = 3)
recovered_rbtn.grid(row = 4, column = 3)

#Search Button

search_btn = Button(root, text = 'Search Cases', padx = 100, command = fetch_live_cases)
search_btn.grid(row = 3, column = 1, pady = 10)

myLabel = Label(root)
myLabel.grid(row = 5, column = 1)

root.mainloop()