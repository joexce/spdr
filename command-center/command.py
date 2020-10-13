import requests
import logging as log
import curses
import sys
import npyscreen
from prettytable import PrettyTable

# x = PrettyTable()
# x.field_names = ["Probe", "LatLong"]


class menu(npyscreen.FormBaseNew):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        y, x = self.useable_space()
        self.humidity = self.add(npyscreen.BoxTitle, name="HUMIDITY", relx=1, max_width=80, rely=2, max_height=20)
        self.altitude = self.add(npyscreen.BoxTitle, name="ALTITUDE",rely=2, relx=(x // 5) + 45, max_height=20)
        self.signal = self.add(npyscreen.BoxTitle, name="SIGNAL",value=0, relx=1, max_width=x // 5,
                                      max_height=0, rely=-29)
        self.logs = self.add(npyscreen.BoxTitle, name="LOGS", relx=(x // 5) + 1, rely=-29)

    def get_data(self,event):
        self.humidity.value = "tes"
        self.humidity.display()


class App(npyscreen.NPSAppManaged):
   def onStart(self):
       
       npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
       self.addForm('MAIN', menu, name='SYSTEM POSITIONING & DATA RECIEVER')
       # A real application might define more forms here.......

if __name__ == '__main__':
   app = App().run()
def getData():
    print("asd")
# url = 'http://localhost:5000/'

# def getRequest():
#     try:
#         request = requests.get(url+"status")
#         data = request.json()
#         print("Data response ", data)
#     except:
#         log.error("Connection failed")

# getRequest()