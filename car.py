from engine.Engine import Engine
from battery.Battery import Battery
from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
    def needs_service(self):
        return self.engine.needs_service() and self.battery.needs_service()
    
