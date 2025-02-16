import customtkinter as ctk
import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame, filedialog, CTkTextbox
import ollama

from src.ai.agent import Agent

ollamaAgent: Agent = Agent("ollama", "llama3.2-vision")

img_file_path = None

def chatUI(parent):
    entryBoxRow = ctk.CTkFrame(parent, fg_color="#00224B",  height= 50)
    entryBoxRow.grid(row=6, column=1, sticky="SEW", padx=5, pady=5)
    entryBoxRow.columnconfigure(3, weight=1)

    inputList = {
        "command": {"label": "Command", "entry": None}}


    for i, (key, value) in enumerate(inputList.items()):
        value['label'] = ctk.CTkTextbox(entryBoxRow, height=100, width=600)
        value['label'].grid(row=1, column=i+1, sticky="ew", padx=5, pady=20)

    open_button = ctk.CTkButton(entryBoxRow, text="Open File", command=lambda: open_file())
    open_button.grid(row=1, column=3, sticky="ew", padx=5)

    sendToAiButton: CTkButton = ctk.CTkButton(entryBoxRow, text="Send ↑", command=lambda: sendprompt(inputList, parent))
    sendToAiButton.grid(row=1, column=4, sticky="ew", padx=5)

def sendprompt(inputList, parent):
    image = img_file_path
    print(img_file_path)
    command = inputList["command"]["label"]

    prompt = f"""Given image, analyze and answer the following question:
    {command.get("1.0", tk.END)}

    Answer only question in short, clear and concise.
    Do not include any additional information.
    """
    response = ollamaAgent.getResponse(prompt, image)

    showResponce(parent, response)


def open_file():
    # Open file dialog and get the file path
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All Files", "*.*")])
    global img_file_path 
    img_file_path = file_path

def showResponce(parent, response):
    responseBox = ctk.CTkScrollableFrame(parent, fg_color="#00224B",  height= 50)
    responseBox.grid(row=1, column=1, sticky="NSEW", padx=5, pady=5)
    responseBox.columnconfigure(3, weight=1)
    
    responceDisplay: CTkLabel = ctk.CTkLabel(responseBox, fg_color="#001B3A", text=response)
    responceDisplay.grid(row=0, column=0, sticky="NSEW", padx=10, pady=5)