import tkinter as tk
window = tk.Tk()
window.title("Hello Tkinter!")
window.mainloop()

window = tk.Tk()

window.title("GUI Elements")

label = tk.Label(text="Label 1")
label.pack()

label_2 = tk.Label(text="Label 2", background="red", foreground="white")
label_2.pack()

label_3 = tk.Label(text="Label 3", background="yellow", width="10", height="5")
label_3.pack()

button = tk.Button(text="Button!", width="7", height="2")
button.pack()

input_felt = tk.Entry(width="15")
input_felt.pack()

text_box = tk.Text()
text_box.pack()

window.mainloop()