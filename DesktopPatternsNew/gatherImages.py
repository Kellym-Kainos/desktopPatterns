
#Imports
import urllib2
from PIL import Image
from bs4 import BeautifulSoup
import random
import re
import os

# -------- FUNCTIONS --------
# Function to check if URL is valid
# Returns valid number for url
def checkUrl(n):
    try :
		urllib2.urlopen("http://www.pttrns.com/p/"+`n`+"").read()
		print "N: "+`n`
		final = n
		return final
    except urllib2.HTTPError, e:
		newNum = random.randint(1,334)
		print "New Num: "+`newNum`
		newNum = checkUrl(newNum)
		return newNum

def drawOne(x,y):
    print "Draw One"
    background = Image.new('RGBA', (1280,800), (255, 255, 255, 255))
    bg_w,bg_h=background.size

    img= Image.open(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/background1.png','r')
    img_w, img_h = img.size

    offset=((bg_w-img_w)/2,(bg_h-img_h)/2)
    background.paste(img,offset)
    background.save(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/backgroundnew.png')
    background.save(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/backgroundnew1.png')

def drawTwo(x,y):
    print "Draw 2"
    background = Image.new('RGBA', (1280,800), (255, 255, 255, 255))
    bg_w,bg_h=background.size

    img= Image.open(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/background1.png','r')
    img_w, img_h = img.size
    offset=((bg_w-img_w)/4,(bg_h-img_h)/2)
    background.paste(img,offset)

    img2= Image.open(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/background2.png','r')
    img2_w, img2_h = img2.size
    offset=((3*(bg_w-img2_w))/4,(bg_h-img2_h)/2)
    background.paste(img2,offset)

    background.save(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/backgroundnew.png')
    background.save(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/backgroundnew1.png')

def drawThree(x,y):
    print "Draw 3"
    background = Image.new('RGBA', (1280,800), (255, 255, 255, 255))
    bg_w,bg_h=background.size

    img= Image.open(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/background1.png','r')
    img_w, img_h = img.size
    offset=((bg_w-img_w)/12,(bg_h-img_h)/2)
    background.paste(img,offset)
        
    img2= Image.open(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/background2.png','r')
    img2_w, img2_h = img2.size
    offset=((6*(bg_w-img2_w))/12,(bg_h-img2_h)/2)
    background.paste(img2,offset)

    img3= Image.open(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/background3.png','r')
    img3_w, img3_h = img3.size
    offset=((11*(bg_w-img3_w))/12,(bg_h-img3_h)/2)
    background.paste(img3,offset)
        
    background.save(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/backgroundnew.png')
    background.save(os.path.dirname(os.path.abspath(__file__))+'/backgrounds/backgroundnew1.png')

def saveImages(imgs, start, end):
    #Iterate through list and create new image.
    listIterator =[]
    listIterator [:] =  range(start, end)

    counter = 1
    for i in listIterator:
        print imgs[i]['src']
        url = imgs[i]['src']
        f = urllib2.urlopen(url)
        with open(os.path.dirname(os.path.abspath(__file__))+"/backgrounds/background"+`counter`+".png", "wb") as code:
            code.write(f.read())
        counter = 1 + counter
# ---------------------------

#Generate random number for URL and validate
randomNum = random.randint(1,334)
pageNum = checkUrl(randomNum)
print "Page num: "+`pageNum`

#Open URL and find all <img>
page = BeautifulSoup(urllib2.urlopen("http://www.pttrns.com/p/"+`pageNum`))
#imgs = page.findAll('img')
imgs =  page.findAll('img')
length = len(imgs)
print "Length: "+`length`

if (length > 4):
    picNum = random.randint(2,length-3)
    saveImages(imgs,picNum, picNum+3)
    drawThree(picNum, picNum+3)
else:
    if (length == 4):
        picNum = random.randint(2,length-2)
        saveImages(imgs,picNum, picNum+2)
        drawTwo(picNum, picNum+2)
    else:
        if (length == 3):
            picNum = random.randint(2,length-1)
            saveImages(imgs,picNum, picNum+1)
            drawOne(picNum,picNum+1)






