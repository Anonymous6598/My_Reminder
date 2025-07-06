import My_Reminder_List_note_interface, typing, customtkinter, locale, tkdrag, tkinter

class List_note(customtkinter.CTkFrame, My_Reminder_List_note_interface.My_Reminder_List_note_interface):
    WIDTH: typing.Final[int] = 300
    HEIGHT: typing.Final[int] = 300
    CORNER_RADIUS: typing.Final[int] = 5
    
    def __init__(self: typing.Self, master: typing.Any | None = None, height: int = HEIGHT, width: int = WIDTH, corner_radius: int = CORNER_RADIUS, border_width: int = 1, fg_color: str = f"transparent", *args, **kwargs) -> None:
        customtkinter.CTkFrame.__init__(self, master=master, height=height, width=width, corner_radius=corner_radius, border_width=border_width, fg_color=fg_color, *args, **kwargs)
        
        self.main_screen_note_frame_box: customtkinter.CTkScrollableFrame = customtkinter.CTkScrollableFrame(master=self, width=275, height=255, corner_radius=self.CORNER_RADIUS, fg_color=f"transparent", border_width=0)
        self.main_screen_note_frame_box.place(x=1, y=1)

        self.main_screen_add_list_note_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self.main_screen_note_frame_box, width=10, height=10, corner_radius=5, text=f"+", fg_color=(f"dark blue", f"green"), font=(f"Roman", 22), command=self.__add_list__)
        self.main_screen_add_list_note_button.grid(row=0, column=0, padx=0)
        
        self.main_screen_add_list_note_button_variable: int = 0
        
        self.main_screen_add_list_note_button_my_reminder_list_note_frame_entry_variable: int = -1

        self.main_screen_note_clear_note_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=290, text=f"обриши", fg_color=(f"dark blue", f"green"), command=self.__delete_note__)
        self.main_screen_note_clear_note_button.place(x=5, y=265)

        self.main_screen_note_frame_box_menu: tkinter.Menu = tkinter.Menu(self.main_screen_note_frame_box, tearoff=0)

        self.main_screen_note_frame_box.bind(f"<Button-3>", lambda event: self.main_screen_note_frame_box_menu.post(event.x_root, event.y_root))
        
        self.main_screen_note_clear_note_button.configure(text=f"clear")

        self.main_screen_note_frame_box_menu.add_command(label=f"new list", command=self.__add_list__)
        self.main_screen_note_frame_box_menu.add_command(label=f"clear", command=self.__delete_note__)
           
        tkdrag.Drag(self)

    @typing.override  
    def __delete_note__(self: typing.Self) -> None:
        self.destroy()
       
    @typing.override
    def __add_list__(self: typing.Self) -> None:
        self.main_screen_add_list_note_button_my_reminder_list_note_frame_entry_variable += 1
        self.main_screen_my_reminder_list_note_frame_entry: My_Reminder_list_note_frame_entry = My_Reminder_list_note_frame_entry(master=self.main_screen_note_frame_box)
        self.main_screen_my_reminder_list_note_frame_entry.grid(column=0, row=self.main_screen_add_list_note_button_my_reminder_list_note_frame_entry_variable)

        self.main_screen_add_list_note_button_variable += 1
        self.main_screen_add_list_note_button.grid(column=0, row=self.main_screen_add_list_note_button_variable, columnspan=1000, rowspan=1000)
    
class My_Reminder_list_note_frame_entry(customtkinter.CTkFrame):
    def __init__(self: typing.Self, width: int = 255, height: int = 30, *args, **kwargs) -> None:
        customtkinter.CTkFrame.__init__(self, width=width, height=height, *args, **kwargs)
        
        self.main_screen_note_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self, width=225, height=25)
        self.main_screen_note_entry.place(x=0, y=1)
        
        self.main_screen_note_remove_note_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"-", font=(f"Roman", 12), fg_color=(f"dark blue", f"green"), height=25, width=30, command=lambda: self.grid_forget())
        self.main_screen_note_remove_note_button.place(x=226, y=1)