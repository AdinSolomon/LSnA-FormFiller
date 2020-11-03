
from formfiller_gui import tk
from formfiller_gui import GUI

root = tk.Tk()
root.geometry("800x600")
app = GUI(master=root)
app.mainloop() 