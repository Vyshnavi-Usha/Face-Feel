from deepface import DeepFace
from tkinter import *
from PIL import ImageTk,Image
ins=Tk()
text1=Text(ins,height=20,width=50)
text2=Text(ins,height=20,width=70)
img = ImageTk.PhotoImage(Image.open(r"happy.jpg"))
label= Label(text1, image=img,  anchor= CENTER)
label.pack()
text1.pack(side=LEFT)
face_analysis = DeepFace.analyze(img_path = r"happy.jpg")
a=face_analysis[0]["dominant_emotion"]
b=face_analysis[0]["emotion"]
c=face_analysis[0]["age"]
d=face_analysis[0]["dominant_gender"]
e=face_analysis[0]["dominant_race"]
f=face_analysis[0]["race"]
text2.tag_configure('big', font=('Verdana',10),foreground="green")
text2.insert(INSERT,"\n\nEmotion: ","big")
text2.insert(INSERT,a)
text2.insert(INSERT,"\n\nDistribution: ","big")
text2.insert(INSERT,b)
text2.insert(INSERT,"\n\nAge: ","big")
text2.insert(INSERT,c)
text2.insert(INSERT,"\n\nGender: ","big")
text2.insert(INSERT,d)
text2.insert(INSERT,"\n\nRace: ","big")
text2.insert(INSERT,e)
text2.insert(INSERT,"\n\nDistribution: ","big")
text2.insert(INSERT,f)
text2.pack(side=LEFT)
ins.mainloop()
