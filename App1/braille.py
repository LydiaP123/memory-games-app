from tkinter import Frame, Canvas
braille = {
    'a': {1: 'on', 2: 'off', 3: 'off', 4: 'off', 5: 'off', 6: 'off'},
    'b': {1: 'on', 2: 'off', 3: 'on', 4: 'off', 5: 'off', 6: 'off'},
    'c': {1: 'on', 2: 'on', 3: 'off', 4: 'off', 5: 'off', 6: 'off'},
    'd': {1: 'on', 2: 'on', 3: 'off', 4: 'on', 5: 'off', 6: 'off'},
    'e': {1: 'on', 2: 'off', 3: 'off', 4: 'on', 5: 'off', 6: 'off'},
    'f': {1: 'on', 2: 'on', 3: 'on', 4: 'off', 5: 'off', 6: 'off'},
    'g': {1: 'on', 2: 'on', 3: 'on', 4: 'on', 5: 'off', 6: 'off'},
    'h': {1: 'on', 2: 'off', 3: 'on', 4: 'on', 5: 'off', 6: 'off'},
    'i': {1: 'off', 2: 'on', 3: 'on', 4: 'off', 5: 'off', 6: 'off'},
    'j': {1: 'off', 2: 'on', 3: 'on', 4: 'on', 5: 'off', 6: 'off'},
    'k': {1: 'on', 2: 'off', 3: 'off', 4: 'off', 5: 'on', 6: 'off'},
    'l': {1: 'on', 2: 'off', 3: 'on', 4: 'off', 5: 'on', 6: 'off'},
    'm': {1: 'on', 2: 'on', 3: 'off', 4: 'off', 5: 'on', 6: 'off'},
    'n': {1: 'on', 2: 'on', 3: 'off', 4: 'on', 5: 'on', 6: 'off'},
    'o': {1: 'on', 2: 'off', 3: 'off', 4: 'on', 5: 'on', 6: 'off'},
    'p': {1: 'on', 2: 'on', 3: 'on', 4: 'off', 5: 'on', 6: 'off'},
    'q': {1: 'on', 2: 'on', 3: 'on', 4: 'on', 5: 'on', 6: 'off'},
    'r': {1: 'on', 2: 'off', 3: 'on', 4: 'on', 5: 'on', 6: 'off'},
    's': {1: 'off', 2: 'on', 3: 'on', 4: 'off', 5: 'on', 6: 'off'},
    't': {1: 'off', 2: 'on', 3: 'on', 4: 'on', 5: 'on', 6: 'off'},
    'u': {1: 'on', 2: 'off', 3: 'off', 4: 'off', 5: 'on', 6: 'on'},
    'v': {1: 'on', 2: 'off', 3: 'on', 4: 'off', 5: 'on', 6: 'on'},
    'w': {1: 'off', 2: 'on', 3: 'on', 4: 'on', 5: 'off', 6: 'on'},
    'x': {1: 'on', 2: 'on', 3: 'off', 4: 'off', 5: 'on', 6: 'on'},
    'y': {1: 'on', 2: 'on', 3: 'off', 4: 'on', 5: 'on', 6: 'on'},
    'z': {1: 'on', 2: 'off', 3: 'off', 4: 'on', 5: 'on', 6: 'on'}
}


class BrailleFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.bg="black"
        self.item_data = {}
        self.canvas = Canvas(self, width=400, height=250, bg='black', highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.oval1 = self.create_oval(0, 0, number_id=1)
        self.oval2 = self.create_oval(100, 0, number_id=2)
        self.oval3 = self.create_oval(0, 100, number_id=3)
        self.oval4 = self.create_oval(100, 100, number_id=4)
        self.oval5 = self.create_oval(0, 200, number_id=5)
        self.oval6 = self.create_oval(100, 200, number_id=6)
        self.text = self.canvas.create_text(275, 125, text="?", fill="white", font=("Arial", 100))
        self.current_activation = {1: "off", 2: "off", 3: "off", 4: "off", 5: "off", 6: "off"}

    def create_oval(self, x_pos, y_pos, number_id):
        x = self.canvas.create_oval(x_pos, y_pos, x_pos + 50, y_pos + 50, fill='grey')
        self.canvas.tag_bind(x, "<Button-1>", lambda event: self.change_color(self.canvas, x))
        self.item_data[x] = number_id
        return x

    def change_color(self, canvas, oval_id):
        current_color = canvas.itemcget(oval_id, "fill")
        if current_color != "white":
            canvas.itemconfig(oval_id, fill='white')
            self.current_activation[self.item_data[oval_id]] = "on"
        else:
            canvas.itemconfig(oval_id, fill='grey')
            self.current_activation[self.item_data[oval_id]] = "off"
        change = True
        for key in braille:
            if braille[key] == self.current_activation:
                canvas.itemconfig(self.text, text=key)
                change = False
            elif change == True:
                canvas.itemconfig(self.text, text="?")





