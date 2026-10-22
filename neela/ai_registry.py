class AIRegistry:
    def __init__(self):
        self.models = {}

    def register(self, name, model):
        self.models[name] = model

    def get_model(self, name):
        return self.models.get(name, None)

registry = AIRegistry()