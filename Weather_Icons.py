#################################################
#                    INST326                    #
#                  12/11/2019                   #
#        Aisha Koroma and Ayesha Shafquat       #
#                 Final Project                 #
#                 Weather Icons                 #
#################################################

#importing modules
import os #for directory
import urllib.request #for opening urls

#creating lists with icon names
day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

# Gettng images from API
base_url = 'https://openweathermap.org/img/w/'
#creating folder 'img 'in your directory to hold icons
img_dir = './img/'
if not os.path.exists(img_dir):
    #making the directory
    os.makedirs(img_dir)

# Get the day weather icons
# loop through icon list
for name in day:
    # create a local file named 'img' and insert icon list names
    file_name = img_dir+name
    if not os.path.exists(file_name):
        #copying the icon API to local file (downloading) 
        urllib.request.urlretrieve(base_url+name, file_name)

# Repeat the same thing for night weather icons
for name in night:
    file_name = img_dir+name
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(base_url+name, file_name)