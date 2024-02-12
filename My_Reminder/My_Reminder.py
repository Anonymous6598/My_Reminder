import tkinter, tkinter.filedialog, tkinter.messagebox, typing, My_Reminder_interface, random, tkdrag, My_Reminder_screen, CTkMenuBar, My_Reminder_note, My_Reminder_list_note, locale
from tkinterdnd2 import *
from customtkinter import *

class GUI(My_Reminder_screen.Tk, My_Reminder_interface.My_Reminder_interface):
    
    TITLE: typing.Final[str] = f"My Reminder"
    ICON: typing.Final[str] = f"my reminder icon.ico"
    COLOR_THEME: typing.Final[str] = f"dark-blue"
    WIDGET_SCALING: typing.Final[float] = 1.251
    APPEREANCE: typing.Final[str] = f"system"

    def __init__(self: typing.Self, fg_color: str | tuple[str, str] | None = None, *args: typing.Any, **kwargs: typing.Any):
        My_Reminder_screen.Tk.__init__(self, fg_color, *args, **kwargs)
        
        set_widget_scaling(self.WIDGET_SCALING)
        set_default_color_theme(self.COLOR_THEME)
        set_appearance_mode(self.APPEREANCE)
        deactivate_automatic_dpi_awareness()

        self.title(self.TITLE)
        self.iconbitmap(self.ICON)
        
        self.main_secreen_title_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(master=self)

        self.main_screen_note_frame: CTkFrame = CTkFrame(master=self, height=791, width=1535, corner_radius=0, bg_color=f"transparent", border_color=(f"black", f"white"), border_width=1)
        self.main_screen_note_frame.place(x=0, y=0)
        
        if locale.getdefaultlocale()[0] == "sr_RS":   
           self.main_secreen_title_menu.add_cascade(text=f"нова белешка", command=self.__create_note__)
           self.main_secreen_title_menu.add_cascade(text=f"нови списак", command=self.__create_list_note__)  
           
        elif locale.getdefaultlocale()[0] == "ru_RU":
           self.main_secreen_title_menu.add_cascade(text=f"новая заметка", command=self.__create_note__)
           self.main_secreen_title_menu.add_cascade(text=f"новый список", command=self.__create_list_note__)           

        else:
           self.main_secreen_title_menu.add_cascade(text=f"new note", command=self.__create_note__)
           self.main_secreen_title_menu.add_cascade(text=f"new list", command=self.__create_list_note__)


    @typing.override
    def __create_note__(self: typing.Self) -> None:
        self.note: My_Reminder_note.Note = My_Reminder_note.Note(master=self.main_screen_note_frame)
        self.note.place(x=random.randint(300, 500), y=random.randint(100, 200))

    @typing.override
    def __create_list_note__(self: typing.Self) -> None:
        self.note: My_Reminder_list_note.List_note = My_Reminder_list_note.List_note(master=self.main_screen_note_frame)
        self.note.place(x=random.randint(300, 500), y=random.randint(100, 200))
   
if __name__ == f"__main__":
    program: GUI = GUI()
    program.mainloop()