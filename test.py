from pynput import mouse

def mouse_click(x, y, button, pressed):
    if button == mouse.Button.left or mouse.Button.right and pressed:
        print(f'X:{x} Y:{y}')

listener = mouse.Listener(on_click=mouse_click)
listener.start()
listener.join()