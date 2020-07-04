#!/usr/bin/python36

import subprocess
import cv2 

cap = cv2.VideoCapture(0)
ret, image = cap.read()

cv2.imwrite('/root/Udev_automation/defaulter.jpg' , image) 
#cv2.imshow('hi' , image)
#cv2.waitKey()
cv2.destroyAllWindows()

subprocess.getoutput("ansible-playbook /root/Udev_automation/security.yml  --vault-password-file=/root/Udev_automation/mypasswd")
