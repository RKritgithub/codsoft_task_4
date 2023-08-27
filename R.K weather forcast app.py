from tkinter import*
from tkinter import ttk
# to use API in python we need a module called request(runt he URL)
import requests 
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b6bb23793c3c46e7c09fb8ee81dce087").json()
    weather_lable1.config(text=data["weather"][0]["main"])

    weather_dis_lable1.config(text=data["weather"][0]["description"])

    temperature_lable1.config(text=str(int(data["main"]["temp"]-273.15)))

    pressure_lable1.config(text=data["main"]["pressure"])
    



window = Tk()
window.title("Weather Forecast")
window.configure(bg="#78C1F3")
window.geometry("500x570")

#label creation
name_lable = Label(window, text="Weather App",font=("Bricolage Grotesque",30,"bold"))
name_lable.place(x=25,y=50,height=50,width=450)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir",
"Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

result = ttk.Combobox(window, text="Weather App",values=list_name,font=("Bricolage Grotesque",18,"bold"),textvariable=city_name)
result.place(x=25,y=120,height=50,width=450)

#label 1 on left
weather_lable = Label(window, text="Weather Climate",font=("Bricolage Grotesque",15))
weather_lable.place(x=25,y=260,height=50,width=210)
#label 1 on right
weather_lable1 = Label(window, text="",font=("Bricolage Grotesque",20))
weather_lable1.place(x=250,y=260,height=50,width=210)
#label 2 on left
weather_dis_lable = Label(window, text="Weather Description",font=("Bricolage Grotesque",15))
weather_dis_lable.place(x=25,y=330,height=50,width=210)
#label 1 on right
weather_dis_lable1 = Label(window, text="",font=("Bricolage Grotesque",15))
weather_dis_lable1.place(x=250,y=330,height=50,width=210)
#label 1 on left
temperature_lable = Label(window, text="Temperature",font=("Bricolage Grotesque",15))
temperature_lable.place(x=25,y=400,height=50,width=210)
#label 1 on right
temperature_lable1 = Label(window, text="",font=("Bricolage Grotesque",15))
temperature_lable1.place(x=250,y=400,height=50,width=210)


#label 1 on left
pressure_lable = Label(window, text="Pressure",font=("Bricolage Grotesque",15))
pressure_lable.place(x=25,y=470,height=50,width=210)
#label 1 on right
pressure_lable1 = Label(window, text="",font=("Bricolage Grotesque",15))
pressure_lable1.place(x=250,y=470,height=50,width=210)





#button creation
done_button = Button(window, text="Done",font=("Bricolage Grotesque",18,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)


window.mainloop()















