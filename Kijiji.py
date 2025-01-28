#all these are installed from pip at 32bit location
#python 3.7 script
from PIL import ImageGrab, Image, ImageDraw
import os
import time
import win32api, win32con #pywin32
import pyautogui
import pydirectinput
import webbrowser
import pyodbc
import extcolors
from datetime import datetime


# Globals
# ------------------ 
x_pad = 0#-14 # Using 3840x2160 at 125% zoom so use pads to for other res
y_pad = 0#-35
x_coded_res = 3840
y_coded_res = 2160
zoom_coded_res = 100
x_res = x_coded_res#3440
y_res = y_coded_res#1440
zoom_res = 100
error_reset = False

def screenGrab():
    box = (x_pad+1, y_pad+1, 1920,1080)
    #box = ()
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print ("Click.")          #completely optional. But nice for debugging purposes.
    time.sleep(.4)

def leftclickFast():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)

def mousePos(cord):
    win32api.SetCursorPos((x_pad+int(cord[0]*(x_res/x_coded_res)*(zoom_res/zoom_coded_res)), y_pad+int(cord[1]*(y_res/y_coded_res)*(zoom_res/zoom_coded_res))))
    
def loop_get_cords():
    while(1):
        x,y = win32api.GetCursorPos()
        #x = x - x_pad
        #y = y - y_pad
        print (x,y)
        time.sleep(0.5)
  
def get_cords():
    x,y = win32api.GetCursorPos()
    #x = x - x_pad
    #y = y - y_pad
    print (x,y)

def return_cords():
    x,y = win32api.GetCursorPos()
    #x = x - x_pad
    #y = y - y_pad
    return x, y

def start():
    #location of first menu
    mousePos((182, 225))
    leftClick()
    time.sleep(.1)

def open_link(start_index=0, count=19):
    chrome_path = 'C:/Program Files/Google/Chrome Dev/Application/chrome.exe %s'
    search_terms = "blue"
    
    counter = 1
    #search_dir = "C:\\Users\\{username}\\Downloads\\New folder\\New folder"
    search_dir = "D:\\{username}\\{username}old\\New folder\\New folder (2)\\pi)New folder (37)"
    #files = os.listdir(search_dir)
    #files.sort(key=lambda x: os.path.getmtime(os.path.join(search_dir, x)))
    with open('C:/Users/{username}/Downloads/guru99_c2.txt', encoding="utf8") as f:
        files = f.readlines()
    
    for filename in reversed(files):
        time.sleep(0.25)
        if counter >= start_index:
            print(filename)
            #url = "https://www.google.com.tr/search?q={}".format(filename)
            url = "https://www.google.com.tr/search?tbm=isch&q={}".format(filename)
            webbrowser.get(chrome_path).open_new_tab(url)
        counter+=1
        if counter-start_index > count:
            break
def filename_to_txt(start_index=0):
    counter = 1
    search_dir = "D:\\{username}\\{username}old\\New folder\\New folder (2)\\pi)New folder (37)"
    files = os.listdir(search_dir)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(search_dir, x)))
    f= open("guru99_c2.txt","w+")
    for filename in (files):
        if counter >= start_index:
            print(filename)
            #f.write("%s\n" % (filename))
        counter+=1
    f.close()
    print(counter)
def keyboard():
    pyautogui.keyDown("alt")
    time.sleep(.1)
    pyautogui.press("tab")
    time.sleep(.1)
    pyautogui.press("tab")
    time.sleep(.1)
    #pyautogui.press("tab")
    pyautogui.keyUp("alt")
    try:
        while True:
            pyautogui.scroll(-10000)
    except KeyboardInterrupt:
        pass

