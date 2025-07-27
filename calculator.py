import tkinter as tk

def on_click(char):
    current = entry_var.get()
    if char == 'C':
        entry_var.set('')
    elif char == '=':
        try:
            entry_var.set(str(eval(current)))
        except Exception:
            entry_var.set('Error')
    else:
        entry_var.set(current + str(char))

root = tk.Tk()
root.title("Round Styled Calculator")
root.configure(bg='#8B004B')  # dark pink background

entry_var = tk.StringVar()
entry = tk.Entry(
    root, textvariable=entry_var, font=('Consolas', 24), bd=0, highlightthickness=0,
    width=14, borderwidth=0, justify='right', fg='#FFFFFF', bg='#67003B'
)
entry.grid(row=0, column=0, columnspan=4, pady=(15,10), padx=12, sticky='we')

buttons = [
    'C', '7', '8', '9',
    '/', '4', '5', '6',
    '*', '1', '2', '3',
    '-', '0', '=', '+'
]

button_styles = {
    'numbers': {'bg': '#ADD8E6', 'fg': '#FFFFFF', 'active': '#BFEFFF'},  # light blue/white
    'pink': {'bg': '#FF007F', 'active': '#E60073', 'fg': '#FFFFFF'},
    'blue': {'bg': "#3CADCD", 'active': '#3CADCD', 'fg': '#FFFFFF'},
    'clear': {'bg': "#CD1F6D", 'active': "#CD1F6D", 'fg': '#FFFFFF'},
    'equal': {'bg': '#3CADCD', 'active': '#3CADCD', 'fg': '#FFFFFF'},
}

row = 1
col = 0
for button in buttons:
    if button == 'C':
        color = button_styles['clear']
    elif button == '=':
        color = button_styles['equal']
    elif button in ['/', '*', '-', '+']:
        color = button_styles['blue']
    elif button.isdigit():
        color = button_styles['numbers']
    else:
        color = button_styles['pink']

    tk.Button(
        root, text=button, font=('Consolas', 20, 'bold'), bg=color['bg'], fg=color['fg'],
        activebackground=color['active'], bd=0, relief='ridge', padx=26, pady=26, highlightthickness=0,
        command=lambda x=button: on_click(x)
    ).grid(row=row, column=col, padx=12, pady=12, sticky='nsew')
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(row+1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()

