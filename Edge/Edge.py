import cv2
img=cv2.imread(r'C:\Users\sange\Downloads\cycle.jpg')
gray1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray1)
cv2.waitKey(0)
img1=cv2.imread(r'C:\Users\sange\Downloads\taj.jpg')
gray2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray2)
cv2.waitKey(0)
img2=cv2.imread(r'C:\Users\sange\Downloads\jogging.jpg')
gray3=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray3)
cv2.waitKey(0)
canny_high=cv2.Canny(gray1,200,230)
cv2.imshow("High",canny_high)
cv2.imwrite(r'C:\Users\sange\OneDrive\Desktop\Theshold\Edge\Cycle.jpg',canny_high)
cv2.waitKey(0)
canny_high1=cv2.Canny(gray2,100,240)
cv2.imshow("High",canny_high1)
cv2.imwrite(r'C:\Users\sange\OneDrive\Desktop\Theshold\Edge\Taj_Mahal.jpg',canny_high1)
cv2.waitKey(0)
canny_high2=cv2.Canny(gray3,190,240)
cv2.imshow("High",canny_high2)
cv2.imwrite(r'C:\Users\sange\OneDrive\Desktop\Theshold\Edge\Jogging.jpg',canny_high2)
cv2.waitKey(0)