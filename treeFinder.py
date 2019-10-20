import cv2
import numpy as np

#Load images
imag1 = cv2.imread('data/satellite_img/7_1.png',1)
imag2 = cv2.imread('data/satellite_img/8_1.png',1)
imag3 = cv2.imread('data/data/satellite_img/9.png',1)
imag4 = cv2.imread('data/data/satellite_img/10.png',1)

save1 = 'data/satellite_img/AI-Results/Image1/'
save2 = 'data/satellite_img/AI-Results/Image2/'
save3 = 'data/data/satellite_img/AI-Results/Image3/'
save4 = 'data/data/satellite_img/AI-Results/Image4/'

def save(imag,name,save):
	cv2.imwrite(save+name,imag)


def treeFinder(img1,saver):
	### Raw Image save
	save(img1,'1.jpg',saver)
	#Image size
	heigth = np.size(img1, 0)
	width = np.size(img1, 1)

	#Estructural elements
	se1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
	se2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
	se3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))

	#Image to HSV
	ima = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

	#Image thresholding for getting tree colors
	#lower_green = np.array([60,70,30])
	#upper_green = np.array([100,100,88])

	lower_green = np.array([60,50,30])
	upper_green = np.array([145,100,88])

	#Mask generation
	mask = cv2.inRange(ima, lower_green, upper_green)

	#Omask
	Omask = np.zeros((heigth,width,3), np.uint8)
	for i in range(heigth):
		for j in range(width):
			if mask[i,j] == 0:
				Omask[i,j] = img1[i,j]
			else:
				Omask[i,j,1] = 255
	save(Omask,'2.jpg',saver)

	#Corrections
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, se1)

	#Omask2
	Omask2 = np.zeros((heigth,width,3), np.uint8)
	for i in range(heigth):
		for j in range(width):
			if mask[i,j] == 0:
				Omask2[i,j] = img1[i,j]
			else:
				Omask2[i,j,1] = 255
	save(Omask2,'3.jpg',saver)

	openning = cv2.morphologyEx(closing, cv2.MORPH_OPEN, se2)
	#Omask3
	Omask3 = np.zeros((heigth,width,3), np.uint8)
	for i in range(heigth):
		for j in range(width):
			if mask[i,j] == 0:
				Omask3[i,j] = img1[i,j]
			else:
				Omask3[i,j,1] = 255
	save(Omask3,'4.jpg',saver)


	#Fist mask
	res = cv2.bitwise_and(img1,img1, mask= openning)


	## Mask with desired trees (region mode)
	new = np.zeros((heigth,width,3), np.uint8)
	for i in range(heigth):
		for j in range(width):
			if not (res[i,j,0] == 0 and res[i,j,1] == 0 and res[i,j,2] == 0):
				new[i,j,0] = 25
				new[i,j,1] = 115
				new[i,j,2] = 38

	#Omask4
	Omask4 = Overlay(new,img1,heigth,width)
	save(Omask4,'5.jpg',saver)

	new = cv2.erode(new,se3,1)

	#Omask5
	Omask5 = Overlay(new,img1,heigth,width)
	save(Omask5,'6.jpg',saver)

	new = cv2.erode(new,se2,1)

	#Omask6
	Omask6 = Overlay(new,img1,heigth,width)
	save(Omask6,'7.jpg',saver)

	## Clustering
	coords = []
	for i in range(heigth):
		for j in range(width):
			if not (new[i,j,0] == 0 and new[i,j,1] == 0 and new[i,j,2] == 0):
				coords.append((i,j))
	parakmeans = np.float32(coords)
	K = 30
	attempts = 10
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	ret,label,center=cv2.kmeans(parakmeans,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

	#Final image
	new2 = np.zeros((heigth,width,3), np.uint8)
	for i in range(len(center)):
		new2[int(round(center[i][0])),int(round(center[i][1])),1] = 255

	#Omask7
	Omask7 = Overlay(new2,img1,heigth,width)
	save(Omask7,'8.jpg',saver)

	#Final tunning
	new2 = cv2.dilate(new2,se1,1)
	final =Overlay(new2,img1,heigth,width)
	save(final,'9.jpg',saver)
	return final

def Overlay(new2,img1,heigth,width):
	#Overlay
	final = np.zeros((heigth,width,3), np.uint8)
	for i in range(heigth):
		for j in range(width):
			if new2[i,j,1] == 0:
				final[i,j] = img1[i,j]
			else:
				final[i,j,1] = 255
	return final

#final1 = treeFinder(imag1,save1)
#final2 = treeFinder(imag2,save2)
final3 = treeFinder(imag3,save3)
final4 = treeFinder(imag4,save4)



#cv2.imshow('res',final)
#cv2.waitKey(30000)
#cv2.destroyAllWindows()