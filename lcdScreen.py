from gpiozero import Button
import time
from rpi_lcd import LCD

lcd = LCD(address=0x27)

class Page:
  def __init__(self, carName, carBrand, time):
    self.carName = carName
    self.carBrand = carBrand
    self.time = time

  def display(self):
    pass
  
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

    