def ww():
    for x in range(2,10):
        get_cords()
        y=6
        mousePos((3458, 676+y*70))
        leftClick()
        mousePos((3484, 788+y*70))
        leftClick()
        pyautogui.keyDown("ctrl")
        time.sleep(.1)
        pyautogui.press("1")
        time.sleep(.1)
        pyautogui.keyUp("ctrl")
        time.sleep(.3)
        mousePos((3592, 673+y*70))
        leftClick()
        time.sleep(.3)
        mousePos((4988, 1285))
        leftClick()
        time.sleep(3)
        mousePos((4816, 510))
        leftClick()
        time.sleep(.3)
        pyautogui.keyDown("ctrl")
        time.sleep(.1)
        pyautogui.press("2")
        time.sleep(.1)
        pyautogui.keyUp("ctrl")
        time.sleep(.5)
        pyautogui.press("F5")
        time.sleep(.3)
        pyautogui.press("Enter")
        time.sleep(.3)
        pyautogui.keyDown("ctrl")
        time.sleep(.1)
        pyautogui.press("1")
        time.sleep(.1)
        pyautogui.keyUp("ctrl")

def whatsapp_broadcast_all_contacts():
    #4k screen, samsung dex full on s20 fe 5g, whatsapp on left side of screen

    #first start broadcast page
    #mousePos((1865, 128))
    #leftClick()
    #time.sleep(0.5)
    #mousePos((1650, 225))
    #leftClick()
    #time.sleep(0.5)

    #search button, nvm manually locate first text
    #mousePos((1855, 129))

    #select contacts
    count = 0
    
    while(count < 243):
        count2 = 0
        while(count2 < 13):
            r1,g1,b1 = return_color(110,477+count2*128)
            if r1 >= 245 and g1 >= 245 and b1 >= 245:
                mousePos((823, 427+count2*128))
                leftclickFast()    
            count2 += 1
            time.sleep(0.08)
            
        count += 13
        count2 = 0
        while(count2 < 13):
            pyautogui.scroll(-1000)
            time.sleep(0.05)
            count2 += 1
        time.sleep(0.2)
    
        
def loop_till_pixel_change(x,y,r1=256,g1=256,b1=256, maxt=15): #maxt in seconds
    x = x_pad+int(x*(x_res/x_coded_res))
    y = y_pad+int(y*(y_res/y_coded_res))
    if r1==256 or g1==256 or b1==256:
        s = screenGrab()
        (r1,g1,b1) = s.getpixel((x,y))
    loop = 1
    loopCounter=0
    global error_reset
    while(loop):
        s = screenGrab()
        (r2,g2,b2) = s.getpixel((x,y))
        if (r2==r1 and g2==g1 and b2==b1):
            time.sleep(0.2)
        else:
            loop = 0

        loopCounter = loopCounter + 1
        if loopCounter*0.2 >= maxt:
            loop=0
            #check if on kijiji file history page
            (r2,g2,b2) = s.getpixel((714,1245))
            if (r2==18 and g2==18 and b2==18):
                pyautogui.hotkey('ctrl', 'l')
                time.sleep(0.2)
                input("STUCK")
                pyautogui.typewrite('kijiji.ca')
                time.sleep(0.2)
                pyautogui.press("enter")
                time.sleep(0.5)
                print("Went to kijij.ca)")
                error_reset = True

def loop_till_pixel_reach(x,y,r1,g1,b1,maxt=15):
    x = x_pad+int(x*(x_res/x_coded_res))
    y = y_pad+int(y*(y_res/y_coded_res))
    loop = 1
    loopCounter=0
    while(loop):
        s = screenGrab()
        (r2,g2,b2) = s.getpixel((x,y))
        if (r2==r1 and g2==g1 and b2==b1):
            loop = 0
        else:
            time.sleep(0.2)

        loopCounter = loopCounter + 1
        if loopCounter*0.2 >= maxt:
            loop=0


def loop_get_color():
    while(1):
        s = screenGrab()
        x, y = return_cords()
        (r1,g1,b1) = s.getpixel((x,y)) 
        print("Color: " + str(r1) + " " + str(g1) + " " + str(b1))
        time.sleep(0.5)

