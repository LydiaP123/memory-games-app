import tkinter as tk
from braille import BrailleFrame
from binary import BinaryFrame
from radio import RadioFrame
from PIL import Image, ImageTk
# morse code, periodic table


window = tk.Tk()
window.configure(bg='black')
window.title("")
window.attributes("-topmost", True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
home_frame = tk.Frame(window, bg='black')
button_frame = tk.Frame(window, bg='black')
button_frame.pack(side="top", pady=(0, 75))
home_frame.pack()
CURRENT_FRAME = home_frame
frame2 = BrailleFrame(window)
frame3 = BinaryFrame(window)
frame4 = RadioFrame(window)

def update_frame(new_frame):
    global CURRENT_FRAME
    CURRENT_FRAME.pack_forget()
    new_frame.pack()
    CURRENT_FRAME = new_frame

canvas1 = tk.Canvas(bg='black', width=500, height=70, highlightthickness=0)
right_image1 = Image.open("/Users/lydiaperlin/PycharmProjects/App1/right_arrow.png")
right_image2 = ImageTk.PhotoImage(right_image1)
left_image1 = Image.open("/Users/lydiaperlin/PycharmProjects/App1/left_arrow.png")
left_image2 = ImageTk.PhotoImage(left_image1)
right_arrow = canvas1.create_image(450,35, image=right_image2)
left_arrow = canvas1.create_image(50,35, image=left_image2)
# canvas1.pack(side="bottom", pady=70)
# canvas1.tag_bind(left_arrow, "<Button-1>", lambda event: update_frame(home_frame))
# canvas1.tag_bind(right_arrow, "<Button-1>", lambda event: update_frame)
window.update()

braille_button = tk.Button(button_frame, text="Braille", command=lambda: update_frame(frame2))
braille_button.grid(row=0, column=0)

binary_button = tk.Button(button_frame, text="Binary", command=lambda: update_frame(frame3))
binary_button.grid(row=0, column=1)

radio_button = tk.Button(button_frame, text="NATO alphabet", command=lambda: update_frame(frame4))
radio_button.grid(row=0, column=2)

morse_button = tk.Button(button_frame, text="Morse code")
morse_button.grid(row=0, column=3)

periodic_button = tk.Button(button_frame, text="Periodic")
periodic_button.grid(row=0, column=4)

window.mainloop()
