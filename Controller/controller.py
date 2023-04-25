from View.view import View
from Model.model import Model

class Controller:
    """
    Controller in the MVC paradigm.
    """

    def __init__(self,
                 view: View,
                 model: Model,
                 ) -> None:
        """
        Constructor of the Controller.
        """
        self.model = model
        self.view = view

    def run(self):
        self.model.print_res()
    