def get_color(x=-1,y=-1):
    s = screenGrab()
    if x==-1 or y==-1:
        x, y = return_cords()
    (r1,g1,b1) = s.getpixel((x,y)) 
    print("Color: " + str(r1) + " " + str(g1) + " " + str(b1))

def return_color(x=-1, y=-1):
    s = screenGrab()
    if x==-1 or y==-1:
        x, y = return_cords()
    x = x_pad+int(x*(x_res/x_coded_res))
    y = y_pad+int(y*(y_res/y_coded_res))
    (r1,g1,b1) = s.getpixel((x,y))
    return r1, g1, b1

def kijiji_delete(count=10,skipAd=0,account='Me'):
    #4k screen 100% chrome zoom, kijiji open on left side
    
    #s = screenGrab()
    #(r1,g1,b1) = s.getpixel((935,480)) #loading button
    #print("White Color: " + str(r1) + " " + str(g1) + " " + str(b1))

    #goto my ads
    mousePos((1594, 198)) #click account
    leftClick()
    time.sleep(0.5)
    #mousePos((1480, 275)) #click myads
    pyautogui.press("tab")
    time.sleep(0.2)
    r1,g1,b1 = return_color(808,466)
    pyautogui.press("enter")
    loop_till_pixel_change(808,466,r1,g1,b1,maxt=8)
    time.sleep(3) 
    
    if count >= 100:
        search_dir = "C:/Users/{username}/Downloads/Kijiji/Kijiji Ad Descriptions/"
        if account == 'R':
            search_dir = 'C:/Users/{username}/Downloads/Kijiji/Kijiji Ad Descriptions R/'
        files = os.listdir(search_dir)
        count = len(files)
    if skipAd > 0:
        count = count - 1
    print("Deleting Ads: " + str(count))
    for x in range(0,count):
        mousePos((529, 881)) #y=974 if kijiji app download now at top
        
        if skipAd != 0 and x >= skipAd-1:
            mousePos((529, 881+172*skipAd))
        leftClick()
        time.sleep(0.25)
        mousePos((960, 1208-25+25))
        leftClick()
        time.sleep(0.25)

        mousePos((948, 1333-25+25))
        leftClick()
        time.sleep(0.5)
        
        loop_till_pixel_reach(960,1320-25+25,255,255,255) #till success window
        time.sleep(1)

        r1,g1,b1 = return_color(951, 1073)
        if 80 < r1 < 90 and 185 < g1 < 200 and 115 < b1 < 130:
            print("Success Deleted: " + str(x+1))
            mousePos((1189, 856-25+25)) #x button
        else:
            skipAd += 1
            print("Fail Deleted, skipAd= :" +str(skipAd))
            time.sleep(1)
            mousePos((1213, 849)) #x button
        
        leftClick()
        time.sleep(0.5)
        
