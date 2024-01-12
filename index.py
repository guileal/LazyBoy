import pyautogui as lazyGui
import time as lazyTime

largura, altura = lazyGui.size()

lazyGui.moveTo(largura / 2, altura / 2)

lazyGui.click()

lazyTime.sleep(1)


lazyGui.shortcut("command", "space")
lazyGui.typewrite("whatsapp")
lazyGui.keyDown("enter")



