import pyautogui as lazyGui
import time as lazyTime

largura, altura = lazyGui.size()

lazyGui.moveTo(largura / 2, altura / 2)
lazyGui.click()
lazyTime.sleep(1)

lazyGui.hotkey("command", "space")
lazyGui.typewrite("whatsapp")
lazyGui.press("enter")

lazyTime.sleep(2)

search_box_location = lazyGui.locateOnScreen('lazyReferences/whatsapp-search.png', confidence=0.9)
message_input = lazyGui.locateOnScreen('lazyReferences/message-input.png', confidence=0.6)

if search_box_location is not None:
    # x, y, width, height = search_box_location
    # center_x = x + (width / 2)
    # center_y = y + (height / 2)

    # lazyGui.moveTo(center_x, center_y)
    # lazyGui.click()
    # # lazyGui.typewrite("Lucas Mordzin")
    # lazyTime.sleep(2)
    # lazyGui.press("enter")

    x2, y2, width2, height2 = message_input
    center_x_2 = x2 + (width2 / 2)
    center_y_2 = y2 + (height2 / 2)

    lazyGui.moveTo(center_x_2, center_y_2)
    lazyGui.click()
    lazyGui.typewrite("Acho que foi hein?")
    lazyGui.press("enter")
else:
    print("Campo de pesquisa não encontrado")
