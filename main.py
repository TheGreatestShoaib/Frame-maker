import cv2

def frame(inp):
	picture = cv2.imread(inp,cv2.IMREAD_COLOR) #reading main picture 
	frame= cv2.imread("doney.jpg",cv2.IMREAD_COLOR) #reading frame
	#resizing image and picture both two 
	frame = cv2.resize(frame,(900,900)) 
	picture = cv2.resize(picture,(900,900))
	hei, wid = picture.shape[:2]  # image height and width
	for x in range(183,hei):
		for y in range(330,wid):
			if x  < int(870) and y < int(830): # change value according to the frame
				frame[x,y] = picture[x-110,y-190] #image position in frame ,change according to the picture
			else:
				break
				
	cv2.imwrite("final_result.jpg",frame) #saving file two device
	cv2.imshow("last",frame)
	cv2.waitKey(0)

frame("kakashi2.jpg")