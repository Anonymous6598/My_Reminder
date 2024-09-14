import tkinter, tkinter.filedialog, tkinter.messagebox, typing, My_Reminder_interface, random, My_Reminder_screen, CTkMenuBar, My_Reminder_note, My_Reminder_list_note, locale, asyncio, My_Reminder_AI
import customtkinter
from tkinterdnd2 import *
from customtkinter import *

class Program(My_Reminder_screen.Tk, My_Reminder_interface.My_Reminder_interface):
    
    TITLE: typing.Final[str] = f"My Reminder "
    ICON: typing.Final[str] = f"my reminder icon.ico"
    COLOR_THEME: typing.Final[str] = f"dark-blue"
    APPEREANCE: typing.Final[str] = f"system"
    WIDGET_SCALING: typing.Final[int] = 1.251

    def __init__(self: typing.Self, fg_color: str | tuple[str, str] | None = None, *args: typing.Any, **kwargs: typing.Any):
        My_Reminder_screen.Tk.__init__(self, fg_color, *args, **kwargs)
        
        set_default_color_theme(self.COLOR_THEME)
        set_appearance_mode(self.APPEREANCE)
        set_widget_scaling(self.WIDGET_SCALING)
        deactivate_automatic_dpi_awareness()

        self.title(self.TITLE)
        self.iconbitmap(self.ICON)
        
        self.main_secreen_title_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(master=self)

        self.main_screen_note_frame: CTkFrame = CTkFrame(master=self, height=791, width=1535, corner_radius=0, bg_color=f"transparent", border_color=(f"black", f"white"), border_width=1)
        self.main_screen_note_frame.place(x=0, y=0)
        
        self.main_screen_note_menu_button: customtkinter.CTkButton = self.main_secreen_title_menu.add_cascade(text=f"☰")

        self.main_screen_note_frame_menu: tkinter.Menu = tkinter.Menu(self.main_screen_note_frame, tearoff=0)

        self.bind("<Button-3>", lambda event: self.main_screen_note_frame_menu.post(event.x_root, event.y_root))
        
        if locale.getdefaultlocale()[0] == "sr_RS":
           self.main_screen_note_menu_button_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_note_menu_button, fg_color=f"transparent")

           self.main_screen_note_menu_button_submenu.add_option(option=f"нова белешка", command=self.__create_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"нови списак", command=self.__create_list_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"ВИ", command=lambda: AI_window())

           self.main_screen_note_frame_menu.add_command(label=f"нова белешка", command=self.__create_note__)
           self.main_screen_note_frame_menu.add_command(label=f"нови списак", command=self.__create_list_note__)

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"ВИ", command=lambda: AI_window())

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"излаз", command=lambda: sys.exit())
           
        elif locale.getdefaultlocale()[0] == "ru_RU":
           self.main_screen_note_menu_button_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_note_menu_button, fg_color=f"transparent")

           self.main_screen_note_menu_button_submenu.add_option(option=f"новая заметка", command=self.__create_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"новый список", command=self.__create_list_note__)

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_menu_button_submenu.add_option(option=f"ИИ (Нейро сеть)", command=lambda: AI_window())  

           self.main_screen_note_frame_menu.add_command(label=f"новая заметка", command=self.__create_note__)
           self.main_screen_note_frame_menu.add_command(label=f"новый список", command=self.__create_list_note__)
           self.main_screen_note_frame_menu.add_command(label=f"ИИ (Нейро сеть)", command=lambda: AI_window())

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"выход", command=lambda: sys.exit())         

        else:
           self.main_screen_note_menu_button_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_note_menu_button, fg_color=f"transparent")

           self.main_screen_note_menu_button_submenu.add_option(option=f"new note", command=self.__create_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"new list", command=self.__create_list_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"AI", command=lambda: AI_window())

           self.main_screen_note_frame_menu.add_command(label=f"new note", command=self.__create_note__)
           self.main_screen_note_frame_menu.add_command(label=f"new list", command=self.__create_list_note__)

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"AI", command=lambda: AI_window())

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"exit", command=lambda: sys.exit())

    @typing.override
    def __create_note__(self: typing.Self) -> None:
        self.note: My_Reminder_note.Note = My_Reminder_note.Note(master=self.main_screen_note_frame)
        self.note.place(x=random.randint(300, 500), y=random.randint(100, 200))

    @typing.override
    def __create_list_note__(self: typing.Self) -> None:
        self.note: My_Reminder_list_note.List_note = My_Reminder_list_note.List_note(master=self.main_screen_note_frame)
        self.note.place(x=random.randint(300, 500), y=random.randint(100, 200))
        
class AI_window(CTkToplevel):
    
    TITLE: typing.Final[str] = f"My Diary AI assistant"
    HEIGHT: typing.Final[int] = 375
    WIDTH: typing.Final[int] = 655
    ICON: typing.Final[str] = f"my reminder icon.ico"

    def __init__(self: typing.Self, *args, **kwargs) -> None:
        CTkToplevel.__init__(self, *args, **kwargs)

        self.title(self.TITLE)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.after(250, lambda: self.iconbitmap(self.ICON))

        self.ai_window_textbox: CTkTextbox = CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
        self.ai_window_textbox.place(x=0, y=0)

        self.ai_window_textbox.configure(state=f"disabled")

        self.ai_window_entry: CTkEntry = CTkEntry(master=self, height=30, width=524, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
        self.ai_window_entry.place(x=0, y=269)

        self.ai_window_entry.bind(f"<Return>", self.__response__)

    def __response__(self: typing.Self, configure: str | None = None) -> None:
        self.ai_window_entry_data: str = self.ai_window_entry.get()

        self.ai_window_textbox.configure(state=f"normal")
        self.query: str = asyncio.run(My_Reminder_AI.My_Reminder_LM().__response__(self.ai_window_entry_data))

        self.ai_window_textbox.insert(tkinter.END, f"{self.query}\n", f"-1.0")
        self.ai_window_textbox.configure(state=f"disabled")
        self.ai_window_entry.delete(f"-1", tkinter.END)
   
if __name__ == f"__main__":
    program: Program = Program()
    program.mainloop()