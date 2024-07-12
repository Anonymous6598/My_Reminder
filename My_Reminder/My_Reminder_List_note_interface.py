import abc, typing

class My_Reminder_List_note_interface(abc.ABC):  
    @abc.abstractmethod
    def __delete_note__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __add_list__(self: typing.Self) -> None:
        pass  