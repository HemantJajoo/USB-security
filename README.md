# USB-security

First step is to create a trigger in udev program and to make your own service which performs the actions you want it to do. I have provided a documentation of how to do it in the file named udev automation documentation.

Now we have succesfully trigerred a program which runs when someone inserts a usb stick, the next task is to create a program that takes the intruders photo.

For taking the photo i am using the open cv module of python and storing the photo in a file named defaulter.jpg. Code for this is in the file named photo.py.

Now the last task is to mail that photo.
Since we want this mailing process to be automatic I have used ansible for automation. but wait the problem here is to provide the password for the mail id from which you are sending the mail. To cope with this problem I have used ansible vault option in which i have provided the password of my mail id securely and only i can acess this vault. 
Now ansible has to open this vault so I have provided the vault password in a file hidden somwhere on my sytem that no one can found.

Ansible automatically after getting all the inputs send the uthorized personnel a mail with the defaulters photo.
