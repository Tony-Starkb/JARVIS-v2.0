

from email.mime import text


class IntentParser:
    def parse(self, text):
        text = text.lower()

# App ope/close actions

        if "open" in text and "chrome" in text:
            return {"intent": "open_app", "app": "chrome"}
        
        if "open" in text and "youtube" in text:
            return {"intent": "open_app", "app": "youtube"}
        
        if "open" in text and "notepad" in text:
            return {"intent": "open_app", "app": "notepad"}
        
        if "open" in text and "wordpad" in text:
            return {"intent": "open_app", "app": "wordpad"}
        
        if "open" in text and "mspaint" in text:
            return {"intent": "open_app", "app": "mspaint"}
        
        if "open" in text and "calculator" in text:
            return {"intent": "open_app", "app": "calculator"}
        
        if "open" in text and "this pc" in text:
            return {"intent": "open_app", "app": "explorer"}
        
        if "open" in text and "control" in text:
            return {"intent": "open_app", "app": "control"}
        
        if "open" in text and "music player" in text:
            return {"intent": "open_app", "app": "wmplayer"}
        
        if "open" in text and "snippingtool" in text:
            return {"intent": "open_app", "app": "snippingtool"}

        if "close" in text and "chrome" in text:
            return {"intent": "close_app", "app": "chrome"}
        
        if "close" in text and "notepad" in text:
            return {"intent": "close_app", "app": "notepad"}

        if "close" in text and "wordpad" in text:
            return {"intent": "close_app", "app": "wordpad"}

        if "close" in text and "mspaint" in text:
            return {"intent": "close_app", "app": "mspaint"}
        
        if "close" in text and "calculator" in text:
            return {"intent": "close_app", "app": "calculator"}
        
        if "close" in text and "this pc" in text:
            return {"intent": "close_app", "app": "explorer"}
        
        if "close" in text and "control" in text:
            return {"intent": "close_app", "app": "control"}
        
        if "close" in text and "music player" in text:
            return {"intent": "close_app", "app": "wmplayer"}
        
        if "close" in text and "snippingtool" in text:
            return {"intent": "close_app", "app": "snippingtool"}
    
        if "shutdown" in text:
            return {"intent": "shutdown"}

        if "time" in text:
            return {"intent": "get_time"}
        
        if "sleep" in text:
            return {"intent": "sleep"}
        
        if "scroll" in text and "up" in text:
            return {"intent": "scroll", "direction": "up"}
        
        if "scroll" in text and "down" in text:
            return {"intent": "scroll", "direction": "down"}

# In App actions

        if "notepad" in text and "type" in text:
            return {
                "intent": "app_action",
                "app": "notepad",
                "action": "type",
                "text": text.replace("type", "").replace("in notepad", "").strip()
            }

        if "save" in text and "notepad" in text:
            return {
                "intent": "app_action",
                "app": "notepad",
                "action": "save"
            }

        if "new file" in text and "notepad" in text:
            return {
                "intent": "app_action",
                "app": "notepad",
                "action": "new"
            }

        if "close" in text and "notepad" in text:
            return {
                "intent": "app_action",
                "app": "notepad",
                "action": "exit"
            }


        return {"intent": "unknown"}
