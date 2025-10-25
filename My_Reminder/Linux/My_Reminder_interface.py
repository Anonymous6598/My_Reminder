import abc, typing

class My_Reminder_interface(abc.ABC):
    @abc.abstractmethod
    def __create_note__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __create_list_note__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __create_list_note__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __fullscreen__(self: typing.Self, event: str | None = None) -> None:
        pass
