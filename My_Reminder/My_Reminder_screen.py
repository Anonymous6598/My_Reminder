import customtkinter, tkinterdnd2, typing

class Window(customtkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)
        tkinterdnd2.TkinterDnD.TkdndVersion: tkinterdnd2.TkinterDnD._require = tkinterdnd2.TkinterDnD._require(self)
