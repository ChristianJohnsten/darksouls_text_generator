from tkinter import *
from image_gen import ImgGen
from word_gen import WordGen
from pathlib import Path
from random import randint

class DarkSoulsGen:
    def __init__(self, bg_dir):
        # ----- Create word_gen and image_gen objects -----
        self.wg = WordGen()
        self.im_gen = ImgGen()

        # ----- Default values -----
        self.size = 854, 480
        self.font = (r'Trajan Pro Regular.ttf', 32)
        self.default_text = "{adjective} {noun} {past tense verb}"

        # ----- Initialize tkinter root window -----
        self.root = Tk()
        self.root.geometry('854x523+600+200')
        self.root.resizable(False, False)
        self.root["bg"] = "black"

        # ----- Generate first image -----
        self.bg_dir = bg_dir
        self.load_backgrounds()
        self.bg = self.get_random_background()
        self.get_image()

        # ----- Keybindings bar -----
        keybinds = ["[Space] Re-generate all",
                    "[S] Save image",
                    "[R] Reset input text",
                    "[B] New background",
                    "[1] New 1st word",
                    "[2] New 2nd word",
                    "[3] New 3rd word"
                    ]

        keybinds = ("      ").join(keybinds)  # Joins all keybindings with 6 spaces to separate them
        keybinds = "  " + keybinds  # Add 2 spaces of padding to the front of the keybindings string

        self.keybinds_bar = Label(self.root, text=keybinds, bg="#000000", fg="#FFFFFF", anchor="w")
        self.keybinds_bar.grid(row=2, column=0, sticky="nsew")

        # ----- Text entry bar -----
        self.text_entry_frame = Frame(self.root, bg="#FFFFFF", borderwidth=0)
        self.text_entry_frame.columnconfigure(1, weight=1)
        self.text_entry_frame.grid(row=0, column=0, sticky="nsew")

        self.text_entry_label = Label(self.text_entry_frame, text="Input text:", bg="#FFFFFF", fg="#000000")
        self.text_entry_label.grid(row=0, column=0)

        self.text_entry = Entry(self.text_entry_frame, bg="#EEEEEE", fg="#000000", borderwidth=0)
        self.text_entry.insert(0, self.default_text)  # Sets initial text
        self.text_entry.grid(row=0, column=1, columnspan=2, sticky="nsew")

        # ----- Background image label -----
        self.bg_img_label = Label(self.root, image=self.tkimg, borderwidth=0)
        self.bg_img_label.grid(row=1, column=0, padx=0, pady=0)

        # ----- Bindings -----
        self.root.bind("<Key>", self._key_handler)  # Send all key events to _key_handler
        self.bg_img_label.bind("<Button-1>", self._set_img_focus)  # Grab focus when image is left clicked on

        self.root.mainloop()

    def _key_handler(self, event):
        if str(self.root.focus_get()) == ".!frame.!entry":  # If focus is on the text_entry, don't process keybinds
            if event.char in ("\r", "\n"):  # Change focus to the image and generate image when the enter key is pressed
                self._set_img_focus()
                self.get_image(text=self.text_entry.get().lower(), bg=-1)
                self.bg_img_label.configure(image=self.tkimg)
                self.bg_img_label.image = self.tkimg

        else:  # If focus is not on the text_entry, process all keybinds
            if event.char == " ":  # Re-generate all
                self.get_image(text=self.text_entry.get().lower())
                self.bg_img_label.configure(image=self.tkimg)
                self.bg_img_label.image = self.tkimg

            elif event.char == "r":  # Reset text_entry (input text)
                self.text_entry.delete(0, END)
                self.text_entry.insert(0, self.default_text)

            elif self.text_entry.get().lower() == "{adjective} {noun} {past tense verb}":
                if event.char == "1":  # New adjective (1st word)
                    t = self.im_gen.text.split(" ")
                    self.get_image(text="{adjective} "+t[1]+" "+t[2], bg=-1)
                    self.bg_img_label.configure(image=self.tkimg)
                    self.bg_img_label.image = self.tkimg

                elif event.char == "2":  # New noun (2nd word)
                    t = self.im_gen.text.split(" ")
                    self.get_image(text=t[0] + " {noun} " + t[2], bg=-1)
                    self.bg_img_label.configure(image=self.tkimg)
                    self.bg_img_label.image = self.tkimg

                elif event.char == "3":  # New verb (3rd word)
                    t = self.im_gen.text.split(" ")
                    self.get_image(text=t[0]+" "+t[1]+" {past tense verb}", bg=-1)
                    self.bg_img_label.configure(image=self.tkimg)
                    self.bg_img_label.image = self.tkimg

                elif event.char == "b":  # New background
                    t = self.im_gen.text
                    self.get_image(text=t)
                    self.bg_img_label.configure(image=self.tkimg)
                    self.bg_img_label.image = self.tkimg

                elif event.char == "s":  # Save image
                    try:
                        self.save_label.destroy()  # If a save_label already exists, try to destroy it
                    except AttributeError:
                        pass

                    self.save_label = Label(self.root, text="  Saved  ", bg="#000000", fg="#FFFFFF", font=(None, 16))
                    self.save_label.place(relx=0.5, rely=0.15, anchor='center')
                    self.root.after(2000, self._hide_save_label)  # After 2 seconds, hide the save label
                    self.im_gen.save()

    def _hide_save_label(self):
        self.save_label.destroy()

    def _set_img_focus(self, event=None):
        self.bg_img_label.focus_set()

    def get_image(self, size=None, bg=None, text=None):
        if size is None:  # If size is not given, use default size
            size = self.size
        if bg is None:  # If background is not given, use a random one
            bg = self.get_random_background()
        elif bg == -1:  # Use last selected image
            bg = self.bg
        if text is None:  # If text is not given, use the default text
            text = self.default_text

        # Replace {noun}, {adjective}, etc. with randomly selected ones
        for i in range(text.count("{adjective}")):
            text = text.replace("{adjective}", self.wg.get_adjective(), 1)
        for i in range(text.count("{noun}")):
            text = text.replace("{noun}", self.wg.get_noun(), 1)
        for i in range(text.count("{past tense verb}")):
            text = text.replace("{past tense verb}", self.wg.get_pt_verb(), 1)

        self.img = self.im_gen.gen(size, bg, text.lower())
        self.tkimg = self.im_gen.tk()
        return self.img

    def load_backgrounds(self):
        self.backgrounds = []
        for item in Path.iterdir(Path(self.bg_dir)):
            if item.suffix.lower() in (".png", ".jpg"):
                self.backgrounds.append(item.absolute())

    def get_random_background(self):
        self.bg = self.backgrounds[randint(0, len(self.backgrounds)-1)]
        return self.bg


if __name__ == "__main__":
    dsg = DarkSoulsGen(bg_dir="backgrounds")
