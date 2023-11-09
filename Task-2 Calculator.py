from tkinter import Tk, StringVar, Entry, Button

class Calculator(Tk):
    def __init__(self):
        Tk.__init__(self)  # Call the __init__ method of the Tk class

        self.title('Calculator')
        self.geometry('400x400')
        self.configure(background="white")
        self.string = StringVar()
        entry = Entry(self, textvariable=self.string)
        entry.grid(row=0, column=0, columnspan=4)
        entry.configure(background="white")
        self.btn_bg_color = 'cyan'
        entry.focus()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "c", "ac",  # Corrected labels to lowercase
        ]

        row, col = 1, 0
        for button_text in buttons:
            if button_text == '=':
                btn = Button(self, height=2, width=4, padx=10, pady=10, text=button_text, command=self.equals)
            elif button_text in ['c', 'ac']:
                btn = Button(self, height=2, width=4, padx=10, pady=10, text=button_text, command=lambda bt=button_text: self.clear(bt))
            else:
                btn = Button(self, height=2, width=4, padx=10, pady=10, text=button_text, command=lambda bt=button_text: self.add_char(bt))

            btn.grid(row=row, column=col, padx=5, pady=5)
            btn.configure(background=self.btn_bg_color)

            col += 1
            if col == 4:
                col = 0
                row += 1

        self.mainloop()

    def clear(self, char):
        if char == 'c':  # Corrected to lowercase
            self.string.set(self.string.get()[:-1])
        elif char == 'ac':  # Corrected to lowercase
            self.string.set("")

    def equals(self):
        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            self.string.set("INVALID INPUT")

    def add_char(self, char):
        self.string.set(self.string.get() + str(char))


Calculator()
