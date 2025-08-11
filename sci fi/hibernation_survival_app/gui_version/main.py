import tkinter as tk
from tkinter import messagebox
from game_logic import HibernationSubject

class HibernationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hibernation Survival")
        self.subject = HibernationSubject()
        
        # UI Setup
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        # Status Frame
        self.status_frame = tk.LabelFrame(self.root, text="Subject Status", padx=10, pady=10)
        self.status_frame.pack(pady=10)
        
        self.health_label = tk.Label(self.status_frame, text="", font=("Arial", 12))
        self.health_label.pack()
        
        # Actions Frame
        self.action_frame = tk.LabelFrame(self.root, text="Actions", padx=10, pady=10)
        self.action_frame.pack(pady=10)
        
        tk.Button(self.action_frame, text="Check Vitals", command=self.check_vitals).grid(row=0, column=0, padx=5)
        tk.Button(self.action_frame, text="Cut Hand", command=self.cut_hand).grid(row=0, column=1, padx=5)
        tk.Button(self.action_frame, text="Give Meds", command=self.give_meds).grid(row=0, column=2, padx=5)
        tk.Button(self.action_frame, text="Reset", command=self.reset).grid(row=1, column=0, pady=5)
        tk.Button(self.action_frame, text="Quit", command=self.root.quit).grid(row=1, column=2, pady=5)
    
    def update_display(self):
        status = self.subject.get_status()
        self.health_label.config(
            text=f"Health: {status['health']}%\nHand: {status['hand']}",
            fg="green" if status['health'] > 50 else "orange" if status['health'] > 20 else "red"
        )
    
    def check_vitals(self):
        messagebox.showinfo("Vitals", f"Health: {self.subject.health}%\nHand: {'Intact' if self.subject.hand_intact else 'Missing'}")
    
    def cut_hand(self):
        result = self.subject.cut_hand()
        messagebox.showwarning("Action", result)
        self.update_display()
        self.check_game_over()
    
    def give_meds(self):
        result = self.subject.give_meds()
        messagebox.showinfo("Action", result)
        self.update_display()
    
    def reset(self):
        self.subject.reset()
        self.update_display()
    
    def check_game_over(self):
        if self.subject.health <= 0:
            messagebox.showerror("Game Over", "💀 Subject has died!")
            self.reset()

if __name__ == "__main__":
    root = tk.Tk()
    app = HibernationApp(root)
    root.mainloop()