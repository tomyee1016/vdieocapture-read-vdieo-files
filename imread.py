import cv2
cap = cv2.VideoCapture('E:/广东爱情故事.mp4')
while(cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('baby',gray)
    if cv2.waitKey(1)&0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()