# import PySimpleGUI as sg

from Model.model import Model

class View:
    """
    View in the MVC paradigm.
    """

    def __init__(self,
                 model: Model,
                 ) -> None:
        """
        Constructor of the View.
        """
        self.model = model
