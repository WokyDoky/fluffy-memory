import subprocess
import winreg
import subprocess
import pyautogui

#This is my way of doing it before going into winreg and changing the varible there
#This opens sysdm.cpl>>environment variables
subprocess.Popen("rundll32.exe sysdm.cpl,EditEnvironmentVariables", shell=True)
#Click the var that you want
var_loc = pyautogui.locateOnScreen('1999.png')
pyautogui.click(var_loc.left + var_loc.width / 2, var_loc.top + var_loc.height / 2)
#TODO
#Add so it click "edit"
edit_loc = pyautogui.locateOnScreen('edit.png')
pyautogui.click(edit_loc.left + edit_loc.width / 2, edit_loc.top + edit_loc.height / 2)
#Inputs the correct var and applies the changes
#I will add a ctrl a so it deletes everything
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('a')
pyautogui.keyUp('ctrl')
pyautogui.keyDown('backspace')
pyautogui.keyUp('backspace')

pyautogui.typewrite('1999@engsrvls01.utep.edu')

#Click apply
apply_loc = pyautogui.locateOnScreen('apply.png')
pyautogui.click(apply_loc.left + apply_loc.width / 2, apply_loc.top + apply_loc.height / 2)
#kill the code

#This changes the varible from windows reg


# Set the new value of the Path variable
#new_path_value = "C:\NewDirectory"

# Open the Environment Variables key in the Windows Registry
#reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\Session Manager\Environment", 0, winreg.KEY_ALL_ACCESS)

# Set the new value of the Path variable in the Windows Registry
#winreg.SetValueEx(reg, "Path", 0, winreg.REG_EXPAND_SZ, new_path_value)

# Close the Windows Registry key
#winreg.CloseKey(reg)

# Open the "Environment Variables" window in the "System Properties" window
#subprocess.Popen("rundll32.exe sysdm.cpl,EditEnvironmentVariables", shell=True)