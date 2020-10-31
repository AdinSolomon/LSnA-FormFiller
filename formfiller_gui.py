import tkinter as tk
from tkinter import filedialog

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.populate_window()

    def populate_window(self):
        self.widgets_form_format()
        self.widgets_input_format()
        self.widgets_input_files()
        self.widgets_generate()
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=4, column=1)

    def widgets_form_format(self):
        # User selects a form format file (word file)
        self.form_format_selector = tk.Button(self)
        self.form_format_selector["text"] = "Select Form Format File\n(Word document)"
        self.form_format_selector["command"] = self.select_form_format_file
        self.form_format_selector.grid(row=0, column=0)
        self.form_format_location = tk.Entry(self)
        self.form_format_location.grid(row=1, column=0)

    def select_form_format_file(self):
        # file selector dialog
        print("select_form_format_file()")
        filename = self.choose_file("Word Document (format files)", "*.docx")
        self.form_format_location.insert(0,filename)

    def widgets_input_format(self):
        # User selects an input format file (excel file)
        self.input_format_selector = tk.Button(self)
        self.input_format_selector["text"] = "Select Input Format File\n(Excel file)"
        self.input_format_selector["command"] = self.select_input_format_file
        self.input_format_selector.grid(row=2, column=0)
        self.input_format_location = tk.Entry(self)
        self.input_format_location.grid(row=3, column=0)
        
    def select_input_format_file(self):
        # file selector dialog
        print("select_input_format_file()")

    def widgets_input_files(self):
        # List of input files which the user can populate
        #   by following a file selector dialog.
        self.input_file_selector = tk.Button(self)
        self.input_file_selector["text"] = "Select Input Files\n(Excel files)"
        self.input_file_selector["command"] = self.select_input_files
        self.input_file_selector.grid(row=0, column=2)
        self.input_file_list = tk.Listbox(self)
        self.input_file_list.insert(1, "test1")
        self.input_file_list.insert(0, "test2")
        self.input_file_list.grid(row=1, column=2)
        pass

    def select_input_files(self):
        print("select_input_files()")

    def widgets_generate(self):
        # These widgets create files from the form format and input files
        self.generate = tk.Button(self)
        self.generate["text"] = "Generate Forms"
        self.generate["command"] = self.generate_forms
        self.generate.grid(row=3, column=2)
    
    def generate_forms(self):
        print("generate_forms()")

    def choose_file(self, file_type: str, file_ext: str):
        # TODO - make parameters useful
        return filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", "*.txt*")))

