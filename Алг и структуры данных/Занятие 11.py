from tkinter import *
import requests
import json

def clicked(event):
    api = f'https://api.github.com/users/{entry.get()}'
    user_data = requests.get(api).json()
    company = user_data['company']
    created_at = user_data['created_at']
    email = user_data['email']
    id = user_data['id']
    name = user_data['name']
    url = user_data['url']
    json_data = {'company': company, 'created_at': created_at, 'email': email, 'id': id, 'name': name, 'url': url}
    with open('res.json', 'w') as f:
        json.dump(json_data, f)

window = Tk()
window.title("ПР11")
window.geometry("500x250")

base_lbl = Label(text="Имя репозитория (Например rust)")
base_lbl.place(relx=.5, rely=.4, anchor="center")

entry = Entry(window, width=40)
entry.place(relx=.5, rely=.5, anchor="center")

btn = Button(text="json")
btn.place(relx=.5, rely=.6, anchor="center")
btn.bind("<Button-1>", clicked)

window.mainloop()