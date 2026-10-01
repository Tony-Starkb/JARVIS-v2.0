import psutil

def is_app_running(app_name):
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] and app_name.lower() in process.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


if __name__ == "__main__":
    app_to_check = "notepad"  # Change this to the desired application name
    if is_app_running(app_to_check):
        print(f"{app_to_check} is currently running.")
    else:
        print(f"{app_to_check} is not running.")