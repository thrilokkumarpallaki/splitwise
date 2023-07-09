from abc import ABC


class ICommand(ABC):
    """
    A Command abstract class which acts like a blueprint to its concrete classes.
    """
    @classmethod
    def match(cls, cmd_input: str) -> bool:
        """
        This method takes the console input parameters and checks all the required parameters are
        passed or not.
        :param cmd_input: A command line input
        :return: A boolean values representing match is successful or not.
        """
        pass

    @classmethod
    def execute(cls, cmd_input: str):
        """
        This method actually performs the command execution by calling appropriate methods.
        :param cmd_input: A command line input
        :return: None
        """
        pass
