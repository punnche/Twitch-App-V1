import customtkinter
from timer import *
from auth import *
from live_check import *
from tkinter import *
from threading import Thread
def main():
    app = Loading_Window()
    app.mainloop()





class Loading_Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

# Creates window and frame_0

        self.geometry("500x500")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0,weight=1)
        
        self.Frame_0 = customtkinter.CTkFrame(master = self, width = 475, height = 475, corner_radius=20,border_width=2)
        self.Frame_0.grid(row=0, column=0, padx=20,pady=20, sticky="nsew")
        
        self.Frame_0.grid_columnconfigure(0, weight=0)
        self.Frame_0.grid_columnconfigure(0,weight=4)
        
        self.check()

# Checks if the Twitch servers and API servers are online, if True: continues, if False: displays error message

    def check(self):
        if check_if_online() == True:
            self.label_0 = customtkinter.CTkLabel(master = self.Frame_0,text="Connecting... ",text_font=("Roboto Medium", -16))
            self.label_0.grid(row = 4, column=0, padx=20, pady=20,sticky="ew")

            self.label_1 = customtkinter.CTkLabel(master = self.Frame_0,text="Twitch servers are available <Response [200]>",text_font=("Roboto Medium", -16))
            self.label_1.grid(row = 5, column=0, padx=20, pady=20,sticky="ew")

            self.update()
            self.bar()


            self.after(5000, lambda:self.application())
            


        elif check_if_online() == False:
            self.label_0 = customtkinter.CTkLabel(master = self.Frame_0,text="Twitch Servers seem to be experiencing difficulties, try again later!", 
                                                text_font=("Roboto Medium", -16))
            self.label_0.grid(row = 4, column=0, padx=100, pady=50,sticky="ew")
            
            self.progressbar = customtkinter.CTkProgressBar(master=self.Frame_0,mode='indeterminate')
            self.progressbar.grid(row=8,column=0,sticky="ew",padx=20, pady=20)
            self.progressbar.configure(fg_color = "#FFFFFF", progress_color = "#6CE97B")
            self.progressbar.start()
            self.progressbar.update_idletasks()

# Starts the progress bar
  
    def bar(self):
        self.progressbar = customtkinter.CTkProgressBar(master=self.Frame_0,mode='indeterminate')
        self.progressbar.grid(row=8,column=0,sticky="ew",padx=20, pady=20)
        self.progressbar.configure(fg_color = "#FFFFFF", progress_color = "#6CE97B")
        self.progressbar.start()

# Deletes the loading page and prompts the user for a streamer name

    def application(self):
        self.forget_all_load()
        self.label_1 = customtkinter.CTkLabel(master = self.Frame_0,text="Enter a Twitch Streamer:",text_font=("Roboto Medium", -16))
        self.label_1.grid(row = 1, column=0, padx=100, pady=50,sticky="new")

        self.entry_1 = customtkinter.CTkEntry(master = self.Frame_0)
        self.entry_1.grid(row = 2, column=0,padx=20, pady=20)

        self.button_1 = customtkinter.CTkButton(master = self.Frame_0, text="Live?", width = 35, height = 25, text_font=("Roboto Medium", -16),
                                                corner_radius=20, fg_color="#1C5B8C", hover_color="#0D6BB4", command = lambda:self.button_pressed()) # add enter as go
        self.button_1.grid(row=3, column=0, padx=20,pady=20, sticky="n")


# Clears the entry box

    def delete(self):
        self.entry_1.delete("0","end")

# When the live button is pressed, streamer_name function is called and it gets the streamers name; returns False if IndexError
# When the live button is pressed, Check function is called and it checks if the streamer is live; returns True if live and False if not

    def button_pressed(self):
        import time
        global streamer_name_inf, streamer
        streamer = self.entry_1.get()
        streamer = streamer.lower()
        streamer_name_inf =  streamer_name(streamer)
        if streamer_name_inf == False:
            streamer_name_inf = streamer
        result = Check(streamer)

