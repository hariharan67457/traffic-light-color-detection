from tkinter import *
from PIL import ImageTk, Image
  

from tkinter import filedialog
from tlr import * 

def openfilename():
  
    # open file dialog box to select image

    filename = filedialog.askopenfilename(title ='fileexplorer')
    return filename
def open_img():
    # Select the Imagename  from a folder 
    x = openfilename()
    s=""
    for i in x[::-1]:
        if i!='/':
            s+=i 
        else:
            break
    try: 
        apply_tlr(s[::-1])
    except:
        pass
   
    

      
   


# Create a window
root = Tk()
  
# Set Title as Image Loader
root.title("traffic light detector")

text=Label(root,justify=CENTER,fg='red',font="Helvetica 16 bold italic",text='welcome to our traffic light detector application')



text.pack()
t=Label(root,justify=CENTER,fg='green',font="Helvetica 16 bold italic",text='Please click the below button to choose the traffic light image')
# Set the resolution of window
t.pack()
root.geometry('700x500')
  
# Allow Window to be resizable
root.resizable(width = True, height = True)
  
# Create a button and place it into the window using grid layout
btn = Button(root, text ='open image', command = open_img,height=3,width=9,bg='blue',fg='white').place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()         



