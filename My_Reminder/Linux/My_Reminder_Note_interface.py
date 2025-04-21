import abc, typing

class My_Reminder_Note_interface(abc.ABC):
    @abc.abstractmethod
    def __open_note__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __save_note__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __delete_note__(self: typing.Self) -> None:
        pass