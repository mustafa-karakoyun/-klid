# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:34:35 2024

@author: karak
"""

#Kütüphaneyi ekleyelim
import math

#Bize lazım olacak iki liste var girişte tanımladık
distances=[]
points=[(3,5),(4,7),(5,9)]

#Fonksiyonu oluşturduk
def euclideanDistance(p1,p2):
    
    x1,x2=p1
    y1,y2=p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance=euclideanDistance(points[i],points[j])
        distances.append(distance)
    

#En kısa mesafeyi yazdıralım
print("En kısa mesafe:",min(distances))
    