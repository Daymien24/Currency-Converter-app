import tkinter as tk
import requests
from PIL import Image, ImageTk
#ukladanie elementow - pack (side, fill, expand) or grid or place(najlepsze)



def format_response(curr, spis, ile):
    try:        
        value = int(ile)
        eur = spis['rates']['EUR']
        usd = spis['rates']['USD']
        gbp = spis['rates']['GBP']
        chf = spis['rates']['CHF']
        pln = spis['rates']['PLN']
        if curr == "PLN":
            if value == 1:
                final_str = (f"For {value} zl unit you'll get:\n\n"
                        f'Euro: {value*eur:.2f} \nDolar: {value*usd:.2f} \nFunt: {value*gbp:.2f} \nFrank: {value*chf:.2f} ')
            if value < 0:
                final_str = "You cant convert a negatvie value!"
            else:
                final_str = (f"For {value} zl units you'll get:\n\n"
                            f'Euro: {value*eur:.2f} \nDolar: {value*usd:.2f} \nFunt: {value*gbp:.2f} \nFrank: {value*chf:.2f} ')
        if curr == "EUR":
            if value == 1:
                final_str = (f"For {value} euro you'll get:\n\n"
                        f'PLN: {value*pln:.2f} \nDolar: {value*usd:.2f} \nFunt: {value*gbp:.2f} \nFrank: {value*chf:.2f} ')
            if value < 0:
                final_str = "You cant convert a negatvie value!"
            else:
                final_str = (f"For {value} euro you'll get:\n\n"
                            f'PLN: {value*pln:.2f} \nDolar: {value*usd:.2f} \nFunt: {value*gbp:.2f} \nFrank: {value*chf:.2f} ')
        if curr == "USD":
            if value == 1:
                final_str = (f"For {value} dollar you'll get:\n\n"
                        f'Euro: {value*eur:.2f} \nPln: {value*pln:.2f} \nFunt: {value*gbp:.2f} \nFrank: {value*chf:.2f} ')
            if value < 0:
                final_str = "You cant convert a negatvie value!"
            else:
                final_str = (f"For {value} dollars you'll get:\n\n"
                            f'Euro: {value*eur:.2f} \nPln: {value*pln:.2f} \nFunt: {value*gbp:.2f} \nFrank: {value*chf:.2f} ')
        if curr == "CHF":
            if value == 1:
                final_str = (f"For {value} frank you'll get:\n\n"
                        f'Euro: {value*eur:.2f} \nDolar: {value*usd:.2f} \nFunt: {value*gbp:.2f} \nPln: {value*pln:.2f} ')
            if value < 0:
                final_str = "You cant convert a negatvie value!"
            else:
                final_str = (f"For {value} franks you'll get:\n\n"
                            f'Euro: {value*eur:.2f} \nDolar: {value*usd:.2f} \nFunt: {value*gbp:.2f} \nPln: {value*pln:.2f} ')

    except:
        final_str = 'Houston, mamy problem!'
    return final_str

photos_saved = []
def open_image(*photos):
    paddy = 10
    for i in range(0,4):
        size = int(lower_frame.winfo_height()*0.09)
        img = ImageTk.PhotoImage(Image.open('./img/'+photos[i]+'.png').resize((size, size)))
        #weather_icon.delete("all") # usuwa wszystkie ikony jake sa w canvasie
        currency_icon.create_image(30,0+paddy, anchor='nw', image=img)
        currency_icon.image = img
        photos_saved.append(img)
        paddy+=25
     

def get_currency(curr,ile):   
    
    url = f'https://api.exchangerate-api.com/v4/latest/{curr}'
    response = requests.get(url)
    spis = response.json()
    text = format_response(curr, spis, ile)
    print(text)
    label['text'] = text
    if curr == "PLN":
        photos = ['euro', 'usa', 'gbp', 'chf']
    if curr == "EUR":
        photos = ['pln', 'usa', 'gbp', 'chf']
    if curr == "USD":
        photos = ['euro', 'pln', 'gbp', 'chf']
    if curr == "CHF":
        photos = ['euro', 'usa', 'gbp', 'pln']
    
    # for i in range(0,4):
    #     icon_name = photos[i]
    #     photos.append(icon_name)

    open_image(*photos)





root = tk.Tk();
root.title("Kantor")

canvas = tk.Canvas(root, height=575, width=600) # size okna
canvas.pack()



background_img = tk.PhotoImage(file='./background/money_treejpg.png',)
background_label = tk.Label(root, image=background_img)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

frame= tk.Frame(root, bg='#45fc03', bd=5) #bd- border
frame.place(relx=0.5, rely=0.35,relwidth=0.5, relheight=0.1, anchor='n') #resnponsive, change size ekranu, wypelnia kolorkiem okno

clicked = tk.StringVar()
clicked.set("PLN")
drop = tk.OptionMenu(frame, clicked, "PLN", "EUR", "USD", "CHF")
drop.place(relwidth=0.23, relheight=1)

entry = tk.Entry(frame, font=('Comic Sans MS', '10','bold'))
entry.place(relx=0.25, relwidth=0.4, relheight=1)

button = tk.Button(frame,font=('Comic Sans MS', '10','bold'), text="Convert", bd = 3, activeforeground = 'green', command=lambda: get_currency(clicked.get(), entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#45fc03', bd=10)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.4, anchor='n')


label = tk.Label(lower_frame, font = ('Comic Sans MS', '13','bold'), anchor='nw', justify='left', bd=4)
label.place( relwidth=1, relheight=1)

currency_icon = tk.Canvas(label, bd=0, highlightthickness=0)
currency_icon.place(relx=.5, rely = 0.22, relwidth=1)
#print(clicked.get())
root.mainloop()