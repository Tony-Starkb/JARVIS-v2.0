class ContextManager:
    def __init__(self):
        self.history = []

    def update(self, user_input):
        self.history.append(user_input)

    def get_recent_context(self, n=3):
        return self.history[-n:]
