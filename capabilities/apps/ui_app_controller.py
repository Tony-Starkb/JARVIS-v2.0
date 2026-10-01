"""
Here in this file, we will write the functionality/code to give the jarvis the ability to 
fully control simple UI Windows applications like writing, saving, opening files and each and everything 
that an app can do or we can do using keyboard shortcuts.

This module normalizes app names, checks for running processes more robustly, and handles
common launch errors (missing executable, UWP apps, etc.).
"""

# Import necessary modules for controlling apps
import pyautogui
import time
import os
import subprocess
import shutil

# Prefer package-relative import when used as a package; fall back when run directly.
try:
    from .check_If_App_Is_Open import is_app_running
except (ImportError, ModuleNotFoundError):
    from check_If_App_Is_Open import is_app_running

class UIAppController:
    def __init__(self, app_name):
        # Normalize app name and keep variants
        self.app_name = app_name
        self.app_basename = os.path.basename(self.app_name)
        self.app_name_no_ext = os.path.splitext(self.app_basename)[0]
        self.process = None

    def open_App(self):
        # Check by process name without extension for a more reliable test
        '''
        if is_app_running(self.app_name_no_ext):
            print(f"{self.app_basename} is already running.")
            return
        '''
        # Try to launch executable if available on PATH
        try:
            if shutil.which(self.app_basename):
                self.process = subprocess.Popen([self.app_basename])
                time.sleep(1)  # Wait for Application to open
                print(f"Opened {self.app_basename} (via executable).")
                return

            # As a fallback, try os.startfile (Windows) for registered apps/files
            try:
                os.startfile(self.app_basename)
                time.sleep(1)
                print(f"Opened {self.app_basename} (via os.startfile).")
                return
            except Exception:
                # Last resort: use shell start (Windows cmd)
                try:
                    subprocess.Popen(self.app_basename, shell=True)
                    time.sleep(1)
                    print(f"Opened {self.app_basename} (via shell).")
                    return
                except FileNotFoundError:
                    raise

        except FileNotFoundError:
            print(f"Executable '{self.app_basename}' not found. Try using the correct executable name (e.g. 'calc.exe' for Calculator).")
        except Exception as e:
            print(f"Failed to open '{self.app_basename}': {e}")





    def close_App(self):
        # Prefer to terminate the process if we started it and it's still running
        
        if self.process:
            if self.process.poll() is None:
                try:
                    self.process.terminate()
                    self.process.wait(timeout=2)
                    print(f"Terminated {self.app_basename} (via process handle).")
                    return
                except Exception:
                    pass

        # Fallback: send Alt+F4 to the active window
        if not is_app_running(self.app_name_no_ext):
            print(f"{self.app_basename} is not running.")
            return
        else:
            os.system(f'taskkill /IM {self.app_basename}.exe /F')
            time.sleep(0.5)
            # pyautogui.press('n')  # Press 'N' for "Don't Save" if prompted
            print(f"Requested {self.app_basename} to close has executed.")
            
            
    def minimize_App(self):
        # use this function to minimize the app if it is running
        
        if is_app_running(self.app_name_no_ext):
            pyautogui.hotkey('win', 'down')
            return
        else:
            print(f"{self.app_basename} is not running.")

    def maximize_App(self):
        # use this function to maximize the app if it is running
        
        if is_app_running(self.app_name_no_ext):
            pyautogui.hotkey('win', 'up')
            return
        else:
            print(f"{self.app_basename} is not running.")


if __name__ == "__main__":
    print("Select one from the list:")

    print("1. notepad.exe (Notepad)")
    print("2. calc.exe (Calculator)")
    print("3. wordpad.exe (WordPad)")
    print("4. mspaint.exe (Paint)")
    print("5. explorer.exe (File Explorer)")
    print("6. control.exe (Control Panel)")
    print("7. wmplayer.exe (Windows Media Player)")
    print("8. SnippingTool.exe (Snipping Tool)")
    print("9. Chrome")

    user_input = input("Enter the application number you want to control: ")

    if user_input == "1":
        input_app = "notepad.exe"
    elif user_input == "2":
        # Use the traditional executable name for Calculator
        input_app = "calc.exe"
    elif user_input == "3":
        input_app = "wordpad.exe"
    elif user_input == "4":
        input_app = "mspaint.exe"
    elif user_input == "5":
        input_app = "explorer.exe"
    elif user_input == "6":
        input_app = "control.exe"
    elif user_input == "7":
        input_app = "wmplayer.exe"
    elif user_input == "8":
        input_app = "SnippingTool.exe"
    elif user_input == "9":
        input_app = "chrome"
    else:
        print("Invalid selection. Exiting.")
        raise SystemExit(1)

    controller = UIAppController(input_app)
    print("Select any one option:")
    print("1. Open Application")
    print("2. Close Application")
    print("3. Minimize Application")
    print("4. Maximize Application")
    print("5. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            controller.open_App()
        elif choice == '2':
            controller.close_App()
            break
        elif choice == '3':
            controller.minimize_App()
        elif choice == '4':
            controller.maximize_App()
        elif choice == '5':
            break