'''
In this file(notepad_file.py), I will try to create the code using which i can automate 
all the features of the file menu of notepad application using pyautogui library.
Tasks to be Automated:
- new(ctrl + n)
- new window(ctrl + shift + n)
- open(ctrl + o)
- save(ctrl + s)
- save as(ctrl + shift + s)
- page setup(alt + f)
- print(ctrl + p)
- exit(alt + f4)

'''

"""
Notepad Automation Module
Automates common Notepad operations using keyboard shortcuts
"""

import pyautogui
import time
import subprocess
import os

class NotepadAutomation:
    """Class to automate Windows Notepad operations"""
    
    def __init__(self):
        """Initialize the Notepad automation class"""
        self.notepad_process = None
        pyautogui.FAILSAFE = True  # Move mouse to corner to abort
        pyautogui.PAUSE = 0.5  # Pause between actions
        
    def execute(self, action, **kwargs):
        if action == "new":
            return self.new_file()
        elif action == "new window":
            return self.new_window()
        elif action == "open":
            return self.open_file(kwargs.get("filepath"))
        elif action == "save":
            return self.save_file()
        elif action == "save as":
            return self.save_as(kwargs.get("filepath"))
        elif action == "print":
            return self.print_file()
        elif action == "exit":
            return self.exit_notepad()
        elif action == "type":
            return self.type_text(kwargs.get("text"))
        else:
            raise ValueError(f"Unknown notepad action: {action}")

    
    '''
    def launch_notepad(self):
        """Launch Notepad application"""
        try:
            self.notepad_process = subprocess.Popen(['notepad.exe'])
            time.sleep(1)  # Wait for Notepad to open
            print("Notepad launched successfully")
            return True
        except Exception as e:
            print(f"Error launching Notepad: {e}")
            return False
    '''
    
    def new_file(self):
        """Create a new file using Ctrl + N"""
        try:
            pyautogui.hotkey('ctrl', 'n')
            print("New file created (Ctrl + N)")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error creating new file: {e}")
            return False
    
    def new_window(self):
        """Open a new Notepad window using Ctrl + Shift + N"""
        try:
            pyautogui.hotkey('ctrl', 'shift', 'n')
            print("New window opened (Ctrl + Shift + N)")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error opening new window: {e}")
            return False
    
    def open_file(self, filepath=None):
        """
        Open a file using Ctrl + O
        
        Args:
            filepath: Optional path to the file to open
        """
        try:
            pyautogui.hotkey('ctrl', 'o')
            print("Open dialog triggered (Ctrl + O)")
            time.sleep(1)
            
            if filepath and os.path.exists(filepath):
                pyautogui.write(filepath, interval=0.05)
                pyautogui.press('enter')
                print(f"File opened: {filepath}")
            else:
                print("Waiting for manual file selection...")
            
            return True
        except Exception as e:
            print(f"Error opening file: {e}")
            return False
    
    def save_file(self):
        """Save the current file using Ctrl + S"""
        try:
            pyautogui.hotkey('ctrl', 's')
            print("File saved (Ctrl + S)")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def save_as(self, filepath=None):
        """
        Save file with a new name using Ctrl + Shift + S
        
        Args:
            filepath: Optional path for saving the file
        """
        try:
            pyautogui.hotkey('ctrl', 'shift', 's')
            print("Save As dialog triggered (Ctrl + Shift + S)")
            time.sleep(1)
            
            if filepath:
                pyautogui.write(filepath, interval=0.05)
                pyautogui.press('enter')
                print(f"File saved as: {filepath}")
            else:
                print("Waiting for manual file naming...")
            
            return True
        except Exception as e:
            print(f"Error in Save As: {e}")
            return False
    
    def page_setup(self):
        """Open page setup dialog using Alt + F (File menu)"""
        try:
            pyautogui.hotkey('alt', 'f')
            time.sleep(0.3)
            pyautogui.press('u')  # Press 'u' for Page Setup
            print("Page setup opened (Alt + F)")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error opening page setup: {e}")
            return False
    
    def print_file(self):
        """Open print dialog using Ctrl + P"""
        try:
            pyautogui.hotkey('ctrl', 'p')
            print("Print dialog opened (Ctrl + P)")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error opening print dialog: {e}")
            return False
    
    def exit_notepad(self):
        """Exit Notepad using Alt + F4"""
        try:
            pyautogui.hotkey('alt', 'F4')
            print("Notepad exit triggered (Alt + F4)")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error exiting Notepad: {e}")
            return False
    
    def type_text(self, text):
        """
        Type text into Notepad
        
        Args:
            text: String to type into Notepad
        """
        try:
            pyautogui.write(text, interval=0.05)
            print(f"Text typed: {text[:50]}...")
            return True
        except Exception as e:
            print(f"Error typing text: {e}")
            return False
