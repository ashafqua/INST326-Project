#################################################
#                    INST326                    #
#                  12/11/2019                   #
#        Aisha Koroma and Ayesha Shafquat       #
#                 Final Project                 #
#              Weather application              #
#################################################

#importing modules
import requests
import tkinter as tk
from PIL import Image
from PIL import ImageTk

HEIGHT=500
WIDTH=600 

# creating function that GETs JSON data for the weather using the openweather API
def get_weather(city):
    key='a4aa5e3d83ffefaba8c00284de6ef7c3'
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    data = response.json()
    label['text'] = response_format(data)
    icon = data['weather'][0]['icon']
    open_image(icon)
    
# function that retrieves weather information     
def response_format(weather):
    #test block of code for errors using try method so the program doesnt crash
    try:
        # variable storage also
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        wind_speed = weather['wind']['speed']
        wind_dir = weather['wind']['deg']
        wind_dir = wind_direction_convert(wind_dir)
        humidity = weather['main']['humidity']
        hightemp = int(weather['main']['temp_max'])
        lowtemp = int(weather['main']['temp_min'])
        latitude = weather['coord']['lat']
        longitude = weather['coord']['lon']
        icon = weather['weather'][0]['icon']
        
        # print formatting for GUI interface
        final_str = """
City: {}
Conditions: {}
Temperature: {}°F
Wind Speed: {} mph
Wind Direction: {}
Humidity: {}%
Local Coordinates: ({:.2f}, {:.2f})
High Temperature: {}°F
Low Temperature: {}°F
""".format(name, description, temperature, wind_speed, wind_dir, humidity, latitude, longitude, hightemp, lowtemp)
    
    # if error found this is the return statement
    except:
       final_str = 'There was a problem retrieving that information'
    return final_str
    
# function for converting wind direction    
def wind_direction_convert(degree):
#Takes in the variable wind_dir and converts the numeric value to its corresponding cardinal direction
    if degree >= 337.501 or degree <= 22.5:
        wind_direction = 'North'
    elif degree >= 22.501 and degree <= 65.5:
        wind_direction = 'Northeast'
    elif degree >= 65.501 and degree <= 112.5:
        wind_direction = 'East'
    elif degree >= 112.501 and degree <= 157.5:
        wind_direction = 'Southeast'
    elif degree >= 157.501 and degree <= 202.5:
        wind_direction = 'South'
    elif degree >= 202.501 and degree <= 247.5:
        wind_direction = 'Southwest'
    elif degree >= 247.501 and degree <= 292.5:
        wind_direction = 'West'
    else:
        wind_direction = 'Northwest'
    return wind_direction

# function for weather icon implementation
def open_image(icon):
    size = int(lower_frame.winfo_height()*0.35)
    #retrieving icon image from local file 'img'
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

# GUI design (adding tkinter widgets)
# Creating parent window named root
root = tk.Tk()
root.title("Gui Weather App!")

# creating app canvas/interface
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#styling interface
background_image = tk.PhotoImage(file="background.jpg")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
  

# Creating container to hold widgets
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# adding user input widget (search box)
entry = tk.Entry(frame, text="Enter a city",font=40)
entry.place(relwidth=0.65, relheight=1)

# adding button widget. Command calls get_weather function and passes 'entry' as the parameter
button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# 2nd frame background and border styling
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

#icon styling
weather_icon = tk.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=1)

# method to run application
root.mainloop()

