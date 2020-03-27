#!/usr/bin/env python


# imports
try:
    from pynput import mouse, keyboard
except ModuleNotFoundError:
    print("Your python does not have pynput installed. Let us change that...")
    import os
    os.system("pip install pynput")
    print("...done.")
    from pynput import mouse, keyboard


# listeners
def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            keyboard_controller.press(keyboard.Key.left)
            keyboard_controller.release(keyboard.Key.left)
            print("Left")
        if button == mouse.Button.right:
            keyboard_controller.press(keyboard.Key.right)
            keyboard_controller.release(keyboard.Key.right)
            print("Right")

def on_scroll(x, y, dx, dy):
    if dy > 0:  # up
        keyboard_controller.press(keyboard.Key.up)
        print("Uuu...")
    else:  # down
        keyboard_controller.release(keyboard.Key.up)
        print("...up")


# main
keyboard_controller = keyboard.Controller()
with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll) as mouse_listener:
    print("Macro launched. Happy One Step From Eden run :)")
    # wait until mouse_listener.stop called or StopException raised or on_* returns False
    mouse_listener.join()
    # clean keys that are still down
    keyboard.release(keyboard.Key.up)