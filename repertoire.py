from tkinter import* 
from functools import partial

def app():

    def repertoire(): 
        root = Tk()
        h = root.winfo_screenheight()
        l = root.winfo_screenwidth()
        root.configure(bg = "black")
        b = 50
        contacts = ["Philou","Hélicoptère","Flifli","Clémenthe à l'eau","Natcho","Calixtou"]
        initiales = ["P","H","F","C","N","C"]
        for i in range(len(contacts)):
            contact = Button(root, text = contacts[i], background = "#FFD700", bd = 0)
            #if contact :
             #   messagerie()
            canvas = Canvas(root, background = "#FFD700", width=50,height=50, bd = 0)
            initial = Label(text = initiales[i], background = "#FFD700", height = 0, width = 0, font=("Courier", 28))
            canvas.place(x = 0, y = b)
            contact.place(x = 60, y = b+10)
            initial.place(x = 10, y = b+1)
            b += 60
        root.title("Répertoire")
        root.mainloop()
    
    repertoire()
    
