import typing
from customtkinter import *
from tkinterdnd2 import *

class Tk(CTk, TkinterDnD.DnDWrapper):
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        CTk.__init__(self, *args, **kwargs)
        TkinterDnD.TkdndVersion: TkinterDnD._require = TkinterDnD._require(self)
