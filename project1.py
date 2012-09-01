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
  chromaKey = makePicture('chromaKey.jpg') 
  
  scene = makePicture('1921Yankees.jpg') 
 
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
  
  sourceX = 0 
  for x in range(0, getWidth(target)):
    sourceY = 0 
    
    for y in range(0, getHeight(target) ):
      
      color = getColor(getPixel(source,int(sourceX),int(sourceY)))  
      
      sourceY = sourceY + 1/factor 
      
      
      setColor(getPixel(target,x,y),color) 
    sourceX = sourceX + 1/factor   
  
  return target  
  
  
def grayscalePicture(picture): 
  
  for p in getPixels(picture): 
    newRed = getRed(p) 
    newGreen = getGreen(p) 
    newBlue = getBlue(p) 
    luminance = (newRed + newGreen + newBlue)/3 
    setColor(p,makeColor(luminance, luminance, luminance)) #sets color picture's pixel into gray 
  return picture
  
  
def placeInPictChromaKey(scene, chromaKey, maskPict, arealeft, areatop): 
  newScene = duplicatePicture(scene) 
  if getHeight(chromaKey) + areatop< getHeight(scene): 
    distanceVertical = areatop + getHeight (chromaKey) 
  else:   
    distanceVertical = getHeight(scene)  
  if getWidth(chromaKey) + arealeft< getWidth(scene): 
    distanceHorizontal = arealeft + getWidth(chromaKey) 
  else: 
    distanceHorizontal  = getWidth(scene) 
    
 
  maskX = 0
  for x in range(arealeft, distanceHorizontal ): 
    maskY  = 0  
    for y in range(areatop , distanceVertical): 
      colorMask = getColor(getPixel(maskPict,maskX,maskY) ) 
      if colorMask == white:  
        colorChroma = getColor(getPixel(chromaKey,maskX,maskY))
        setColor(getPixel(newScene,x,y),colorChroma) 
      maskY = maskY + 1
    
    maskX = maskX + 1 
  
  return newScene  
  
      
    