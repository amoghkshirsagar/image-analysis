import customtkinter as ctk
import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkProgressBar, CTkScrollableFrame, filedialog, CTkTextbox
from threading import Thread

from src.ai.agent import Agent

class ChatApp:
    def __init__(self, parent):
        self.parent = parent
        self.ollamaAgent = Agent("ollama", "llama3.2-vision")
        self.img_file_path = None
        self.create_ui()
    
    def create_ui(self):
        self.entryBoxRow = ctk.CTkFrame(self.parent, fg_color="#00224B", height=50)
        self.entryBoxRow.grid(row=6, column=1, sticky="SEW", padx=5, pady=5)
        self.entryBoxRow.columnconfigure(2, weight=1)

        self.command = ctk.CTkTextbox(self.entryBoxRow, height=100, width=600)
        self.command.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.buttons = ctk.CTkFrame(self.entryBoxRow, fg_color="#00224B")
        self.buttons.grid(row=1, column=2, sticky="NSEW", padx=5, pady=5)

        self.open_button = ctk.CTkButton(self.buttons, text="Open File", command=self.open_file)
        self.open_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.sendToAiButton = CTkButton(self.buttons, text="Send ↑", command=self.sendprompt)
        self.sendToAiButton.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        # Status Bar
        self.statusBar = ctk.CTkFrame(self.parent, fg_color="#001B3A", height=20)
        self.statusBar.grid(row=7, column=1, sticky="SEW", padx=5, pady=5)
        self.statusBar.columnconfigure(0, weight=1)
        
        self.status_message = CTkLabel(self.statusBar, text="Status: Ready", anchor="w")
        self.status_message.grid(row=0, column=0, sticky="W", padx=5)
        
        self.progress_bar = CTkProgressBar(self.statusBar)
        self.progress_bar.grid(row=0, column=1, sticky="WE", padx=3)
        self.progress_bar.set(0)  # Initialize progress to 0
    
    def sendprompt(self):
        image = self.img_file_path
        command_text = self.command.get("1.0", tk.END)
        self.update_status("Processing...", 0.5)
        
        def task():
            response = self.ollamaAgent.sendCommandAndGetResponse(command_text, image)
            self.parent.after(0, lambda: self.update_status("Done", 1.0))
            self.parent.after(0, lambda: self.showResponse(response))
        
        thread = Thread(target=task)
        thread.start()
    
    def open_file(self):
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All Files", "*.*")])
        self.img_file_path = file_path
    
    def showResponse(self, response):
        responseBox = ctk.CTkScrollableFrame(self.parent, fg_color="#00224B")
        responseBox.grid(row=1, column=1, sticky="NSEW", padx=5, pady=5)
        responseBox.columnconfigure(1, weight=1)
        
        responseDisplay = CTkLabel(responseBox, fg_color="#001B3A", text=response, width=600)
        responseDisplay.grid(row=0, column=1, sticky="NSEW", padx=10, pady=5)
    
    def update_status(self, message, progress):
        self.status_message.configure(text=f"Status: {message}")
        self.progress_bar.set(progress)