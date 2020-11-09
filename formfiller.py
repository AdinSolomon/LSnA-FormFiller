
from GUI import tk
from GUI import GUI

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = GUI(master=root)
    app.mainloop()
