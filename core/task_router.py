import os
import sys
import datetime
import webbrowser

# Import UIAppController - support both package and direct script execution.
try:
    from capabilities.apps.ui_app_controller import UIAppController
except ModuleNotFoundError:
    # If running the file directly (e.g., `python core/task_router.py`) the project root
    # may not be on sys.path. Add the parent directory (project root) and retry.
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from capabilities.apps.ui_app_controller import UIAppController
try:
    from capabilities.apps.notepad.notepad_file import NotepadAutomation
except ModuleNotFoundError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    from capabilities.apps.notepad.notepad_file import NotepadAutomation
    

class TaskRouter:
    def __init__(self):
        self.notepad = NotepadAutomation()
    
    def route(self, intent_data):
        intent = intent_data["intent"]

        if intent == "open_app":
            return self.open_app(intent_data["app"])
        
        if intent == "close_app":
            return self.close_app(intent_data["app"])

        if intent == "get_time":
            return self.get_time()

        if intent == "shutdown":
            return "Shutdown command received (disabled for safety)."
        
        if intent == "sleep":
            return "Sleep command received (disabled for safety)."
        
        if intent == "app_action":
            return self.handle_app_action(intent_data)
        
        return "I didn't understand that."
    
    def handle_app_action(self, intent_data):
        app = intent_data.get("app")
        action = intent_data.get("action")

        if app == "notepad":
            return self.notepad.execute(action, **intent_data)

        return f"No handler for app action: {app}"

    
    def open_app(self, app_name):
        app_controller = UIAppController(app_name)
        app_controller.open_App()
        return f"Attempted to open {app_name}."
    
    def close_app(self, app_name):
        app_controller = UIAppController(app_name)
        app_controller.close_App()
        return f"Attempted to close {app_name}."

    def get_time(self):
        return datetime.datetime.now().strftime("Current time: %H:%M:%S")