import pyautogui
import time
import os
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

pyautogui.printInfo("Weather forecast for tomorrow")
pyautogui.press('enter')
pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://en.ilmatieteenlaitos.fi/')
pyautogui.press('enter')

pyautogui.moveTo(200, 550)  # Move the mouse to a specific position (adjust coordinates as needed)
pyautogui.leftClick()  # Click to focus on the search bar

screenshot = pyautogui.screenshot()
screenshot.save(f'weather_forecast_{timestamp}.png')

pyautogui.moveTo(800, 700)  # Move the mouse to a specific position (adjust coordinates as needed)
pyautogui.rightClick()  # Right-click to open the context menu
pyautogui.moveTo(850, 825)  # Move the mouse to a specific position (adjust coordinates as needed)
pyautogui.leftClick()  # Click to select the weather forecast section

#open xlsx and save the copied image
pyautogui.hotkey('win', 'r')
time.sleep(2)
pyautogui.write('excel')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)  # Wait for Excel to open

pyautogui.moveTo(300, 300)  # Move the mouse to a specific position (adjust coordinates as needed)
pyautogui.leftClick()  # Click to focus on the Excel window
time.sleep(2)


pyautogui.hotkey('ctrl', 'Home')
time.sleep(0.5)
pyautogui.click(100,84)
pyautogui.write(f'Today: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
pyautogui.press('enter')
pyautogui.write('Weather Forecast for Tomorrow')
time.sleep(3)
pyautogui.press('down') 
pyautogui.press('down')

pyautogui.hotkey('ctrl', 'v')  # Paste the copied image into Excel  
time.sleep(1)

pyautogui.hotkey('ctrl', 'g')           # Click Name Box (top-left cell reference box)
time.sleep(1)
pyautogui.write('A39')
pyautogui.press('enter')
time.sleep(0.5)

pyautogui.write('Weather forecast fetched from the Finnish Meteorological Institute website')
pyautogui.press('enter')    # Press Enter to save the file
time.sleep(1)

script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, f"weather_forecast_{timestamp}.xlsx")

pyautogui.press("f12")          # Save As in Excel
time.sleep(2)
pyautogui.write(save_path, interval=0.01)
pyautogui.press("enter")
pyautogui.alert(f'Weather forecast saved successfully as weather_forecast_{timestamp}.xlsx') 