# Asks the user if they want to go to the stream

        if result == True:
            self.label_1.grid_forget()
            self.button_1.grid_forget()
            self.entry_1.grid_forget()
            self.label_2 = customtkinter.CTkLabel(master = self.Frame_0,text=f"{streamer_name_inf} is live! Would you like to go to the stream?",text_font=("Roboto Medium", 12))
            self.label_2.grid(row = 3, column=0, padx=10, pady=50,sticky="ew")

            self.button_2 = customtkinter.CTkButton(master = self.Frame_0, text="Yes", width = 35, height = 25, text_font=("Roboto Medium", -16),
                                                corner_radius=20, fg_color="#1C5B8C", hover_color="#0D6BB4", command = lambda:self.button_yes()) 
            self.button_2.grid(row=5, column=0, padx=20,pady=20, sticky="nw")

            self.button_3 = customtkinter.CTkButton(master = self.Frame_0, text="No", width = 35, height = 25, text_font=("Roboto Medium", -16),
                                                corner_radius=20, fg_color="#1C5B8C", hover_color="#0D6BB4", command = lambda:self.join_later()) 
            self.button_3.grid(row=5, column=0, padx=20,pady=20, sticky="ne")
            
            self.label_2.update_idletasks()

# Asks the user if they want to join said streamer when they are online

        elif result == False:
            self.label_1.grid_forget()
            self.button_1.grid_forget()
            self.entry_1.grid_forget()
            self.label_2 = customtkinter.CTkLabel(master = self.Frame_0,text=f"{streamer_name_inf} is offline! Would you like to join when {streamer_name_inf} is online?",
                                                text_font=("Roboto Medium", 12))
            self.label_2.grid(row = 3, column=0, padx=10, pady=25,sticky="ew")
            self.button_3 = customtkinter.CTkButton(master = self.Frame_0, text="Yes", width = 35, height = 25, text_font=("Roboto Medium", -16),
                                                corner_radius=20, fg_color="#1C5B8C", hover_color="#0D6BB4", command = lambda:self.join_later()) 
            self.button_3.grid(row=5, column=0, padx=20,pady=20, sticky="nw")

            self.button_4 = customtkinter.CTkButton(master = self.Frame_0, text="No", width = 35, height = 25, text_font=("Roboto Medium", -16),
                                                corner_radius=20, fg_color="#1C5B8C", hover_color="#0D6BB4", command = lambda:self.back_to_main_from_offline()) 
            self.button_4.grid(row=5, column=0, padx=20,pady=20, sticky="ne")
            self.label_2.update_idletasks()


        self.delete()
        time.sleep(.25)

# Prompts the user back to the main screen
    
    def back_to_main_from_offline(self):
        self.label_2.grid_forget()
        self.button_3.grid_forget()
        self.button_4.grid_forget()
        self.application()

# If the user hits "yes" when asked if they want to join the stream later, this function is ran
# Prompts the user with a dropdown menu in which they select and time and hit 'Continue'
# Only runs if result == False

    def join_later(self):
        self.label_1.grid_forget()
        self.button_1.grid_forget()
        self.entry_1.grid_forget()
        self.button_4.grid_forget()
        self.button_3.grid_forget()
        self.label_3 = customtkinter.CTkLabel(master = self.Frame_0,text=f"Select a time below to wait for until {streamer_name_inf} is live",
                                                text_font=("Roboto Medium", 12))
        self.label_3.grid(row = 3, column=0, padx=10, pady=25,sticky="ew")
        self.label_4 = customtkinter.CTkLabel(master = self.Frame_0,text=f"{streamer_name_inf}'s stream will open as soon as we detect he is live within the time selected",
                                                text_font=("Roboto Medium", 10))
        self.label_4.grid(row = 4, column=0, padx=5, pady=25,sticky="ew")
        
        self.dropdown_1 = customtkinter.CTkOptionMenu(master = self.Frame_0, values=["1 hour", "2 hours", "3 hours", "4 hours", "5 hours", "6 hours",
                                                                                    "7 hours", "8 hours", "9 hours", "10 hours", "11 hours", "12 hours", "Until Live"])
        self.dropdown_1.grid(row = 6, column=0, padx=5, pady=25, sticky="n")

        self.button_5 = customtkinter.CTkButton(master = self.Frame_0, text="Continue", width = 35, height = 25, text_font=("Roboto Medium", -16),
                                                corner_radius=20, fg_color="#1C5B8C", hover_color="#0D6BB4", command = lambda:self.continue_on()) 
        self.button_5.grid(row=7, column=0, padx=20,pady=20, sticky="n")

