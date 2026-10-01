from core.context_manager import ContextManager
from core.intent_parser import IntentParser
from core.task_router import TaskRouter
from core.ethics_guard import EthicsGuard

class Brain:
    def __init__(self):
        self.context = ContextManager()
        self.intent_parser = IntentParser()
        self.router = TaskRouter()
        self.ethics = EthicsGuard()

    def process(self, user_input):
        # Step 1: Ethics check
        if not self.ethics.is_allowed(user_input):
            return "I cannot perform that action."

        # Step 2: Update context
        self.context.update(user_input)

        # Step 3: Understand intent
        intent_data = self.intent_parser.parse(user_input)

        # Step 4: Route task
        result = self.router.route(intent_data)

        return result
