import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the result
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 18), bd=5, relief=tk.SUNKEN, justify=tk.RIGHT)
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Calculator buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, font=('Arial', 18), bd=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

        # Make the buttons expand to fill the available space
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        elif text == 'C':
            self.result_var.set("0")
        else:
            current_text = self.result_var.get()
            if current_text == '0' or current_text == 'Error':
                self.result_var.set(text)
            else:
                self.result_var.set(current_text + text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
