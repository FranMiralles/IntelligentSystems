import tkinter.ttk as ttk
import tkinter as tk
import os
from PIL import Image, ImageTk

#Color constants
WALLS = '#031602' #black
DIRT = '#66d401' #d9d9d9
SPECIAL = '#b34d03' #lightgreen
ROUTE = '#0e0f93'
GENERATED = '#8080ff'
BACK = '#e5ffbe' #ECECEC
presetsData = 'presets.txt'


# Instance of the window
root = tk.Tk()
root.title("Searching Algorithms")

root.geometry("1000x800+0+0")
root.minsize(800, 500)
root.config(bg = BACK)

# Menu walls
menuBar = tk.Menu(root)
menuBar.config(bg = BACK, font = ('Normal', 9))
root.config(menu = menuBar)
presetMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Preset walls", menu=presetMenu, background=BACK)


presetMenu.add_command(label="Preset #1", command=lambda num=1:selectPreset(0), background=BACK)
presetMenu.add_command(label="Preset #2", command=lambda num=1:selectPreset(1), background=BACK)
presetMenu.add_command(label="Preset #3", command=lambda num=1:selectPreset(2), background=BACK)
presetMenu.add_command(label="Preset #4", command=lambda num=1:selectPreset(3), background=BACK)
presetMenu.add_separator(background=BACK)
savePresetMenu = tk.Menu(presetMenu, tearoff=0)
presetMenu.add_cascade(label="Save current as", menu=savePresetMenu, background=BACK)
savePresetMenu.add_command(label="Preset #1", command=lambda num=1:savePreset(0), background=BACK)
savePresetMenu.add_command(label="Preset #2", command=lambda num=1:savePreset(1), background=BACK)
savePresetMenu.add_command(label="Preset #3", command=lambda num=1:savePreset(2), background=BACK)
savePresetMenu.add_command(label="Preset #4", command=lambda num=1:savePreset(3), background=BACK)

def selectPreset(num):
    with open(presetsData) as presets:
        lines = [line.strip() for line in presets.readlines()]
        data = eval(lines[num])
        clearMethod(1)
        k = 0
        for i in range(15):
            for j in range(15):
                if(data[k] == 'WALLS'):
                    buttons[i][j].config(bg=WALLS)
                k += 1


def savePreset(num):
    with open(presetsData, 'r+') as presets:
        lines = [line.strip() for line in presets.readlines()]
        newLine = []
        for i in range(15):
            for j in range(15):
                data = 'None'
                if(buttons[i][j].cget("bg") == WALLS):
                    data = 'WALLS'
                newLine.append(data)
        lines[num] = newLine
        presets.seek(0)
        presets.write(str(lines[0]) + '\n'); presets.write(str(lines[1]) + '\n'); presets.write(str(lines[2]) + '\n'), presets.write(str(lines[3]))




def pressButton(event):
    button = event.widget.button
    if(button.cget("bg") == DIRT):
        button.configure(bg=WALLS)
    else: 
        if(button.cget("bg") == WALLS):
            button.configure(bg=DIRT)
    

# Frame1, maze

frm1 = tk.LabelFrame(root, text="Maze", bg = BACK)
frm1.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.85)

buttons = []

def getButtons():
    return buttons

# Creation of the maze composed of buttons
for i in range(15):
    row = []
    for j in range(15):
        button = tk.Button(frm1, text="", width=2, height=1)
        button.place(relx=0.01 + j/15.5, rely= 0.01 + i/15.5, relheight=0.066, relwidth=0.066)
        button.row = i
        button.col = j
        button.button = button
        if i == 1 and j == 1:
            button.config(text='Exit', bg=SPECIAL)
        elif i == 13 and j == 13:
            button.config(text='Goal', bg=SPECIAL)
        else:
            button.config(bg=DIRT)
        button.bind("<Button-1>", pressButton)
        row.append(button)
    buttons.append(row)



# Frame2, select algorithms

frm2 = tk.LabelFrame(root, padx=10, pady=10, text="Action", bg = BACK)
frm2.place(relx=0.7, rely=0.1, relwidth=0.25, relheight=0.4)


def getAlgorithmName():
    return comboBox.get()

solveButton = tk.Button(frm2, text="Solve", bg=DIRT)
solveButton.place(relx=0.05, rely=0.45, relwidth=0.45, relheight=0.5)

def getSolveButoon():
    return solveButton

clearButton = tk.Button(frm2, text="Clear Route", bg=DIRT)
clearButton.place(relx=0.5, rely=0.45, relwidth=0.45, relheight=0.25)

clearAllButton = tk.Button(frm2, text="Clear All", bg=DIRT)
clearAllButton.place(relx=0.5, rely=0.7, relwidth=0.45, relheight=0.25)

def clearMethod(tipoClear):
    for i in range(15):
        for j in range(15):
            if((i != 1 or j != 1) and (i != 13 or j != 13)):
                if(tipoClear == 0):
                    if(buttons[i][j].cget("bg") != DIRT and buttons[i][j].cget("bg") != WALLS):
                        buttons[i][j].config(bg=DIRT)
                else:
                    if(buttons[i][j].cget("bg") != DIRT):
                        buttons[i][j].config(bg=DIRT)

clearButton.bind("<Button-1>", lambda event, tipoClear=0: clearMethod(tipoClear))
clearAllButton.bind("<Button-1>", lambda event, tipoClear=1: clearMethod(tipoClear))



comboBox = ttk.Combobox(frm2, width=10, state="readonly", values=["BFS", "DFS", "GREEDY MANHATTAN", "A MANHATTAN"])
comboBox.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)
comboBox.set(comboBox['values'][0])


# Frame3, result of algorithms

frm2 = tk.LabelFrame(root, padx=10, pady=10, text="Results", bg = BACK)
frm2.place(relx=0.7, rely=0.55, relwidth=0.25, relheight=0.3)

pathLength = tk.Label(frm2, text='Path Length: ', anchor="w", bg= BACK)
pathLength.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.15)
pathLengthValue = tk.Label(frm2, text='0', anchor="e", bg= BACK)
pathLengthValue.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.15)
nodesGenerated = tk.Label(frm2, text='Nodes Generated: ', anchor="w", bg= BACK)
nodesGenerated.place(relx=0.05, rely=0.25, relwidth=0.6, relheight=0.15)
nodesGeneratedValue = tk.Label(frm2, text='0', anchor="e", bg= BACK)
nodesGeneratedValue.place(relx=0.7, rely=0.25, relwidth=0.25, relheight=0.15)
time = tk.Label(frm2, text='Time in seconds:', anchor="w", bg= BACK)
time.place(relx=0.05, rely=0.45, relwidth=0.6, relheight=0.15)
timeValue = tk.Label(frm2, text='0', anchor="e", bg= BACK)
timeValue.place(relx=0.7, rely=0.45, relwidth=0.25, relheight=0.15)


def loop():
    root.mainloop()