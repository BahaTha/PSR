import socket
import tkinter
import tkinter.messagebox
import customtkinter
import sys

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.title("Soukra Bank")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Bank of Soukra",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Debit",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Credit",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="withdraw an invoice",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")


        # ============ frame_right ============

        # ============ frame_info ============

        # configure grid layout (1x1)


        # ============ frame_right ============

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Enter your Code")
        self.entry.grid(row=1, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Type the amount")
        self.entry.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Debit",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_1.grid(row=3, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Credit",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_2.grid(row=3, column=2, columnspan=1, pady=20, padx=20, sticky="we")
        self.button_3 = customtkinter.CTkButton(master=self.frame_right,
                                                text="withdraw an invoice",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_3.grid(row=3, column=3, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.switch_2.select()

        #self.slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
        #self.radio_button_3.configure(state=tkinter.DISABLED)
        #self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        #self.check_box_2.select()

    def button_event(self):
        print("Button pressed")

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()



def main_client():
    print("choisissez l'operation a executer")
    print("1. operation de depot")
    print("2. operation de retrait")
    choix=input("valeur de choix")
    if (choix=="1"):
        montant=input("saisir le montant a deposer")
        return(montant)
    
    elif(choix=="2"):
        montant=input("saisir le montant a retirer")
        return(montant)
    else: return(-1)
if __name__ == "__main__":
    app = App()
    app
    while True:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect(("192.168.1.1", 50000))
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect(("192.168.1.1", 50000))
     request=main_client()
     s.send(request.encode())
     result = s.recv(1024)
     print(result)


