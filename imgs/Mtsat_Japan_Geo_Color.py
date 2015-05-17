#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
import os
import sys
import string
import arcgisscripting
import shutil
import sched, time

file = "Z:/SatData/Satimages/nonprojected/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color" # Правка
file_img = "Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color" # Правка
f = open("Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/Project/Mtsat_Japan_Geo_Color.txt","r") # Правка
txt = 'Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/Project/Mtsat_Japan_Geo_Color.txt' # Правка

# Создание опорных точек
def pervie (f):

    def zagruzka (f):

        for i in f:
            ff = re.split( '\s',i) # Из выведенной строки создается список с разделенными цифровыми данными
              
            c = ff [0]
            d = ff [1]
            m = "'" + str (c) + " " + str (d) + "'" + ";"
            return m
           
    n = len(open(txt, 'r').readlines())  
    nn = n - 1   
    i = 0
    sum = ""

    while i <= nn:
        sum = sum + zagruzka (f)
        i = i + 1
    return sum    
    
def vtorie (f):

    def zagruzka (f):

        for i in f:
            ff = re.split( '\s',i) # Из выведенной строки создается список с разделенными цифровыми данными
              
            c = ff [2]
            d = ff [3]
            m = "'" + str (c) + " " + str (d) + "'" + ";"
            return m
           
    n = len(open(txt, 'r').readlines())  
    nn = n - 1   
    i = 0
    sum = ""

    while i <= nn:
        sum = sum + zagruzka (f)
        i = i + 1
    return sum


	
# Вывод списка jpg файлов из каталога	
def sum_jpg (file): 
    for dirpath, dirnames, filenames in os.walk (file):
        c = filenames
        
        sum = []
        for i in c:
            c = i
            b = c[-3:]
            if b == "jpg":    # Возможная правка
                jpg = []       # Возможная правка
                jpg.append (c)  # Возможная правка
                sum = sum + jpg   # Возможная правка 
        return sum	
	
# Вывод списка jpg файлов из каталога
def sum_img (file): 
    for dirpath, dirnames, filenames in os.walk (file):
        c = filenames
        
        sum = []
        for i in c:
            c = i
            b = c[-3:]
            if b == "jp2":
                img = []
                img.append (c)
                sum = sum + img    
        return sum 
		
# Вывод списка в виде набора цифр (даты) JPG файл		
def date_jpg (jpg):        # Возможная правка
    sum_per_date = []
    for i in jpg:     # Возможная правка
        c = i
        b = c[0:12]  # Возможная правка
        
        date = []
        date.append (b)
        sum_per_date = sum_per_date + date 
    return sum_per_date
    
	
# Вывод списка в виде набора цифр (даты) img файл	
def date_img (img):        
    sum_per_date = []
    for i in img:
        c = i
        b = c[0:12] # Возможная правка
        
        date = []
        date.append (b)
        sum_per_date = sum_per_date + date 
    return sum_per_date   

# Привязка файов с расширением имени '_DAY.jpg'	
def zapusk1 (c, source_control_points, target_control_points):
    for i in c:
        file = i + '_DAY.jpg'
        file2 = i + '_DAY.jp2'
        in_raster = 'Z:/SatData/Satimages/nonprojected/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/'+ file
        out_raster = 'Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/'+ file2    
        
        # Расстановка опорных точек
        gp = arcgisscripting.create ()
        ppp = gp.Warp_management (in_raster, source_control_points, target_control_points, out_raster, "POLYORDER2", "BILINEAR") 
        ccc = ppp

        # Определение проекции
        coordsys = "Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/Project/Mtsat_Japan_Geo_Color.img"
        gp.DefineProjection_management (ccc, coordsys)  
        print gp.DefineProjection_management (ccc, coordsys) 

# Привязка файов с расширением имени '_DAYNGT.jpg'			
def zapusk2 (c, source_control_points, target_control_points):
    for i in c:
        file = i + '_DAYNGT.jpg'
        file2 = i + '_DAYNGT.jp2'
        in_raster = 'Z:/SatData/Satimages/nonprojected/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/'+ file
        out_raster = 'Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/'+ file2    
        
        # Расстановка опорных точек
        gp = arcgisscripting.create ()
        ppp = gp.Warp_management (in_raster, source_control_points, target_control_points, out_raster, "POLYORDER2", "BILINEAR") 
        ccc = ppp

        # Определение проекции
        coordsys = "Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/Project/Mtsat_Japan_Geo_Color.img"
        gp.DefineProjection_management (ccc, coordsys)  
        print gp.DefineProjection_management (ccc, coordsys)	
		
