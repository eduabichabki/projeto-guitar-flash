import pyautogui
import keyboard

while keyboard.is_pressed("1") == False:
    if pyautogui.pixelMatchesColor(1373,630, (0,152,0)):
        pyautogui.press("a")
    if pyautogui.pixelMatchesColor(1373,630, (255,0,0)):
        pyautogui.press("s")
    if pyautogui.pixelMatchesColor(1373,630, (244,244,2)):
        pyautogui.press("j")
