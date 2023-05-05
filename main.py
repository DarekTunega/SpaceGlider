import tkinter as tk
import pyautogui
import pytesseract
import keyboard
import time

attack_speed = 2.5
ping = 0.22
x = 487
y = 1026
width = 521 - x
height = 1042 - y

windup_time = 0.2 * attack_speed
attack_delay = max(0.05, windup_time - ping)
post_attack_delay = 0.1 - windup_time
distance_to_move = 200 * attack_speed

move_key = 'a'
attack_key = 'c'

root = tk.Tk()
root.title("Orbwalker")
root.geometry("200x150")

is_running = False
is_attacking = False

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
                time.sleep(max(0, post_attack_delay))
            else:
                is_attacking = False
                if not is_running:
                    break
                else:
                    time.sleep(0.1)

def stop():
    global is_running
    is_running = False

def take_screenshot():
    global attack_speed
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save("screenshot.png")
    attack_speed_value = pytesseract.image_to_string(screenshot, config='--psm 6')
    attack_speed = float(attack_speed_value)
    print("attack speed: ", attack_speed)

play_button = tk.Button(root, text="Play", command=play)
play_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(pady=10)

screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=10)

root.mainloop()