# Runs when the button 'Continue' is pressed  
    def continue_on(self):
        global value
        global time_in_hours
        time_in_hours = self.dropdown_1.get()
        value = self.dropdown_1.get()
        self.label_2.grid_forget()
        self.label_3.grid_forget()
        self.label_4.grid_forget()
        self.dropdown_1.grid_forget()
        self.button_5.grid_forget()
        self.update_idletasks()
        self.label_5 = customtkinter.CTkLabel(master = self.Frame_0,text=f"Time selected: {time_in_hours}",
                                                text_font=("Roboto Medium", 20))
        self.label_5.grid(row = 4, column=0, padx=5, pady=25,sticky="ew")
        self.label_6 = customtkinter.CTkLabel(master = self.Frame_0,text=f"CHECK the box below if you WANT to be notified when {streamer_name_inf} is live,",
                                                text_font=("Roboto Medium", 10))
        self.label_6.grid(row =5, column=0, padx=5, pady=2,sticky="ew")
        self.label_7 = customtkinter.CTkLabel(master = self.Frame_0,text=f"you will have to confirm when notified if you want the stream to open or not",
                                                text_font=("Roboto Medium", 10))
        self.label_7.grid(row =6, column=0, padx=5, pady=15,sticky="ew")
        self.label_8 = customtkinter.CTkLabel(master = self.Frame_0,text=f"If you do NOT want to be notified, and just want the stream to open,",
                                                text_font=("Roboto Medium", 10))
        self.label_8.grid(row =7, column=0, padx=5, pady=2,sticky="ew")
        self.label_9 = customtkinter.CTkLabel(master = self.Frame_0,text=f"leave it UNCHECKED",
                                                text_font=("Roboto Medium", 10))
        self.label_9.grid(row =8, column=0, padx=5, pady=0,sticky="ew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master = self.Frame_0, text = "Check this if you want to be notified", onvalue="on", offvalue="off")
        self.checkbox_1.grid(row = 9, column =0, padx=5, pady=10, sticky= "n")
        self.button_6 = customtkinter.CTkButton(master = self.Frame_0, text="Continue", width = 35, height = 25, text_font=("Roboto Medium", -16),
                                                corner_radius=20, fg_color="#1C5B8C", hover_color="#0D6BB4", command = lambda:self.waiting()) 
        self.button_6.grid(row=10, column=0, padx=20,pady=20, sticky="n")
        self.update_idletasks()

    
    

    def waiting(self):
        checked = self.checkbox_1.get()
        print(checked)
        timer_start =  Get_time(value)
        timer_start = str(timer_start)
        print(timer_start)
        s = timer_start
        ss = s.replace("(","")
        sss=ss.replace(")","")
        ssss = sss.replace("'","")
        timer_start_time = ssss.replace(",","")
        if timer_start_time != 'None':
            hour, min, sec = timer_start_time.split(" ")
        elif timer_start == 'None':
            hour = "00"
            min = "00"
            sec = "00"
        self.label_5.grid_forget()
        self.label_6.grid_forget()
        self.label_7.grid_forget()
        self.label_8.grid_forget()
        self.label_9.grid_forget()
        self.checkbox_1.grid_forget()
        self.button_6.grid_forget()
        self.label_11 = customtkinter.CTkLabel(master = self.Frame_0,text=f"Time selected: {time_in_hours}",
                                                text_font=("Roboto Medium", 13))
        self.label_11.grid(row =5, column=0, padx=5, pady=13,sticky="nesw")
        if checked == 'off':
            checked = False
        elif checked == 'on':
            checked = True
    
        if checked == False:
            self.label_9 = customtkinter.CTkLabel(master = self.Frame_0,text=f"Go ahead and minimize this tab or keep it open and we will",
                                                text_font=("Roboto Medium", 13))
            self.label_9.grid(row =8, column=0, padx=5, pady=13,sticky="nesw")
            self.label_10 = customtkinter.CTkLabel(master = self.Frame_0,text=f"automatically open the stream when {streamer_name_inf} is live",
                                                text_font=("Roboto Medium", 13))
            self.label_10.grid(row =9, column=0, padx=5, pady=5,sticky="nesw")
            self.label_12 = customtkinter.CTkLabel(master = self.Frame_0,text=f"Time: Until Live",
                                                text_font=("Roboto Medium", 13))
            self.label_12.grid(row =10, column=0, padx=5, pady=13,sticky="nesw")
            self.update_idletasks()
            if timer_start != 'Until Live':
                self.timer(hour, min, sec)
        elif checked == True:
            self.label_9 = customtkinter.CTkLabel(master = self.Frame_0,text=f"Go ahead and minimize this tab or keep it open and we will",
                                                text_font=("Roboto Medium", 10))
            self.label_9.grid(row =8, column=0, padx=5, pady=2,sticky="nesw")
            self.label_10 = customtkinter.CTkLabel(master = self.Frame_0,text=f"notify you and ask if you want to open the stream when {streamer_name_inf} is live",
                                                text_font=("Roboto Medium", 10))
            self.label_10.grid(row =9, column=0, padx=5, pady=1,sticky="new")
            self.label_12 = customtkinter.CTkLabel(master = self.Frame_0,text=f"Time: Until Live",
                                                text_font=("Roboto Medium", 13))
            self.label_12.grid(row =10, column=0, padx=5, pady=13,sticky="nesw")
            self.update_idletasks()
            #self.a = Thread(target= self.timer(hour,min,sec))
            if timer_start != '00 00 00':
                self.b = Thread(target = Long_Check(hour, streamer, checked))
                self.b.start()
                if timer_start == '00 00 00':
                    Long_Check(hour, streamer, checked)
                if self.b == False:
                    root = Tk()
                    root.geometry("300x300")
                    message_box = Message(root, text = f"The time ran out and {streamer_name} did not go live")
                    message_box.pack()
                    root.mainloop()



    def timer(self, hour, min, sec):
        times = int(hour)*3600 + int(min)*60 + int(sec)

        while times > -1:
            minute , second = (times//60, times%60)
            hourr = 0
            if int(min) > 60:
                hourr,minute = (minute//60, minute%60)
            
            sec = second
            min = minute
            hour = hourr

            self.label_12.configure(text= f"{hour} : {min} : {sec}")
            self.update()
            if times == 0:
                self.label_12.configure(text = "Time's up!")
            self.after(1000)
            times = times - 1

# Is ran when the user presses "Yes" when asked if they want to open the stream, takes back to main screen

    def button_yes(self):
        go_to_stream(streamer_name_inf)
        self.label_2.grid_forget()
        self.button_2.grid_forget()
        self.button_3.grid_forget()
        self.application()

# Deletes all the loading widgets

    def forget_all_load(self):
        self.label_0.grid_forget()
        self.label_1.grid_forget()
        self.progressbar.grid_forget()
    




if __name__ == '__main__':
    main()
