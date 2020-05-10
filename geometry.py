import tkinter

window = tkinter.Tk()
window.title("geometry")

label = tkinter.Label(window, text="hello", font=("Arial Bold", 50))
label.grid(column=0, row=2)
button = tkinter.Button(window, text="button", bg="red", fg="white")
button.grid(column=0, row=0)
#Geometry function
window.geometry("630x700")


window.mainloop()