def kijiji(onlyNewDir=0, addS=0, somethingDownloaded=0, start_index=0, end_index=100, account='Me', username='default'):
    #4k screen 100% chrome zoom, kijiji open on left side
    if onlyNewDir == 1:
        search_dir = 'C:/Users/{username}/Downloads/Kijiji/Kijiji ad new'
    else:
        search_dir = 'C:/Users/{username}/Downloads/Kijiji/Kijiji Ad Descriptions/'
    if account == 'R':
        search_dir = 'C:/Users/{username}/Downloads/Kijiji/Kijiji Ad Descriptions R/'
    files = os.listdir(search_dir)
    files.sort
    adNames = sorted(files)
    #4k screen
    #Open my ads
    #mousePos((1574, 202))
    #leftClick()
    #mousePos((1497, 267))
    #leftClick()
    #time.sleep(2)
    endIndex = end_index
    if end_index == 100:
        endIndex = len(adNames)
    for index in range(start_index,endIndex):
        print(index, ": ", adNames[index])
    index = start_index
    while index < endIndex:
        #Post Ad
        x1 = 0
        x2 = 0
        x3 = 0
        xBrandOffset = 0
        xCarrierOffset = 0
        xForSaleByBusiness = 0
        xFulfillmentOptions = 0
        longerdescription = 0
        pleaseContactPrice = 0
        xTags = 0
        num_of_pics = 1
        rental_property = 0 #rental variables
        change_location = 0
        default_category_option = 1
        descYCord = 1284 #Changes when too many new ad details like brand, etc are add
        if adNames[index] == "6000mAh Power Bank Micro + Apple Lightning Cable + Wireless":
            AdCost = '5'
            num_of_pics = 5
        elif adNames[index] == "Twin Size Bed":
            AdCost = '70'
        
        elif adNames[index] == "Black Tile Stands x5":
            AdCost = '15'
            x1 = 3
            x2 = 8
            x3 = 4
            num_of_pics = 4
        elif adNames[index] == "IPhone 12 White 64gb BNIB Sealed":
            AdCost = '750'
            xBrandOffset = 1 #Apple Brand
            xCarrierOffset = 1 #Unlocked Carrier
            descYCord = 1433
            num_of_pics = 3
        elif adNames[index] == "IPhone 12 Purple 64gb":
            AdCost = '550'
            #xBrandOffset = 1 #Apple Brand
            #xCarrierOffset = 1 #Unlocked Carrier
            #descYCord = 1433
            num_of_pics = 2
        elif adNames[index] == "Microsoft Surface Pro 6 i7 16gb 512gb SSD Laptop":
            AdCost = '1100'
            xBrandOffset = 12 #Other/Microsoft Brand
            xCarrierOffset = 1 # Screen size under 14
            descYCord = 1400
            num_of_pics = 5
        
        elif adNames[index] == "2 Bedroom 2 Bath Condo in Kitchener Downtown":
            AdCost = '2300'
            num_of_pics = 7
            rental_property = 2
            num_bedrooms = 2
            bathroom_offset = 3
            move_in_date = "03/01/2023"
            rental_size = "765"
            laundry_in_unit = 1
            laundry_in_building = 0
            dishwasher = 1
            fridge = 1
            space_yard = 1
            space_balcony = 1
            not_gym = 0
            pool = 1
            concierge = 1
            twenty_four_hour_security = 1
            bicycle_parking = 1
            storage_space = 1
            elevator_in_building = 1
            hydro_included = 0
            heat_included = 1
            water_included = 1
            cable_included = 0
            internet_included = 0
            num_of_parking = 1
            change_location = 1
            change_location_address = "60 Frederick Street" #unit 1107
            descYCord = 1854
        

        #click post and enter name
        r1,g1,b1 = return_color(1082,515)
        mousePos((1679, 200))
        leftClick()
        loop_till_pixel_change(1082,515,r1,g1,b1)
        time.sleep(0.7)
        r1,g1,b1 = return_color(1082,1489)
        if addS == 3:
            addS = datetime.today().weekday() % 3
        if addS==1:
            pyautogui.typewrite(adNames[index] + " ~")
            if index == 0:
                print("~")
        elif addS==2:
            pyautogui.typewrite(adNames[index] + " ~~")
            if index == 0:
                print("~~")
        else:
            pyautogui.typewrite(adNames[index])
        print(str(index+1) + "/" + str(endIndex) + ": " + adNames[index])
        #time.sleep(1)
        pyautogui.press("enter") #pressed next/updated
        #mousePos((1082,1015))
        loop_till_pixel_change(1082,1489,r1,g1,b1,5)
        time.sleep(1)
        #Change the category for some specific ones
        if x1 != 0:
            for x in range(0,x1):
                pyautogui.press("tab")
                time.sleep(0.05)
            pyautogui.press("enter")
            time.sleep(1)
        if x2 != 0:
            for x in range(0,x2):
                pyautogui.press("tab")
                time.sleep(0.05)
            pyautogui.press("enter")
            time.sleep(1)
        if x3 != 0:
            for x in range(0,x3):
                pyautogui.press("tab")
                time.sleep(0.05)
            y_cat=1565

        #else go to first category
        if x1==0 and x2==0 and x3==0:
            pyautogui.press("tab")
            time.sleep(0.1)
            for x in range(0,default_category_option-1):
                pyautogui.press("tab")
                time.sleep(0.05)
            y_cat=2045
            #y_cat=1015

        #finish ad name section
        r1,g1,b1 = return_color(1082,y_cat)
        pyautogui.press("enter")
        loop_till_pixel_change(1082,y_cat,r1,g1,b1)
        time.sleep(2)

        # Change brand for some specific ones
        if xBrandOffset != 0:
            mousePos((589, 722))
            leftClick()
            time.sleep(0.5)
            for x in range(0,xBrandOffset):
                pyautogui.press("down")
                time.sleep(0.05)
            pyautogui.press("enter")
            time.sleep(0.5)

        # Change carrier for some specific ones
        if xCarrierOffset != 0:
            mousePos((589, 1022))
            leftClick()
            time.sleep(0.5)
            for x in range(0,xCarrierOffset):
                pyautogui.press("down")
                time.sleep(0.05)
            pyautogui.press("enter")
            time.sleep(0.5)

        # For rentals (maybe long term rentals only), rental 1 = apartment, 2 = condo, 3 = basement, etc
        if rental_property > 0:
            mousePos((470, 993+(rental_property-1)*34)) #unit type
            leftClick()
            time.sleep(0.2)
            mousePos((470, 1509)) #agreement type, month-to-month default, do this first cuz tab doesnt work later
            leftClick()
            time.sleep(0.2)
            mousePos((470, 1865)) #pet friendly limited default, do this first cuz tab doesnt work later
            leftClick()
            time.sleep(0.2)
            mousePos((470, 1280)) #bedrooms
            leftClick()
            time.sleep(0.5)
            for x in range(0,num_bedrooms*2):
                pydirectinput.press("down")
                time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.press("tab") #bathroom
            time.sleep(0.1)
            for x in range(0,bathroom_offset):
                pydirectinput.press("down")
                time.sleep(0.1)
            pyautogui.press("tab") #move-in-date
            time.sleep(0.1)
            pyautogui.typewrite(move_in_date)
            time.sleep(0.2)
            pyautogui.press("tab") #size
            time.sleep(0.1)
            pyautogui.typewrite(rental_size)
            time.sleep(0.2)
            pyautogui.press("tab") #appliances, page gets scrolled btw
            time.sleep(0.1)
            if laundry_in_unit:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if laundry_in_building:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if dishwasher:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if fridge:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") #personal outdoor space
            time.sleep(0.1)
            if space_yard:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if space_balcony:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            
            mousePos((470, 1365)) #air conditioning
            leftClick()
            time.sleep(0.2)
            mousePos((470, 1696)) #smoking no
            leftClick()
            time.sleep(0.2)
            mousePos((470, 1027)) #furnished
            leftClick()
            time.sleep(0.2)

            mousePos((470, 1844)) #building amenities
            leftClick()
            time.sleep(0.2)
            if not_gym:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if pool:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if concierge:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if twenty_four_hour_security:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if bicycle_parking:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if storage_space:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if elevator_in_building:
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if hydro_included: #utilities
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if heat_included: 
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if water_included: 
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if cable_included:  #wifi and more
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") 
            time.sleep(0.1)
            if internet_included: 
                pyautogui.press("space")
                time.sleep(0.1)
            pyautogui.press("tab") #parking 
            time.sleep(0.1)
            for x in range(0,num_of_parking+1):
                pydirectinput.press("down")
                time.sleep(0.1)

            mousePos((470, 1025)) #accessibility features, no
            leftClick()
            time.sleep(0.2)
            
            
            
        #Change For Sale By
        if xForSaleByBusiness != 0:
            mousePos((481, 746))
            leftClick()
            time.sleep(0.5)

        #Add Fulfillment options, Payment, Condition
        if xFulfillmentOptions != 0:
            mousePos((479, 784))
            leftClick()
            time.sleep(0.1)
            for x in range(0,4):
                pyautogui.press("tab")
                time.sleep(0.1)
                pyautogui.press("tab")
                time.sleep(0.1)
                pyautogui.press("space")
                time.sleep(0.2)
            pyautogui.press("tab")
            time.sleep(0.1)
            pydirectinput.press("down")
            time.sleep(0.2)
            

        #enter tags
        for x in range(0,xTags):
            mousePos((545, 1504))
            leftClick()
            time.sleep(0.2)
            pyautogui.typewrite(Tags[x])
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.2)
            
        
        #enter description and pictures
        mousePos((507, descYCord))
        leftClick()
        with open(search_dir+adNames[index]+'/'+adNames[index]+'.txt', encoding="utf8") as f:
            files = f.readlines()
        time.sleep(0.5)
        #print(files)
        if longerdescription == 2: #typewrite not working
            pyautogui.press("win")
            time.sleep(0.2)
            pyautogui.typewrite("notep")
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'n')
            time.sleep(0.5)
            pyautogui.typewrite(''.join(files))
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'x')
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'p')
            time.sleep(0.5)
        elif longerdescription == 3:
            string = ''.join(files)
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            pyautogui.typewrite(firstpart)
            time.sleep(1)
            pyautogui.typewrite(secondpart)
            time.sleep(1)
        elif longerdescription == 1:
            pyautogui.typewrite(''.join(files))
            time.sleep(15)
        else:
            pyautogui.typewrite(''.join(files))
            time.sleep(3)
        
        

        pyautogui.press("tab")
        time.sleep(0.2)
        pyautogui.press("tab")
        time.sleep(0.2)
        pyautogui.press("tab")
        time.sleep(0.2)
        for x in range(0,xTags-1):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(2)
        

        #choose pictures
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.5)

        pyautogui.typewrite(search_dir+adNames[index])
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.4)
        pyautogui.press("tab")
        time.sleep(0.1)
        pyautogui.press("tab")
        time.sleep(0.1)
        pyautogui.press("tab")
        time.sleep(0.1)

        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.25)

        pyautogui.press("enter")
        time.sleep(1)

        if num_of_pics > 6: #wait_for_pic
            xcord = 308+210*((num_of_pics-1)%6)
            ycord = 689+238
        else:
            xcord = 308+210*(num_of_pics-1)
            ycord = 689
        r1,g1,b1 = return_color(xcord,ycord)

        #price
        count = 10
        if xTags > 0:
            count-=1
        if num_of_pics == 10:
            count -= 1
        for x in range(0,count):
            if count - x == 5 and change_location:
                pydirectinput.press("space")
                time.sleep(0.1)
                pyautogui.typewrite(change_location_address)
                time.sleep(1)
                pydirectinput.press("down")
                time.sleep(0.2)
                pydirectinput.press("enter")
                time.sleep(3)
                for y in range(0,6): #google maps needs to be tabbed
                    pyautogui.press("tab")
                    time.sleep(0.1)
            pyautogui.press("tab")
            time.sleep(0.2)
        if pleaseContactPrice == 1:
            for x in range(0,2):
                pydirectinput.press("down")
                time.sleep(0.2)
        else:
            pyautogui.press("tab")
            time.sleep(0.2)
            pyautogui.typewrite(AdCost)

        #Wait for images
        loop_till_pixel_change(xcord,ycord,r1,g1,b1,10)

        if rental_property > 0: #change ad to lite
            pyautogui.press("tab")
            time.sleep(0.1)
            pyautogui.press("tab")
            time.sleep(0.1)
            pydirectinput.press("space")
            time.sleep(0.1)
        
        pyautogui.scroll(-5000) #post
        time.sleep(2)

        if somethingDownloaded == 1:
            mousePos((256, 1300)) #When something downloaded
        else:
           mousePos((256, 1368)) 
        r1,g1,b1 = return_color(1082,439)
        leftClick()
        loop_till_pixel_change(1082,439,r1,g1,b1)
        time.sleep(1)
        f.close()
        index += 1
        global error_reset #if went back to kijiji.ca due to error
        if error_reset == True:
            index -= 1
            error_reset = False
