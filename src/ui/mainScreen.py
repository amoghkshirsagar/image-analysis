import customtkinter as ctk
import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame

from src.ui.appContent import addAppContent

def buildAppUi():
    app: CTk = ctk.CTk()
    app.geometry("900x800")
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    addAppContent(app)

    app.mainloop()