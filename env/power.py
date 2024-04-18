import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os


def downloader(): 
    url = entry_url.get()
    resolution = resolutions_var.get()

    try: 
        vid = YouTube(url)
        stream = vid.streams.filter(res=resolution).first()
    except:
        print()


root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

#window title

root.title("Youtube downloader")


#set dimensions
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)


#frame
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)



#entry widget
url_label = ctk.CTkLabel(content_frame, text="Please enter youtube url here: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=("10p", "5p"))
entry_url.pack(pady=("10p", "5p"))



#button for downloads
dload_button = ctk.CTkButton(content_frame, text="download", command=downloader)
dload_button.pack(pady=("10p", "5p"))



#resolution
resolutions = ["720px", "360px", "240px"]
resolutions_var = ctk.StringVar()
resolutions_combo = ttk.Combobox(content_frame, value=resolutions, textvariable=resolutions_var)
resolutions_combo.pack(pady=("10p", "5p"))
resolutions_combo.set("240px")


#create progress label
progress_lab = ctk.CTkLabel(content_frame, text="0%")
#progress_lab.pack(pady=("10p", "5p"))


progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0.3)
#progress_bar.pack(pady=("10p", "5p"))


status_lab = ctk.CTkLabel(content_frame, text="loading...")
#status_lab.pack(pady=("10p", "5p"))







root.mainloop()