def switchKijijiAccountTo(account, accloggedin=1):
    if accloggedin == 1:
        mousePos((1548, 198)) #click account
        leftClick()
        time.sleep(0.5)
        mousePos((1507, 642)) #click logout
        r1,g1,b1 = return_color(1784, 331)
        leftClick()
        loop_till_pixel_change(1784, 331,r1,g1,b1)
        time.sleep(2) 
    mousePos((1555, 203)) #click signin
    r1,g1,b1 = return_color(1784, 564)
    leftClick()
    loop_till_pixel_change(1784, 564,r1,g1,b1)
    time.sleep(2) 
    
    mousePos((478, 426)) #click email
    leftClick()
    leftClick()
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(.2)
    pydirectinput.press("backspace")
    time.sleep(0.1)

    if account == "R": #enter account
        pyautogui.typewrite("R")
        time.sleep(0.2)
    elif account == "Me":
        pyautogui.typewrite("Viv")
        time.sleep(0.2)
    else:
        input("account problem")
    pydirectinput.press("down")
    time.sleep(0.5)
    pydirectinput.press("enter")
    time.sleep(0.2)
    pyautogui.press("tab") #keep signed in
    time.sleep(.1)
    pyautogui.press("tab") 
    time.sleep(.1)
    pyautogui.press("space")
    time.sleep(.2)
    pyautogui.press("tab") 
    time.sleep(.1)
    pyautogui.press("tab") 
    time.sleep(0.1) 
    r1,g1,b1 = return_color(1653,1519)
    pyautogui.press("enter")
    loop_till_pixel_change(1653,1519,r1,g1,b1)
    time.sleep(2) 
    

