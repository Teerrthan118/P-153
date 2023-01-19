from tkinter import *
import random

root=Tk()
root.title("Password Generator")
root.geometry("400x400")
input=Entry(root)
input.place(relx=0.5,rely=0.3, anchor = CENTER)
label2=Label(root)
label= Label(root)

array_3d =[[['1','2','3','4','5','6'],["Head","Tail"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][2][3])


def new_password(): 
    random_no_1 = random.randint(0,5)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,7)
    
    letter1 =str(array_3d[0][0][random_no_1])
    letter2 =(array_3d[0][1][random_no_2])
    letter3 =(array_3d[0][2][random_no_3])
    entered_password = input.get()
    label2["text"] = "Guessed password: " + entered_password
    password = letter1 + "" + letter2 + "" + letter3
    label["text"] = "Generated password: " + password

btn = Button(root, text= "New Password", command = new_password)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)
label2.place(relx = 0.5, rely =0.4, anchor = CENTER)
label.place(relx = 0.5, rely =0.6, anchor = CENTER)

root.mainloop()