# Привязка файов с расширением имени '_NGT.jpg'	
def zapusk3 (c, source_control_points, target_control_points):
    for i in c:
        file = i + '_NGT.jpg'
        file2 = i + '_NGT.jp2'
        in_raster = 'Z:/SatData/Satimages/nonprojected/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/'+ file
        out_raster = 'Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/'+ file2    
        
        # Расстановка опорных точек
        gp = arcgisscripting.create ()
        ppp = gp.Warp_management (in_raster, source_control_points, target_control_points, out_raster, "POLYORDER2", "BILINEAR") 
        ccc = ppp

        # Определение проекции
        coordsys = "Z:/SatData/Satimages/Project/Mtsat/mtsat-2r/nrl/JAPAN/Geo-Color/Project/Mtsat_Japan_Geo_Color.img"
        gp.DefineProjection_management (ccc, coordsys)  
        print gp.DefineProjection_management (ccc, coordsys)		

def Razb_sp_png (date_png):
    for  i in date_png:
        return i  

def Razb_sp_img (date_img):   
    for ii in date_img:
        return ii 

def Poisk_pustih (date_png, date_img):
    a = len (date_png)
    m = 0
    sp_f = []
    while m < a:

        c = date_png [m]
        t = []
        


        for ii in date_img:
            if c != ii:
                t.append (0)
            else:
                t.append (c)
                 
        sp = t
        sum = 0
        for ss in sp:
            ss2 = int (ss)
            sum = sum + ss2
        m = m + 1
        
        if sum == 0:
            sp_f.append(c)
    return sp_f 

def del_null (file):
	for dirpath, dirnames, filenames in os.walk (file):
		ii =  dirpath
		for ccc in filenames:
			d = ii +"/"+ ccc
			f = str(d)
			ccc = os.path.getsize (f)
			if ccc < 17:
				os.unlink(f)	

del_null (file) #удаление объектов размером менее 17
	

# Загрузка опорных точек
f = open(txt,"r")
source_control_points = pervie (f)
t = open(txt,"r")
target_control_points = vtorie (t)
	
	
	
# Создаются 3 списка с различными расширениями файлов для jpg
a = sum_jpg (file)

Day_jpg = [] # Список
Daying_jpg = [] # Список
NGT_jpg = [] # Список

for i in a:				# Перебор общего списка с цель разделения данных по расширению названия файла (названия)
	a = "_DAY.jpg"
	b = "_DAYNGT.jpg"
	c = "_NGT.jpg"
	
	h_day = i[12:]
	if h_day == a:
		Day_jpg.append (i)
	elif h_day == b:
		Daying_jpg.append (i)
	elif h_day == c:
		NGT_jpg.append (i)

Day_d_jpg = date_jpg (Day_jpg)
Daying_d_jpg = date_jpg (Daying_jpg)
NGT_d_jpg = date_jpg (NGT_jpg)		

		
		
		
	
# Создаются 3 списка с различными расширениями файлов для Img
a2 = sum_img (file_img)

Day_img = [] # Список
Daying_img = [] # Список
NGT_img = [] # Список

for i2 in a2:				# Перебор общего списка с цель разделения данных по расширению названия файла (названия)
	a2 = "_DAY.jp2"
	b2 = "_DAYNGT.jp2"
	c2 = "_NGT.jp2"
	
	h_day2 = i2[12:]
	if h_day2 == a2:
		Day_img.append (i2)
	elif h_day2 == b2:
		Daying_img.append (i2)
	elif h_day2 == c2:
		NGT_img.append (i2)

Day_d_img = date_img (Day_img)
Daying_d_img = date_img (Daying_img)
NGT_d_img = date_img (NGT_img)	


  

Day_poisk = Poisk_pustih (Day_d_jpg, Day_d_img)  
Daying_poisk = Poisk_pustih (Daying_d_jpg, Daying_d_img)
NGT_poisk = Poisk_pustih (NGT_d_jpg, NGT_d_img)

zapusk1 (Day_poisk, source_control_points, target_control_points)
zapusk2 (Daying_poisk, source_control_points, target_control_points)
zapusk3 (NGT_poisk, source_control_points, target_control_points)

