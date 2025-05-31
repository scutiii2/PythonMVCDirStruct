from views import View
from models import Model

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()
        self.initialize()
        
    def initialize(self):
        self.view.initialize()
        self.model.initialize()
        
    def update(self):
        self.model.preupdate()
        self.view.preupdate()
        
        self.model.update()
        self.view.update()
        
        self.model.postupdate()
        self.view.postupdate()