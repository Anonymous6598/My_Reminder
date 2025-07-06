import customtkinter, tkinter, typing, My_Reminder_interface, random, My_Reminder_screen, CTkMenuBar, My_Reminder_note, My_Reminder_list_note, locale, My_Reminder_AI, sys, warnings, speech_recognition, threading

warnings.filterwarnings(f"ignore")

SLM: My_Reminder_AI.My_Reminder_LM = My_Reminder_AI.My_Reminder_LM().__initialize_model__()

class Program(My_Reminder_screen.Window, My_Reminder_interface.My_Reminder_interface):
    
    TITLE: typing.Final[str] = f"My Reminder (Copliot+PC edition)"
    ICON: typing.Final[str] = f"my reminder icon.ico"
    COLOR_THEME: typing.Final[str] = f"dark-blue"
    APPEREANCE: typing.Final[str] = f"system"
    WIDGET_SCALING: typing.Final[int] = 1.251

    def __init__(self: typing.Self, fg_color: str | tuple[str, str] | None = None, *args: typing.Any, **kwargs: typing.Any):
        My_Reminder_screen.Window.__init__(self, fg_color, *args, **kwargs)
        
        customtkinter.set_default_color_theme(self.COLOR_THEME)
        customtkinter.set_appearance_mode(self.APPEREANCE)
        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.deactivate_automatic_dpi_awareness()

        self.title(self.TITLE)
        self.iconbitmap(self.ICON)
        
        self.main_screen_title_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(master=self)

        self.main_screen_note_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(master=self, height=791, width=1535, corner_radius=0, bg_color=f"transparent", border_color=(f"black", f"white"), border_width=1)
        self.main_screen_note_frame.pack(fill=tkinter.BOTH, expand=True)
        
        self.main_screen_note_menu_button: customtkinter.CTkButton = self.main_screen_title_menu.add_cascade(text=f"☰")

        self.main_screen_note_frame_menu: tkinter.Menu = tkinter.Menu(self.main_screen_note_frame, tearoff=0)

        self.bind(f"<Button-3>", lambda event: self.main_screen_note_frame_menu.post(event.x_root, event.y_root))
        
        self.main_screen_note_menu_button_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_note_menu_button, fg_color=f"transparent")
           
        self.main_screen_note_menu_button_submenu.add_option(option=f"new note", command=self.__create_note__)
        self.main_screen_note_menu_button_submenu.add_option(option=f"new list", command=self.__create_list_note__)
        self.main_screen_note_menu_button_submenu.add_option(option=f"AI", command=lambda: My_Reminder_AI_window())

        self.main_screen_note_frame_menu.add_command(label=f"new note", command=self.__create_note__)
        self.main_screen_note_frame_menu.add_command(label=f"new list", command=self.__create_list_note__)

        self.main_screen_note_frame_menu.add_separator()

        self.main_screen_note_frame_menu.add_command(label=f"AI", command=lambda: My_Reminder_AI_window())

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

class My_Reminder_AI_window(customtkinter.CTkToplevel):

    TITLE: typing.Final[str] = f"My Reminder AI assistant (Copilot+PC edition)"
    HEIGHT: typing.Final[int] = 375
    WIDTH: typing.Final[int] = 655
    ICON: typing.Final[str] = f"my_diary_icon.ico"
    COLOR_THEME: typing.Final[str] = f"dark-blue"
    WIDGET_SCALING: typing.Final[float] = 1.251

    def __init__(self: typing.Self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.set_default_color_theme(self.COLOR_THEME)
        customtkinter.deactivate_automatic_dpi_awareness()

        self.title(self.TITLE)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.after(250, lambda: self.iconbitmap(self.ICON))

        self.ai_window_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
        self.ai_window_textbox.place(x=0, y=0)

        self.ai_window_textbox.configure(state=f"disabled")

        self.ai_window_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self, height=30, width=465, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
        self.ai_window_entry.place(x=0, y=269)

        self.ai_window_microphone_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"🎤", command=self.__audio_input__)
        self.ai_window_microphone_button.place(x=465, y=269)

        self.ai_window_send_request_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"->", command=self.__response__)
        self.ai_window_send_request_button.place(x=495, y=269)

        self.ai_window_entry.bind(f"<Return>", self.__response__)

    @typing.override
    def __response__(self: typing.Self, event: str | None = None) -> None:
        self.ai_window_entry_data: str = self.ai_window_entry.get()

        def run_model():
            response_text: str = My_Reminder_AI.My_Reminder_LM().__response__(pipe=SLM, query=f"<|system|>You are a helpful AI assistant.<|end|><|user|>{self.ai_window_entry_data}<|end|><|assistant|>")

            def update_gui():
                self.ai_window_textbox.configure(state="normal")
                self.ai_window_textbox.insert(tkinter.END, f"USER:\n{self.ai_window_entry_data}\nLlama:\n{response_text}\n")
                self.ai_window_textbox.configure(state="disabled")
                self.ai_window_entry.delete(0, tkinter.END)

            self.after(0, update_gui)

        threading.Thread(target=run_model).start()

    def __audio_input__(self: typing.Self) -> None:
        try:
            self.recognizer: speech_recognition.Recognizer = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as self.source:
                self.audio_data: speech_recognition.AudioData = self.recognizer.record(self.source, duration=5)
                self.text: str = self.recognizer.recognize_google(self.audio_data)

            self.ai_window_entry.insert(f"0", self.text)

        except speech_recognition.UnknownValueError: pass
   
if __name__ == f"__main__":
    program: Program = Program()
    program.mainloop()