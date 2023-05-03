import time
import tkinter as tk
import pyautogui
import keyboard

# set attack speed and ping
attack_speed = 1.07
ping = 0.22  # in seconds

# calculate windup time
windup_time = 0.2 / attack_speed

# calculate attack delay and post attack delay
attack_delay = max(0.05, windup_time - ping)
post_attack_delay = 0.1 - windup_time

# calculate distance to move between attacks
distance_to_move = 200 * attack_speed

# set key bindings
move_key = 'a'
attack_key = 'c'

# initialize GUI
root = tk.Tk()
root.title("Orbwalker")
root.geometry("200x150")

is_running = False

def play():
    global is_running
    is_running = True
    is_attacking = False
    while True:
        if keyboard.is_pressed('space'):
            if not is_attacking:
                keyboard.press(attack_key)
                keyboard.release(attack_key)
                time.sleep(attack_delay)
                is_attacking = True
            else:
                keyboard.press(move_key)
                keyboard.release(move_key)
                time.sleep(distance_to_move / 1000)
                keyboard.press(attack_key)
                keyboard.release(attack_key)
                time.sleep(attack_delay)
                is_attacking = False
            time.sleep(post_attack_delay)
        else:
            if not is_running:
                break
            else:
                time.sleep(0.1)  # small delay to reduce CPU usage

def stop():
    global is_running
    is_running = False

play_button = tk.Button(root, text="Play", command=play)
play_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(pady=10)

# create Take Screenshot button
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=10)

root.mainloop()
