from customtkinter import *
from PIL import Image
from geopy.geocoders import Nominatim
import requests
from timezonefinder import TimezoneFinder
import pytz
import datetime
from tkinter import messagebox

root = CTk()

bg = "#DAFAFF"
text = '#AEEDFF'
borderco = '#83E1FF'
fg = "#57D4FF"
borderwd = 1
conrerRD = 25
avtive = "#2CC8FF"
borderCoo = "#00BBFF"
fg_co = "#00BBFF"


def get_weather():
    place = search.get()
    geolocator = Nominatim(user_agent="alpha v0.0")
    location = geolocator.geocode(place)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.datetime.now(home)
    current_time = local_time.strftime('%I:%M %p')
    TILABEL.configure(text=current_time)
    COlabel.configure(text='Current Weather')

    # Main Weather
    api_key = 'a8322b8329adee52eb401d6533d4e0ac'
    api = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
    try:
        Json_data = requests.get(api).json()
        condition = Json_data['weather'][0]['main']
        description = Json_data['weather'][0]['description']
        temperature = int(Json_data['main']['temp'] - 273.15)
        Pressure = Json_data['main']['pressure']
        humidity = Json_data['main']['humidity']
        wind = Json_data['wind']['speed']
        # Configs
        WindLab_.configure(text=wind)
        humidLab_.configure(text=humidity)
        discription__.configure(text=description)
        pressuer__.configure(text=Pressure)
        heat.configure(text=(temperature,"°"))
        condition__.configure(text=(condition,"|","More","Like",temperature,"°"))
    except Exception as e:
        messagebox.showerror("ERROR!","ERROR fetching weather",e)


# ==main==#
root.geometry("1195x666+400+100")
root.config(bg=bg)
root.title('SkyCast')
root.iconbitmap('icon.ico')
search = CTkEntry(root, placeholder_text=". . .", placeholder_text_color=text, justify='center', bg_color=bg,
                  text_color=text, border_color=borderco, fg_color=fg, width=450, height=60,
                  font=('Sego UI Black', 22), border_width=borderwd, corner_radius=conrerRD)
searchBtn = CTkButton(root, command=get_weather, text="Search", height=60, bg_color=bg, text_color=text,
                      border_color=borderco, fg_color=fg, border_width=borderwd, corner_radius=conrerRD,
                      hover_color=avtive)

# ==labels==#
COlabel = CTkLabel(root, text=" ", text_color=text, font=('Sego UI Black', 30, "bold"), bg_color=bg)
TILABEL = CTkLabel(root, text=" ", text_color=text, font=('Sego UI Black', 33, "bold"), bg_color=bg)

# ==frame==#
LastFrame = CTkFrame(root, bg_color=bg, fg_color=fg_co, border_color=borderCoo, border_width=8, width=1165, height=150)

# Images
wind = CTkImage(dark_image=Image.open('Assets\\wind.png'), size=(71, 57))
humidity = CTkImage(dark_image=Image.open('Assets\\hu.png'), size=(79, 67))
#pressure_ = CTkImage(dark_image=Image.open('Assets\\29392.png'), size=(20, 20))
MainWeather_ = CTkImage(dark_image=Image.open('Assets\\weather02-512.png'), size=(303, 247))
# labs
WindLab = CTkLabel(LastFrame, text="Wind  ", image=wind, compound=RIGHT, text_color=text,
                   font=('Sego UI Black', 30, "bold"))
humidLab = CTkLabel(LastFrame, text="Humidity  ", image=humidity, compound=RIGHT, text_color=text,
                    font=('Sego UI Black', 30, "bold"))
discription = CTkLabel(LastFrame, text="Description", text_color=text, font=('Sego UI Black', 30, "bold"))
pressuer = CTkLabel(LastFrame, text="Pressure", text_color=text, font=('Sego UI Black', 30, "bold"))
#pressuerIMG = CTkLabel(LastFrame, text=" ", image=pressure_, text_color=text, font=('Sego UI Black', 30, "bold"))

# dataLabs
WindLab_ = CTkLabel(LastFrame, text=". . .", text_color=text, font=('Sego UI Black', 30, "bold"))
humidLab_ = CTkLabel(LastFrame, text=". . .", text_color=text, font=('Sego UI Black', 30, "bold"))
discription__ = CTkLabel(LastFrame, text=". . . . . .", text_color=text, font=('Sego UI Black', 30, "bold"))
pressuer__ = CTkLabel(LastFrame,text=". . . . .", text_color=text, font=('Sego UI Black', 30, "bold"))

# Main weather
weather_label = CTkLabel(root,image=MainWeather_,bg_color=bg,text='')

heat = CTkLabel(root,text='',bg_color=bg,text_color='orange',font=('Sego UI Black', 90))
condition__ = CTkLabel(root,text='',bg_color=bg,text_color='orange',font=('Sego UI Black', 30, "bold"))



# Place_packs
weather_label.place(x=400,y=150)
heat.place(x=740,y=220)
condition__.place(x=740,y=340)
LastFrame.pack(side=BOTTOM, pady=10)
WindLab.place(x=40, y=25)
humidLab.place(x=350, y=20)
discription.place(x=700, y=35)
pressuer.place(x=1000, y=35)
#pressuerIMG.place(x=900, y=38)
WindLab_.place(x=60, y=100)
humidLab_.place(x=400, y=100)
discription__.place(x=710, y=100)
pressuer__.place(x=1020, y=100)
COlabel.place(x=45, y=100)
TILABEL.place(x=45, y=140)
searchBtn.place(x=500, y=20)
search.place(x=30, y=20)
root.mainloop()
