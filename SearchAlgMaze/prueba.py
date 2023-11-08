import tkinter as tk

class App:

    def __init__(self):
        self.root = tk.Tk()

        fm1 = tk.Frame(self.root, bg='red')
        fm1.pack(fill='x')

        fm2 = tk.Frame(self.root, bg='blue')
        fm2.pack(fill='y', expand=True, anchor='nw')

        fm3 = tk.Frame(self.root, bg='green')
        fm3.pack(fill='y', expand=True, anchor='ne')

        tk.Label(fm1, text='Frame 1').pack()
        tk.Label(fm2, text='Frame 2').pack()
        tk.Label(fm3, text='Frame 3').pack()

    def mainloop(self):
        self.root.mainloop()

if __name__ == '__main__':
    ejemplo2 = App()
    ejemplo2.mainloop()