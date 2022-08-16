from ctypes import sizeof
import cv2
import numpy as np
import random
import math

NumberOfElementsInGen=11

img=cv2.imread("lebron.jpg",0)
count=0
for i in range (400):
    for j in range (400):
        if(img[i,j]<150):
            img[i,j]=0
            count+=1
        else:
            img[i,j]=255


cv2.namedWindow('Bron',cv2.WINDOW_NORMAL)
cv2.imshow('Bron',np.uint8(img))

print(img.shape)
print("Number of black pixels:",count)
randomlychosenimage=np.full((400,400),255).astype(np.uint8)

def dist(x1,y1,x2,y2):
    k1 = (x1 - x2) * (x1 - x2)
    k2 = (y1 - y2) * (y1 - y2)
    u = (k1+k2)     
    u=math.sqrt(u)
    return u



blackpixels=[]
while(len(blackpixels) <1000):      #sampling 1000 black pixerls from lot
    i=np.random.randint(0,400)
    j=np.random.randint(0,400)
    if(img[i,j]==0):
        blackpixels.append((i,j))
        randomlychosenimage[i][j]=0

gen1=[]
##creating the parent generation
for i in range (NumberOfElementsInGen):
    set=[]
    set=random.sample(blackpixels,1000)
    #print(set)
    gen1.append(set)

##get fitness factors for the generation
fittnessOfGeneration=[]
unsortedfittness=[]
for i in range (NumberOfElementsInGen):
    f=0
    for j in range (999):
        (x1,y1)=gen1[i][j]
        (x2,y2)=gen1[i][j+1]
        f+=dist(x1,y1,x2,y2)
    (x1,y1)=gen1[i][j+1]
    (x2,y2)=gen1[i][0]
    f+=dist(x1,y1,x2,y2)
    fittnessOfGeneration.append(f)
    unsortedfittness.append(f)
min=fittnessOfGeneration.index(min(fittnessOfGeneration))
fittnessOfGeneration.sort()
print(fittnessOfGeneration)

print(unsortedfittness)
print(min)

probabilityOfElements=[0 for i in range(NumberOfElementsInGen)]
count=NumberOfElementsInGen
for i in fittnessOfGeneration:
    index=unsortedfittness.index(i)
    #print(index)
    probabilityOfElements[index]=count/55
    count-=1

print(probabilityOfElements)
##set probability



gen2=[]
##always take the fittest element to the next generation
gen2.append(gen1[min])
for i in range (5):
    




cv2.namedWindow('BronSampled',cv2.WINDOW_NORMAL)
cv2.imshow('BronSampled',np.uint8(randomlychosenimage))   








cv2.waitKey(0)
cv2.destroyAllWindows()