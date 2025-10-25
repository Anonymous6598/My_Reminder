import customtkinter, tkinter, typing, My_Reminder_interface, random, My_Reminder_screen, CTkMenuBar, My_Reminder_note, My_Reminder_list_note, My_Reminder_AI_window, sys, pickle, My_Reminder_settings, ctypes, CTkToolTip

with open(f"my_reminder_language_settings.pickle", f"rb+") as data: language_data: str = pickle.load(data)

with open(f"my_reminder_theme_settings.pickle", f"rb+") as theme_data: theme: str = pickle.load(theme_data)

class Program(My_Reminder_screen.Window, My_Reminder_interface.My_Reminder_interface):
    
    TITLE: typing.Final[str] = f"My Reminder "
    COLOR_THEME: typing.Final[str] = f"dark-blue"
    WIDGET_SCALING: typing.Final[int] = 1.251

    def __init__(self: typing.Self, fg_color: str | tuple[str, str] | None = None, *args: typing.Any, **kwargs: typing.Any):
        My_Reminder_screen.Window.__init__(self, fg_color, *args, **kwargs)
        
        customtkinter.set_default_color_theme(self.COLOR_THEME)
        customtkinter.set_appearance_mode(theme)
        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.deactivate_automatic_dpi_awareness()

        self.title(self.TITLE)
        
        self.main_screen_menu: CTkMenuBar.CTkMenuBar = CTkMenuBar.CTkMenuBar(master=self)
        
        self.main_screen_note_menu_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"☰")

        self.main_screen_menu_settings_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"⚙️", command=lambda: My_Reminder_settings.My_Reminder_setting_window())

        self.main_screen_note_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(master=self, height=791, width=1535, corner_radius=0, bg_color=f"transparent", border_color=(f"black", f"white"), border_width=1)
        self.main_screen_note_frame.pack(fill=tkinter.BOTH, expand=True)

        self.main_screen_note_frame_menu: tkinter.Menu = tkinter.Menu(self.main_screen_note_frame, tearoff=0)

        self.bind("<Button-3>", lambda event: self.main_screen_note_frame_menu.post(event.x_root, event.y_root))
        self.bind(f"<F11>", lambda event: self.__fullscreen__())
        
        if language_data == f"Српски":
           self.main_screen_note_menu_button_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_note_menu_button, fg_color=f"transparent")

           self.main_screen_note_menu_button_submenu.add_option(option=f"нова белешка", command=self.__create_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"нови списак", command=self.__create_list_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"AI", command=lambda: My_Reminder_AI_window.My_Reminder_AI_window()) 

           self.main_screen_note_frame_menu.add_command(label=f"нова белешка", command=self.__create_note__)
           self.main_screen_note_frame_menu.add_command(label=f"нови списак", command=self.__create_list_note__)

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"ВИ", command=lambda: My_Reminder_AI_window.My_Reminder_AI_window())

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"излаз", command=lambda: sys.exit())
           
        elif language_data == f"Русский":
           self.main_screen_note_menu_button_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_note_menu_button, fg_color=f"transparent")

           self.main_screen_note_menu_button_submenu.add_option(option=f"новая заметка", command=self.__create_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"новый список", command=self.__create_list_note__)

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_menu_button_submenu.add_option(option=f"ИИ (Нейро сеть)", command=lambda: My_Reminder_AI_window.My_Reminder_AI_window())  

           self.main_screen_note_frame_menu.add_command(label=f"новая заметка", command=self.__create_note__)
           self.main_screen_note_frame_menu.add_command(label=f"новый список", command=self.__create_list_note__)
           self.main_screen_note_frame_menu.add_command(label=f"ИИ (Нейро сеть)", command=lambda: My_Reminder_AI_window.My_Reminder_AI_window())

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"выход", command=lambda: sys.exit())         

        else:
           self.main_screen_note_menu_button_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_note_menu_button, fg_color=f"transparent")

           self.main_screen_note_menu_button_submenu.add_option(option=f"new note", command=self.__create_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"new list", command=self.__create_list_note__)
           self.main_screen_note_menu_button_submenu.add_option(option=f"AI", command=lambda: My_Reminder_AI_window.My_Reminder_AI_window())

           self.main_screen_note_frame_menu.add_command(label=f"new note", command=self.__create_note__)
           self.main_screen_note_frame_menu.add_command(label=f"new list", command=self.__create_list_note__)

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"AI", command=lambda: My_Reminder_AI_window.My_Reminder_AI_window())

           self.main_screen_note_frame_menu.add_separator()

           self.main_screen_note_frame_menu.add_command(label=f"exit", command=lambda: sys.exit())

        if language_data == f"Српски":
            self.main_screen_menu_settings_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_menu_settings_button, message=f"подешавања")
            self.main_screen_title_menu_menu_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_note_menu_button, message=f"мени")

        elif language_data == f"Русский":
            self.main_screen_menu_settings_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_menu_settings_button, message=f"настройки")
            self.main_screen_title_menu_menu_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_note_menu_button, message=f"меню")
    
        else:
            self.main_screen_menu_settings_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_menu_settings_button, message=f"settings")
            self.main_screen_title_menu_menu_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_note_menu_button, message=f"menu")

    @typing.override
    def __create_note__(self: typing.Self) -> None:
        self.note: My_Reminder_note.Note = My_Reminder_note.Note(master=self.main_screen_note_frame)
        self.note.place(x=random.randint(300, 500), y=random.randint(100, 200))

    @typing.override
    def __create_list_note__(self: typing.Self) -> None:
        self.note: My_Reminder_list_note.List_note = My_Reminder_list_note.List_note(master=self.main_screen_note_frame)
        self.note.place(x=random.randint(300, 500), y=random.randint(100, 200))

    @typing.override
    def __fullscreen__(self: typing.Self) -> None:
        if self.attributes(f"-fullscreen"): self.attributes(f"-fullscreen", False)
        
        else: self.attributes(f"-fullscreen", True)

        if customtkinter.get_appearance_mode()=="Dark": value=1
        
        else: value=0
    
        try:
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1 = 19

            if ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(value)), ctypes.sizeof(ctypes.c_int(value))) != 0: ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1, ctypes.byref(ctypes.c_int(value)), ctypes.sizeof(ctypes.c_int(value)))
        
        except Exception as err: pass
   
if __name__ == f"__main__":
    program: Program = Program()

    program.mainloop()
