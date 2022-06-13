from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title("Country Flags")
root.geometry("600x400")
root.configure(background="lightblue")

get_input = Entry(root)
show_label = Label(root)

india = ImageTk.PhotoImage(Image.open ("India.jpg"))
america = ImageTk.PhotoImage(Image.open ("America.jpg"))
australia = ImageTk.PhotoImage(Image.open ("Australia.png"))
philippines = ImageTk.PhotoImage(Image.open ("Philippines.png"))
japan = ImageTk.PhotoImage(Image.open ("Japan.jpg"))

flags_dictionary = { "India" : india, 
                    "America" : america,
                    "Australia" : australia,
                    "Philippines" : philippines,
                    "Japan" : japan}

def showFlags():
    try:
        flag_name = get_input.get()
        print(flag_name)
        show_label['image'] = flags_dictionary[flag_name]
    except:
        messagebox.showinfo("Error", "Sorry! This country flag is not present in our system")

btn = Button(root , text="Show Flag", bg="green", command=showFlags)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()