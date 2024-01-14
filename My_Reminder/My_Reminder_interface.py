import abc, typing, pickle

class My_Reminder_interface(abc.ABC):
    @abc.abstractmethod
    def __create_note__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __settigs__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __change_language__(self: typing.Self,  pickle_serialization: pickle) -> None:
        pass