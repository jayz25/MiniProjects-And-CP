import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello,Tkinter")
greeting.pack()
button = tk.Button(text="button",
                    width=10,
                    height=2,
                    bg="blue",
                    fg="yellow",
)
button.pack()
window.mainloop()
