
import tkinter as tk
from threading import Thread
import time

class TrafficLight:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Traffic Light")
        self.label = tk.Label(self.root, text="Traffic Light", font=("Helvetica", 24))
        self.label.pack()
        self.light = tk.Label(self.root, text="", font=("Helvetica", 64))
        self.light.pack()
        self.thread = Thread(target=self.change_light)
        self.thread.start()

    def change_light(self):
        colors = ["Red", "Yellow", "Green"]
        for color in colors:
            self.light.config(text=color, fg=color)
            if color == "Red":
                time.sleep(5)
            elif color == "Yellow":
                time.sleep(2)
            else:
                time.sleep(5)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.run()
