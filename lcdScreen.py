from gpiozero import Button
import time
from rpi_lcd import LCD

lcd = LCD(address=0x27)

class Page:
  def __init__(self, carName, carBrand, time, date):
    self.carName = str(carName)
    self.carBrand = str(carBrand)
    self.time = str(time)
    self.date = str(date)

  def display(self):
    lcd.clear()
    lcd.text(f"{self.carName}, {self.carBrand}", 1)      # Current line on top
    lcd.text(self.date, 2)
  
class PageHandler:
  def __init__(self):
    self.pages = []
    self.button1 = Button(17)
    self.button2 = Button(22)
    self.pageNum = 0
  
  def update(self):
    pass

  def switch(dir):
    pass

    
