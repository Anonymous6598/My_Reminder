import tkinter, tkinter.filedialog, tkinter.messagebox, pickle, typing, My_Reminder_interface, My_Reminder_Note_interface, random, functools, pickle, tkdrag
from tkinterdnd2 import *
from customtkinter import *

with open(f"my_reminder_settings.pickle", f"rb+") as data: language_data: str = pickle.load(data)

def memorise(function_param: str) -> str:
																		 
    cache: dict = {}

    @functools.wraps(function_param)
    def wrapper(*args, **kwargs) -> str:
        key: str = str(args) + str(kwargs)
        if key not in cache:
            cache[key]: function = function_param(*args, **kwargs)

        return cache[key]
    
    return wrapper

class Tk(CTk, TkinterDnD.DnDEvent):
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        CTk.__init__(self, *args, **kwargs)
        TkinterDnD.TkdndVersion: TkinterDnD._require = TkinterDnD._require(self)

class GUI(Tk, My_Reminder_interface.My_Reminder_interface):
    
    WIDTH: typing.Final[int] = 1920
    HEIGHT: typing.Final[int] = 1080
    TITLE: typing.Final[str] = f"My Reminder"
    ICON: typing.Final[str] = f"my reminder icon.ico"
    COLOR_THEME: typing.Final[str] = f"dark-blue"
    WIDGET_SCALING: typing.Final[float] = 1.251   

    def __init__(self: typing.Self, fg_color: str | tuple[str, str] | None = None, *args: typing.Any, **kwargs: typing.Any):
        Tk.__init__(self, *args, **kwargs)
        
        set_widget_scaling(self.WIDGET_SCALING)
        set_default_color_theme(self.COLOR_THEME)
        set_appearance_mode(f"system")
        deactivate_automatic_dpi_awareness()

        self.title(self.TITLE)
        self.iconbitmap(self.ICON)
        
        self.after(250, lambda: self.geometry(f"{self.WIDTH}x{self.HEIGHT}"))
        
        self.main_screen_menu_frame: CTkFrame = CTkFrame(master=self, height=791, width=300, corner_radius=3, bg_color=f"transparent", border_color=(f"black", f"white"), border_width=1)
        self.main_screen_menu_frame.place(x=1, y=1)
        
        self.main_screen_menu_frame_create_note_button: CTkButton = CTkButton(master=self.main_screen_menu_frame, text=f"нова белешка", text_color=f"white", height=20, width=296, corner_radius=5, fg_color=f"green", font=(f"Roboto Bold", 22), command=self.__create_note__)
        self.main_screen_menu_frame_create_note_button.place(x=1, y=2)                

        self.main_screen_menu_frame_settings_button: CTkButton = CTkButton(master=self.main_screen_menu_frame, text=f"подешавања", text_color=f"white", height=20, width=296, corner_radius=5, fg_color=f"green", font=(f"Roboto Bold", 22), command=self.__settigs__)
        self.main_screen_menu_frame_settings_button.place(x=1, y=35)        

        self.main_screen_note_frame: CTkFrame = CTkFrame(master=self, height=791, width=1235, corner_radius=3, bg_color=f"transparent", border_color=(f"black", f"white"), border_width=1)
        self.main_screen_note_frame.place(x=300, y=1)
        
        self.main_screen_settings_text: CTkLabel = CTkLabel(master=self, text=f"подешавања", text_color=f"white", font=(f"Roboto Bold", 72))

        self.main_screen_settings_language_text: CTkLabel = CTkLabel(master=self, text=f"језици", text_color=f"white", font=(f"Roboto Bold", 36))

        self.main_screen_settings_language_option: CTkSegmentedButton = CTkSegmentedButton(master=self, values=[f"Српски", f"English", f"Русский"], text_color=f"white", selected_color=f"green", command=self.__change_language__)
    
        self.main_screen_exit_button: CTkButton = CTkButton(master=self, text=f"...", text_color=f"white", height=20, width=10, corner_radius=0, fg_color=f"green", command=self.__exit_settings__)

        self.main_screen_settings_language_option.set(language_data)
        
        match language_data:
            case "Српски":
                self.main_screen_menu_frame_create_note_button.configure(text=f"нова белешка")
                self.main_screen_menu_frame_settings_button.configure(text=f"подешавања")
                 
                self.main_screen_settings_text.configure(text=f"подешавања")
                self.main_screen_settings_language_text.configure(text=f"језици")
                 

            case "English":
                self.main_screen_menu_frame_create_note_button.configure(text=f"new note")
                self.main_screen_menu_frame_settings_button.configure(text=f"settings")
                 
                self.main_screen_settings_text.configure(text=f"settigs")
                self.main_screen_settings_language_text.configure(text=f"languages")
                 
            case _:
               self.main_screen_menu_frame_create_note_button.configure(text=f"новая заметка")
               self.main_screen_menu_frame_settings_button.configure(text=f"настройки")
                 
               self.main_screen_settings_text.configure(text=f"настройки")
               self.main_screen_settings_language_text.configure(text=f"языки")

    @typing.override
    def __create_note__(self: typing.Self) -> None:
        self.note: Note = Note(master=self.main_screen_note_frame)
        self.note.place(x=random.randint(300, 500), y=random.randint(100, 200))
        
        tkdrag.Drag(self.note)
   
    @typing.override
    def __settigs__(self: typing.Self) -> None:
        self.main_screen_menu_frame.place_forget()
        self.main_screen_note_frame.place_forget()

        self.main_screen_exit_button.place(x=1, y=1)
        self.main_screen_settings_text.place(x=3, y=21)
        self.main_screen_settings_language_text.place(x=3, y=102)
        self.main_screen_settings_language_option.place(x=18, y=142)

    def __exit_settings__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_exit_button.place_forget()
        self.main_screen_settings_text.place_forget()
        self.main_screen_settings_language_text.place_forget()
        self.main_screen_settings_language_option.place_forget()

        self.main_screen_menu_frame.place(x=1, y=1)
        self.main_screen_note_frame.place(x=300, y=1)
        
    @typing.override
    def __change_language__(self: typing.Self,  pickle_serialization: pickle) -> None:
        self.main_screen_settings_language_option_variable: str = self.main_screen_settings_language_option.get()
        with open(f"my_reminder_settings.pickle", f"wb+") as self.data:
            pickle.dump(self.main_screen_settings_language_option_variable, self.data)

        match self.main_screen_settings_language_option_variable: 
            case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

            case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

            case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

    def __run__(self: typing.Self) -> None:
        self.mainloop()
        
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
        
        self.main_screen_note_open_note_button: CTkButton = CTkButton(master=self, height=30, width=40, text=f"отвори", fg_color=f"green", command=self.__open_note__)
        self.main_screen_note_open_note_button.place(x=2, y=265)
        
        self.main_screen_note_save_note_button: CTkButton = CTkButton(master=self, height=30, width=40, text=f"сачувај", fg_color=f"green", command=self.__save_note__)
        self.main_screen_note_save_note_button.place(x=118, y=265)

        self.main_screen_note_clear_note_button: CTkButton = CTkButton(master=self, height=30, width=40, text=f"обриши", fg_color=f"green", command=self.__delete_note__)
        self.main_screen_note_clear_note_button.place(x=236, y=265)
        
        match language_data:
            case "Српски":
                self.main_screen_note_open_note_button.configure(text=f"отвори")
                self.main_screen_note_save_note_button.configure(text=f"сачувај") 
                self.main_screen_note_clear_note_button.configure(text=f"обриши")                 

            case "English":
                self.main_screen_note_open_note_button.configure(text=f"open")
                self.main_screen_note_save_note_button.configure(text=f"save") 
                self.main_screen_note_clear_note_button.configure(text=f"clear")
                 
            case _:
                self.main_screen_note_open_note_button.configure(text=f"открыть")
                self.main_screen_note_save_note_button.configure(text=f"сохранить") 
                self.main_screen_note_clear_note_button.configure(text=f"удалить")
        
    @typing.override
    @memorise
    def __open_note__(self: typing.Self) -> None:
        try:
            with open(tkinter.filedialog.askopenfilename(title=f"open file", filetypes=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")]), f"r+", encoding=f"UTF-8") as self.openned_file:
                self.main_screen_note_text_box.insert(f"1.0", self.openned_file.read())

        except FileNotFoundError: pass
        
    @memorise
    def __open_note_with_dnd__(self: typing.Self, event: str | None = None) -> None:
        try:
            with open(event.data, f"r+", encoding=f"UTF-8") as self.openned_file:
                self.main_screen_note_text_box.insert(f"1.0", self.openned_file.read())

        except FileNotFoundError: pass
    
    @typing.override
    @memorise
    def __save_note__(self: typing.Self) -> None:
        with open(tkinter.filedialog.asksaveasfilename(filetypes=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")]), f"w+", encoding=f"UTF-8") as self.file:
            try:
                self.file_data: str = self.main_screen_note_text_box.get("1.0", tkinter.END)
                self.file.write(self.file_data)
					
            except FileNotFoundError: pass
        
    @typing.override
    def __delete_note__(self: typing.Self) -> None:
        self.destroy()

if __name__ == f"__main__":
    program: GUI = GUI()
    program.__run__()