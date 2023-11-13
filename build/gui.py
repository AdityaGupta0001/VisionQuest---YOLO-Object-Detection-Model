

from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
from yoloWebcam import useWebcam
from yoloImage import useImages
from yoloVideo import useVideo

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Aditya\Desktop\test\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
    
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    720.0,
    fill="#000000",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    285.0,
    326.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    642.0,
    37.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    639.0,
    100.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    285.0,
    437.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    154.0,
    375.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    170.0,
    375.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    154.0,
    485.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    170.0,
    485.0,
    image=image_image_8
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    565.5,
    375.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    fg="#FFFFFF",
    bg="#000716",
    font = ("Roboto", 18),
    highlightthickness=0
)
entry_1.place(
    x=193.0,
    y=350.0,
    width=745.0,
    height=48.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    565.5,
    486.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    fg="#FFFFFF",
    bg="#000716",
    font = ("Roboto", 18),
    highlightthickness=0
)
entry_2.place(
    x=193.0,
    y=461.0,
    width=745.0,
    height=48.0
)

global mode
mode=""

def showObjects():
    messagebox.showinfo("Allowed Objects"," Objects can be:  'person' ,'bicycle' ,'car' ,'motorbike' ,'aeroplane' ,'bus' ,'train' , ...")

def detectUsingWebcam():
    global mode
    entry_1.delete(0,tk.END)
    entry_1.config(foreground="#000716", background="#000716")
    entry_2.delete(0,tk.END)
    entry_2.config(foreground="#000716", background="#000716")
    button_5.config(state='disabled')
    mode = 'webcam'

def detectUsingImage():
    global mode
    entry_1.delete(0,tk.END)
    entry_1.config(foreground="#FFFFFF", background="#000716")
    entry_2.delete(0,tk.END)
    entry_2.config(foreground="#000716", background="#000716")
    mode = "image"

def detectUsingVideos():
    global mode
    entry_1.delete(0,tk.END)
    entry_1.config(foreground="#FFFFFF", background="#000716")
    entry_2.delete(0,tk.END)
    entry_2.config(foreground="#FFFFFF", background="#000716")
    mode = "video"

def open_file_dialog():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=[
            ("Image files", "*.jpg;*.png"),
            ("Video files", "*.mp4"),
            ("All files", "*.*")
        ]
    )
    entry_1.delete(0,tk.END)
    entry_1.insert(0,file_path)

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
            "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
            "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
            "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
            "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
            "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
            "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
            "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
            "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
            "teddy bear", "hair drier", "toothbrush"
            ]
    
def detectObjects():
    print(mode)
    if mode == "webcam":
        object = entry_2.get()
        if object not in classNames:
            print("Error")
        else:
            useWebcam(object)
    elif mode == "image":
        print("Hello")
        print(entry_1.get())
        useImages(entry_1.get())
    elif mode == 'video':
        filepath = entry_1.get()
        object = entry_2.get()
        print(filepath, object)
        useVideo(filePath=filepath, object=object)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=detectUsingVideos,
    relief="flat"
)
button_1.place(
    x=505.0,
    y=179.0,
    width=256.0,
    height=96.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=detectUsingWebcam,
    relief="flat"
)
button_2.place(
    x=821.0,
    y=179.0,
    width=256.0,
    height=96.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=detectUsingImage,
    relief="flat"
)
button_3.place(
    x=189.0,
    y=179.0,
    width=256.0,
    height=96.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=detectObjects,
    relief="flat"
)
button_4.place(
    x=512.0,
    y=586.0,
    width=256.0,
    height=96.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_file_dialog,
    relief="flat"
)
button_5.place(
    x=963.0,
    y=347.0,
    width=137.0,
    height=53.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=showObjects ,
    relief="flat"
)
button_6.place(
    x=963.0,
    y=459.0,
    width=137.0,
    height=53.0
)



window.resizable(False, False)
window.mainloop()
