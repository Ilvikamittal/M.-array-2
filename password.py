from tkinter import*
import random
root=Tk()

root.title("password generator")
root.geometry("400x400")
root.configure(background="green")

label=Label(root)
label.place(relx=0.5,rely=0.4,anchor=CENTER)

array=[[["0","1","2","3","4","5","6","7","8","9"],["a","b","c","d"],["A","B","C","D"],["!","@","#","$","%","^"]]]
print(array[0][3][2])

def newPassword():
    random_1=random.randint(0,9)
    random_2=random.randint(0,3)
    random_3=random.randint(0,5)
    
    letter1=str(array[0][0][random_1])
    letter2=str(array[0][3][random_3])
    letter3=str(array[0][1][random_2])
    letter4=str(array[0][2][random_2])
    letter5=str(array[0][1][random_2])
    letter6=str(array[0][3][random_3])
    letter7=str(array[0][2][random_2])
    letter8=str(array[0][0][random_1])
    
    
    label["text"]=letter1+letter2+letter3+letter4+letter5+letter6+letter8
    
btn_1=Button(root,text="password",command=newPassword)    
btn_1.place(relx=0.5,rely=0.5,anchor=CENTER)


    

root.mainloop()

