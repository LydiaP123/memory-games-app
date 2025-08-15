import tkinter as tk
PLACEHOLDER = "Type a letter's code from the NATO phonetic alphabet, and the letter will appear here! All non-letter characters can be inserted one at a time, too."

radio_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-Ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

class RadioFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.bg="black"
        self.entry = tk.Entry(self)
        self.entry.config(width=20, font=("Arial", 20))
        self.entry.grid(row=0, column=0, sticky="nsew")
        self.entry.focus()
        self.entry.bind("<Return>", lambda event: self.process())
        self.text = tk.Label(self, text=PLACEHOLDER, bg='black', fg='white', height=5, padx=15, wraplength=400, font=("Arial", 20))
        self.text.grid(row=0, column=1, sticky="nsew")

    def typing_after_error(self):
        self.entry.delete(0, tk.END)
        self.entry.unbind("<Key>")

    def process(self):
        content = self.text["text"]
        if content == PLACEHOLDER:
            self.text.config(text="")
            content = self.text["text"]
        input = self.entry.get().title()
        error = True
        for letter in radio_alphabet.keys():
            if radio_alphabet[letter] == input:
                self.text.config(text=content+letter)
                error = False
        if len(input) == 1 and input not in radio_alphabet.keys():
            self.text.config(text=content+input)
            error = False
        self.entry.delete(0, tk.END)
        if error:
            self.entry.placeholder = "INVALID"
            self.entry.placeholder_color = "gray"
            self.entry.insert(0, self.entry.placeholder)
            self.entry.icursor(0)
            self.entry.bind("<Key>", lambda event: self.typing_after_error())




