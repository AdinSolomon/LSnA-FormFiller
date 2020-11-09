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
        # User selects a form format file (Word file)
        # Selector Button
        self.form_format_selector = tk.Button(self)
        self.form_format_selector["text"] = "Select Form Format File\n(Word document)"
        self.form_format_selector["command"] = self.select_form_format_file
        self.form_format_selector.grid(row=0, column=0, sticky=tk.S)
        # File Path
        self.form_format_filename = tk.Entry(self)
        self.form_format_filename.grid(row=1, column=0, sticky=tk.N)

    def select_form_format_file(self):
        # file selector dialog
        print("select_form_format_file()")
        temp = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a Form Format File", 
                                          filetypes = (("Form Format (Word)", "*.docx"),("all files","*.*")))
        print("\t", temp)
        self.form_format_filename.insert(0,temp)

    def widgets_input_format(self):
        # User selects an input format file (excel file)
        # Selector Button
        self.input_format_selector = tk.Button(self)
        self.input_format_selector["text"] = "Select Input Format File\n(Excel file)"
        self.input_format_selector["command"] = self.select_input_format_file
        self.input_format_selector.grid(row=2, column=0, sticky=tk.S)
        # File Name
        self.input_format_filename = tk.Entry(self)
        self.input_format_filename.grid(row=3, column=0, sticky=tk.N)
        
    def select_input_format_file(self):
        # file selector dialog
        print("select_input_format_file()")
        temp = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select an Input Format File", 
                                          filetypes = (("Input Format (Excel)", "*.xlsx"),("all files","*.*")))
        print("\t", temp)
        self.input_format_filename.insert(0,temp)

    def widgets_input_files(self):
        # List of input files which the user can populate
        #   by following a file selector dialog.
        # Selector Button
        self.input_file_selector = tk.Button(self)
        self.input_file_selector["text"] = "Select Input Files\n(Excel files)"
        self.input_file_selector["command"] = self.select_input_files
        self.input_file_selector.grid(row=0, column=2, sticky=(tk.N + tk.S + tk.E + tk.W))
        # File List
        self.input_file_list = tk.Listbox(self)
        self.input_file_list.insert(1, "test")
        self.input_file_list.grid(row=1, column=2, rowspan=3)
        pass

    def select_input_files(self):
        print("select_input_files()")
        temp = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select an Input File", 
                                          filetypes = (("Input File (Excel)", "*.xlsx"),("all files","*.*")))
        print("\t", temp)
        self.input_file_list.insert(1, temp)

    def widgets_generate(self):
        # These widgets create files from the form format and input files
        self.generate = tk.Button(self)
        self.generate["text"] = "Generate Forms"
        self.generate["command"] = self.generate_forms
        self.generate.grid(row=4, column=2)
    
    def generate_forms(self):
        print("generate_forms()")

