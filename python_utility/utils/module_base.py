from injector import Binder, Module, SingletonScope

class ModuleBase(Module):
    def __init__(self, model_class, view_class, controller_class):
        self.model_class = model_class
        self.view_class = view_class
        self.controller_class = controller_class

    def configure(self, binder: Binder):
        binder.bind(self.model_class, scope=SingletonScope)
        binder.bind(self.view_class, scope=SingletonScope)
        binder.bind(self.controller_class, scope=SingletonScope)