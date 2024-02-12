import My_Reminder_Note_interface, typing, tkinter.filedialog, locale, tkdrag
from customtkinter import *
from tkinterdnd2 import *

class Note(CTkFrame, My_Reminder_Note_interface.My_Reminder_Note_interface):
    WIDTH: typing.Final[int] = 300
    HEIGHT: typing.Final[int] = 300
    CORNER_RADIUS: typing.Final[int] = 5
    
    def __init__(self: typing.Self, master: typing.Any | None = None, height: int = HEIGHT, width: int = WIDTH, corner_radius: int = CORNER_RADIUS, border_width: int = 1, fg_color: str = f"transparent", *args, **kwargs) -> None:
        CTkFrame.__init__(self, master=master, height=height, width=width, corner_radius=corner_radius, border_width=border_width, fg_color=fg_color, *args, **kwargs)
        
        self.main_screen_note_text_box: CTkTextbox = CTkTextbox(master=self, width=295, height=260, corner_radius=self.CORNER_RADIUS, fg_color=f"transparent", border_width=0)
        self.main_screen_note_text_box.place(x=2, y=2)

        self.main_screen_note_text_box.drop_target_register(DND_ALL)
        self.main_screen_note_text_box.dnd_bind(f"<<Drop>>", self.__open_note_with_dnd__)
        
        self.main_screen_note_open_note_button: CTkButton = CTkButton(master=self, height=30, width=40, text=f"отвори", fg_color=(f"dark blue", f"green"), command=self.__open_note__)
        self.main_screen_note_open_note_button.place(x=2, y=265)
        
        self.main_screen_note_save_note_button: CTkButton = CTkButton(master=self, height=30, width=40, text=f"сачувај", fg_color=(f"dark blue", f"green"), command=self.__save_note__)
        self.main_screen_note_save_note_button.place(x=118, y=265)

        self.main_screen_note_clear_note_button: CTkButton = CTkButton(master=self, height=30, width=40, text=f"обриши", fg_color=(f"dark blue", f"green"), command=self.__delete_note__)
        self.main_screen_note_clear_note_button.place(x=236, y=265)

        tkdrag.Drag(self)
        
        if locale.getdefaultlocale()[0] == "sr_RS":
           self.main_screen_note_open_note_button.configure(text=f"отвори")
           self.main_screen_note_save_note_button.configure(text=f"сачувај") 
           self.main_screen_note_clear_note_button.configure(text=f"обриши")                 
                 
        elif locale.getdefaultlocale()[0] == "ru_RU":
           self.main_screen_note_open_note_button.configure(text=f"открыть")
           self.main_screen_note_save_note_button.configure(text=f"сохранить") 
           self.main_screen_note_clear_note_button.configure(text=f"удалить")
                
        else:
           self.main_screen_note_open_note_button.configure(text=f"open")
           self.main_screen_note_save_note_button.configure(text=f"save") 
           self.main_screen_note_clear_note_button.configure(text=f"clear")
        
    @typing.override
    def __open_note__(self: typing.Self) -> None:
        try:
            with open(tkinter.filedialog.askopenfilename(title=f"open file", filetypes=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")]), f"r+", encoding=f"UTF-8") as self.openned_file:
                 self.main_screen_note_text_box.insert(f"1.0", self.openned_file.read())

        except FileNotFoundError: pass
        
    def __open_note_with_dnd__(self: typing.Self, event: str | None = None) -> None:
        try:
            with open(event.data, f"r+", encoding=f"UTF-8") as self.openned_file:
                self.main_screen_note_text_box.insert(f"1.0", self.openned_file.read())

        except FileNotFoundError: pass
    
    @typing.override
    def __save_note__(self: typing.Self) -> None:
        with open(tkinter.filedialog.asksaveasfilename(filetypes=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")]), f"w+", encoding=f"UTF-8") as self.file:
            try:
                self.file_data: str = self.main_screen_note_text_box.get("1.0", tkinter.END)
                self.file.write(self.file_data)
					
            except FileNotFoundError: pass
        
    @typing.override
    def __delete_note__(self: typing.Self) -> None:
        self.place_forget()