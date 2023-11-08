import tkinter.ttk as ttk
import tkinter as tk


# Instance of the window
root = tk.Tk()
root.title("Search Path in Maze")

def pressButton(event):
    button = event.widget.button
    if(button.cget("bg") == '#d9d9d9'):
        button.configure(bg='black')
    else: 
        if(button.cget("bg") == 'black'):
            button.configure(bg='#d9d9d9')
    

# Frame1, maze

frm1 = tk.Frame(root, padx=10, pady=10, bg='white')
frm1.grid(row=0, column=0, padx= 5, pady= 5)

buttons = []

def getButtons():
    return buttons

# Creation of the maze composed of buttons
for i in range(15):
    row = []
    for j in range(15):
        button = tk.Button(frm1, text="", width=2, height=1)
        button.grid(row=i, column=j)
        button.row = i
        button.col = j
        button.button = button
        if i == 1 and j == 1:
            button.config(text='Exit', bg='lightgreen')
        if i == 13 and j == 13:
            button.config(text='Goal', bg='lightgreen')
        button.bind("<Button-1>", pressButton)
        row.append(button)
    buttons.append(row)



# Frame2, select algorithms

frm2 = tk.Frame(root, padx=10, pady=10, bg='white')
frm2.grid(row=0, column=1, padx= 5, pady= 5)

def getAlgorithmName():
    return comboBox.get()

solveButton = tk.Button(frm2, text="Solve", width=5, height=2)
solveButton.grid(row=0)

def getSolveButoon():
    return solveButton

clearButton = tk.Button(frm2, text="Clear", width=4, height=1)
clearButton.grid(row=1, pady=10)
onlyPath = ttk.Checkbutton(frm2, text="Only Path")
onlyPath.grid(row=1, column=1)

def clearColors(event):
    for i in range(15):
        for j in range(15):
            if((i != 1 or j != 1) and (i != 13 or j != 13)):
                if(buttons[i][j].cget("bg") != '#d9d9d9' and buttons[i][j].cget("bg") != 'black'):
                    buttons[i][j].config(bg='#d9d9d9')

clearButton.bind("<Button-1>", clearColors)

comboBox = ttk.Combobox(frm2, width=10, state="readonly", values=["BFS", "DFS", "Voraz"])
comboBox.grid(row=2)
comboBox.set(comboBox['values'][0])


def loop():
    root.mainloop()