def test(username = ''):
    time.sleep(2)
    search_dir = "C:/Users/{username}/Downloads/Kijiji/Kijiji Ad Descriptions/"
    files = os.listdir(search_dir)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(search_dir, x)))
    print(files)
    #print(files[3])
    print(len(files))
    search_dir = "C:/Users/{username}/Downloads/Kijiji/Kijiji Ad Descriptions/"
    files = os.listdir(search_dir)
    files.sort
    adNames = sorted(files)
    index = 0
    print(adNames)
    with open('C:/Users/{username}/Downloads/Kijiji/Kijiji Ad Descriptions/'+adNames[index]+'/'+adNames[index]+'.txt', encoding="utf8") as f:
        files = f.readlines()
        
    time.sleep(0.5)
    print(files)
    for index in range(0,0):
        print(index)



def main():
    get_cords()
    mousePos((1679, 200))
    print (datetime.today().weekday() % 3)
    #whatsapp_broadcast_all_contacts()
    #loop_get_cords()
    #premiere_pro_copy_paste()

    #kijiji_delete(100,0, 'R') #num of ads, num of skip ads
    #kijiji(0,3,0,0,100,'R')
    #switchKijijiAccountTo("Me", 1) #0 if no acc logged in
    
    kijiji_delete(100,0, 'Me') #num of ads, num of skip ads
    kijiji(0,3,0,0,100,'Me') # onlyNewDir=0, add~=0, somethingDownloaded=0, start_index=0, end_index=100
    #switchKijijiAccountTo("R", 1) #0 if no acc logged in

    
    
    
    
    
    #test()
    #open_link(190)
    #open_link(570)get

    #s = screenGrab()
    #colors_x = extcolors.extract_from_image(s, tolerance=32)
    #print (colors_x)
 
if __name__ == '__main__':
    main()

def cordDictionary(cord_type):
    if cord_type == "post_button":
        if x_res == 3840 and y_res == 2160 and zoom_res == 125:
            return (256, 1368)
        elif x_res == 3840 and y_res == 2160 and zoom_res == 100:
            return (255, 1582)
        
