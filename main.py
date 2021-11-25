import tkinter #for creating the window
import requests#for making api call and requesting the weather data
import json#for working with the raw json data from api call

api_key = "5957d1aeff3d4cc185d101803212311"
#doing a get request and storing the response
raw = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=bangalore&aqi=yes")

#converting the raw json response to usable json
result = json.loads(raw.text)

#getting image for the weather condition

img_url = result["current"]["condition"]["icon"]
raw_img = requests.get(f"https:{img_url}")

with open("icon.png","wb") as icon:
    icon.write(raw_img.content)
    icon.close()

#data from api
cond = result["current"]["condition"]["text"]
temp_c = result["current"]["temp_c"]
location =result["location"]["name"]
state =result["location"]["region"]
country =result["location"]["country"]
humidity = result["current"]["humidity"]
wind = result["current"]["wind_kph"]
wind_direction =result["current"]["wind_dir"]
feelslike = result["current"]["feelslike_c"]
#aqi = air quality index
aqi_co=result["current"]["air_quality"]["co"]
aqi_no2=result["current"]["air_quality"]["no2"]
aqi_o3=result["current"]["air_quality"]["o3"]
aqi_so2=result["current"]["air_quality"]["so2"]


#tkinter code starts from here
window = tkinter.Tk()
window.title("weather app")
#window size
window.geometry("400x300")
#fixed window size
window.resizable(False, False)

#picture widget definition
pic = tkinter.Canvas(window,width=500,height=300)
pic.pack()
img = tkinter.PhotoImage(file="icon.png")
pic.create_image(40,60,image=img)

#text widget defintion
condition = tkinter.Label(window,text=cond)#,width=10)
temperature = tkinter.Label(window,text=temp_c)
location = tkinter.Label(window,justify="right",
text=f"{location}\n{state}\n{country}")

degree = tkinter.Label(window,text="°C")

extra_info=tkinter.Label(window,justify="left",
text=f"humidity: {humidity}%\nwindspeed: {wind}km/h\nwind direction: {wind_direction}\nfeels like: {feelslike}°C")

air_index = tkinter.Label(window,justify="left",
text=f"air quality index:\n  CO: {round(aqi_co,2)}ppm\t\tNO2: {aqi_no2}ppb\n  O3: {round(aqi_o3,2)}ppb\t\tSO2: {round(aqi_so2,2)}ppb")

#text configs
condition.config(font=('Sans-serif','18'))
temperature.config(font=('Sans-serif','40'))
degree.config(font=('Sans-serif','14'))
location.config(font=('Sans-serif','16'))
extra_info.config(font=('Sans-serif','12'))
air_index.config(font=('Sans-serif','12'))

#positions for widgets
condition.place(x=250,y=30)
temperature.place(x=95,y=20)
location.place(x=285,y=100)
degree.place(x=200,y=20)
extra_info.place(x=15,y=110)
air_index.place(x=20,y=200)


#inbuilt infinite loop to run the program
window.mainloop()
