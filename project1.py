#Filename: project1.py
#Author: Adam Lech 
#PID: 9056-63663
#Class: CS 1124 , Spring 2011
#Virginia Tech 
#Purpose: This program will transfer , a part of picture containing a person , who is set against uniform background color, into
#a larger picture which would serve as a scene. This project was a fun way to learn hierarchical decomposiion and added new skill 
# in manipulating digital media. 

def driver():  . 
  chromaColor = makeColor(9,121,38) 
  chromaKey = makePicture('C:\\Users\\Adam\\Pictures\\chromaKey.jpg') 
  
  scene = makePicture('C:\\Users\\Adam\\Documents\\CS 1124\\Miscellenous\\1921Yankees.jpg') 
 
  offsetValue = 65 
  mask = makeMask(chromaKey, chromaColor, offsetValue) 
  grayscalePicture(chromaKey) 
  chroma = scalePictureProportional(chromaKey, 170)  
  mask = scalePictureProportional(mask , 170) 
  newPic =   placeInPictChromaKey(scene, chroma, mask, 600,170)
   
  return newPic 




def makeMask(chromaKey, chromaColor, offsetValue):
  mask = duplicatePicture(chromaKey) 
  for pixels in getPixels(mask): 
    if distance(makeColor(getRed(pixels),getGreen(pixels),getBlue(pixels)),chromaColor)>offsetValue: 
      setColor(pixels,white) 
    else: 
      setColor(pixels,black) 
  return mask 



def scalePictureProportional(picture, newWidth):
  factor = newWidth/float(getWidth(picture))  
  
  newHeight = getHeight(picture) * factor   
  
  source = picture 
  target = makeEmptyPicture(newWidth,int(newHeight)) 
  
  sourceX = 0 # creates X index variable 
  for x in range(0, getWidth(target)):# starts loop which will copy x-wise pixeels into scaled picture 
    sourceY = 0 #starts Y index variable
    
    for y in range(0, getHeight(target) ): #starts nested loop which will copy y-wise  pixels into scaled picture
      
      color = getColor(getPixel(source,int(sourceX),int(sourceY))) # gets pictures color for copying 
      
      sourceY = sourceY + 1/factor #adds new value to the Y index variable 
      
      
      setColor(getPixel(target,x,y),color) #sets color in the scaled picture pixel 
    sourceX = sourceX + 1/factor   # adds another variable to X index variable 
  
  return target #returns target as function's value 
  
  
def grayscalePicture(picture): #creates a gray picture 
  
  for p in getPixels(picture): #starts loop which will turn picture into gray
    newRed = getRed(p) 
    newGreen = getGreen(p) 
    newBlue = getBlue(p) 
    luminance = (newRed + newGreen + newBlue)/3 # creates gray value
    setColor(p,makeColor(luminance, luminance, luminance)) #sets color picture's pixel into gray 
  return picture
  
  
def placeInPictChromaKey(scene, chromaKey, maskPict, arealeft, areatop): #defining function which will actually copy  a part of picture with a person into scene 
  newScene = duplicatePicture(scene) #creates a  new picture with scene duplicate , in order to copy part of chromaKey picture
  if getHeight(chromaKey) + areatop< getHeight(scene): #conditional statement which will set the height of the copied chromaKey picture in case its height extends beyond the bottom line of scene
    distanceVertical = areatop + getHeight (chromaKey) #sets the distance to deteremine pixel position where the copying of the chromaKey picture should start 
  else:   #part of conditional statement which will set the height of the picture if its height doesn't extend beyond bottom of the picture 
    distanceVertical = getHeight(scene)  
  if getWidth(chromaKey) + arealeft< getWidth(scene):  #conditional statement which will set the width of the copied chromaKey picture in case its width extends beyond the right line of scene
    distanceHorizontal = arealeft + getWidth(chromaKey) #sets the distance to deteremine pixel position where the copying of the chromaKey picture should start 
  else: #part of conditional statement which will set the width of the picture if its width doesn't extend beyond right line  of the picture 
    distanceHorizontal  = getWidth(scene) 
    
 
  maskX = 0 #starts X index variable for recalling values of maskPiture pixels values 
  for x in range(arealeft, distanceHorizontal ): # starts loop in x-wise direction , at the pixel x-coordinates where we want to copy chromaKey pixel 
    
    maskY  = 0  #starts Y index variable for recalling values of maskPixtures pixels values
    for y in range(areatop , distanceVertical): #starts loop in  y-wise direction, at the pixel y-coordinate where we want to copy chromaKey pixel 
      colorMask = getColor(getPixel(maskPict,maskX,maskY) ) #obtains the value of the pixel in the maskPicture which will be either white or black 
      if colorMask == white:  #starts conditional statement, in order to transfer only those  pixels into the scene , which represent the person/figure we want to copy
        colorChroma = getColor(getPixel(chromaKey,maskX,maskY)) #obtains the value of pixel colors from chromaKey pictures 
        setColor(getPixel(newScene,x,y),colorChroma) #sets the pixel color on the scene picture to that of chromaKey picture representing person/figure
      maskY = maskY + 1 #adds value to the  Y index variable 
    
    maskX = maskX + 1 # ands value to the X index variable 
  
  return newScene  #assigns the outcome  to the function 
  
      
    