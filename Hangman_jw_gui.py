import tkinter as tk
import random

# Word bank
words = [
    "pointer", "cluster", "context", "cookies", "channel", "instance", "dynamic", "argument", "developer", "database",
    "python", "canvas", "coding", "network", "compile", "debugger", "boolean", "iterate", "syntax", "variable",
    "machine", "function", "object", "inherit", "exception", "thread", "package", "pipeline", "gateway", "integer",
    "parameter", "terminal", "platform", "storage", "digital", "virtual", "library", "command", "execute", "frontend",
    "backend", "framework", "element", "segment", "module", "process", "runtime", "encrypt", "decrypt", "version",
    "timeout", "session", "adapter", "binding", "desktop", "driver", "input", "output", "logging", "mapping",
    "numeric", "pattern", "queue", "record", "render", "router", "scalar", "schema", "script", "secure",
    "server", "socket", "source", "static", "string", "system", "token", "update", "upload", "vector",
    "window", "worker", "wrapper", "zipfile", "lambda", "debug", "float", "double", "class", "method",
    "array", "index", "loop", "case", "break", "catch", "throw", "finally", "super", "constructor"
]

random.shuffle(words)

class RopeEscapeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🪢 Rope Escape - Jumbled Word Challenge")
        self.level = 0
        self.max_levels = len(words)

        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack(pady=10)

        self.level_label = tk.Label(root, text=f"Level {self.level + 1}/100", font=("Arial", 16))
        self.level_label.pack()

        self.word = words[self.level]
        self.jumbled = self.jumble_word(self.word)
        self.word_label = tk.Label(root, text=self.jumbled, font=("Courier", 28), fg="blue")
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 18), justify="center")
        self.entry.pack(pady=10)

        self.submit_btn = tk.Button(root, text="Submit", font=("Arial", 14), command=self.check_answer)
        self.submit_btn.pack(pady=5)

        self.feedback = tk.Label(root, text="", font=("Arial", 14))
        self.feedback.pack(pady=10)

        self.draw_rope()

    def jumble_word(self, word):
        letters = list(word)
        while True:
            random.shuffle(letters)
            jumbled = ''.join(letters)
            if jumbled != word:
                return jumbled

    def draw_rope(self):
        self.canvas.delete("all")
        # Rope and stickman hanging
        self.canvas.create_line(200, 20, 200, 80, width=4)  # Rope
        self.canvas.create_oval(180, 80, 220, 120, width=2)  # Head
        self.canvas.create_line(200, 120, 200, 180, width=2)  # Body
        self.canvas.create_line(200, 130, 170, 160, width=2)  # Left Arm
        self.canvas.create_line(200, 130, 230, 160, width=2)  # Right Arm
        self.canvas.create_line(200, 180, 180, 230, width=2)  # Left Leg
        self.canvas.create_line(200, 180, 220, 230, width=2)  # Right Leg

    def clear_stickman(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 150, text="😮‍💨 He Escaped!", font=("Arial", 24), fill="green")

    def draw_dead(self):
        self.canvas.delete("all")
        self.canvas.create_line(200, 20, 200, 80, width=4)
        self.canvas.create_oval(180, 80, 220, 120, width=2, fill="red")
        self.canvas.create_line(200, 120, 200, 180, width=2)
        self.canvas.create_line(200, 130, 170, 160, width=2)
        self.canvas.create_line(200, 130, 230, 160, width=2)
        self.canvas.create_line(200, 180, 180, 230, width=2)
        self.canvas.create_line(200, 180, 220, 230, width=2)
        self.canvas.create_text(200, 260, text="💀 He didn't make it...", font=("Arial", 16), fill="red")

    def check_answer(self):
        guess = self.entry.get().strip().lower()
        if guess == self.word:
            self.feedback.config(text="✅ Correct! He Escaped!", fg="green")
            self.clear_stickman()
            self.level += 1
            self.entry.delete(0, tk.END)
            if self.level < self.max_levels:
                self.root.after(1500, self.next_level)
            else:
                self.word_label.config(text="🎉 You Rescued All Stickmen!")
                self.entry.config(state="disabled")
                self.submit_btn.config(state="disabled")
        else:
            self.feedback.config(text="❌ Wrong! He got hanged...", fg="red")
            self.draw_dead()
            self.entry.config(state="disabled")
            self.submit_btn.config(state="disabled")

    def next_level(self):
        self.word = words[self.level]
        self.jumbled = self.jumble_word(self.word)
        self.word_label.config(text=self.jumbled)
        self.level_label.config(text=f"Level {self.level + 1}/100")
        self.feedback.config(text="")
        self.entry.config(state="normal")
        self.submit_btn.config(state="normal")
        self.draw_rope()
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x550")
    game = RopeEscapeGame(root)
    root.mainloop()
# This code implements a simple jumbled word game with a rope escape theme using Tkinter.