# import eventmanager
# import model
from Model.model import Model
from View.view import View
from Controller.controller import Controller
# import controller

def run():
    model = Model()
    view = View(model)
    controller = Controller(view, model)
    controller.run()
    # evManager = eventmanager.EventManager()
    # gamemodel = model.GameEngine(evManager)
    # keyboard = controller.Keyboard(evManager, gamemodel)
    # graphics = view.GraphicalView(evManager, gamemodel)
    # gamemodel.run()

if __name__ == '__main__':
    run()