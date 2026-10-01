class EthicsGuard:
    def is_allowed(self, user_input):
        blocked_keywords = ["delete system32", "format c:", "hack"]

        for word in blocked_keywords:
            if word in user_input.lower():
                return False

        return True
