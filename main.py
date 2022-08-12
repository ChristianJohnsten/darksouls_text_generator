from tkinter import *
from image_gen import ImgGen
from word_gen import WordGen
from pathlib import Path
from random import randint

class DarkSoulsGen:
    def __init__(self, bg_dir):
        self.bg_dir = bg_dir
        self.load_backgrounds()

        self.wg = WordGen()
        self.im_gen = ImgGen()

        self.size = 854, 480
        self.root = Tk()
        self.root.bind("<Key>", self._key_handler)
        # self.root.bind('<Motion>', self._motion)

        self.root.geometry('854x480+600+200')
        self.root["bg"] = "black"

        self.font = (r'Trajan Pro Regular.ttf', 32)

        self.text = "oblong vegetable rolled"
        self.bg = self.get_random_background()
        self.img = self.im_gen.gen(self.size, self.bg, self.text)
        self.tkimg = self.im_gen.tk()

        # self.save_label = Label(self.root, text="", bg="#000000", fg="#FFFFFF")
        self.label = Label(self.root, image=self.tkimg)

        self.label.pack(expand=True)
        self.root.mainloop()

    # def _motion(self, event):
        # x, y = event.x, event.y
        # print('{}, {}'.format(x, y))

    def _key_handler(self, event):
        # print(event.char, event.keysym, event.keycode)

        if event.keysym == "space":  # re-gen all
            self.get_image()
            self.label.configure(image=self.tkimg)
            self.label.image = self.tkimg

        elif event.keysym == "1":  # re-gen adjective
            t = self.im_gen.text.split(" ")
            self.get_image(text=self.wg.get_adjective()+" "+t[1]+" "+t[2], bg=-1)
            self.label.configure(image=self.tkimg)
            self.label.image = self.tkimg

        elif event.keysym == "2":  # re-gen noun
            t = self.im_gen.text.split(" ")
            self.get_image(text=t[0]+" "+self.wg.get_noun()+" "+t[2], bg=-1)
            self.label.configure(image=self.tkimg)
            self.label.image = self.tkimg

        elif event.keysym == "3":  # re-gen verb
            t = self.im_gen.text.split(" ")
            self.get_image(text=t[0]+" "+t[1]+" "+self.wg.get_verb(), bg=-1)
            self.label.configure(image=self.tkimg)
            self.label.image = self.tkimg

        elif event.keysym in "b":  # re-gen background
            t = self.im_gen.text
            self.get_image(text=t)
            self.label.configure(image=self.tkimg)
            self.label.image = self.tkimg

        elif event.keysym == "s":  # save image
            try:
                self.save_label.destroy()
            except AttributeError:
                pass

            self.save_label = Label(self.root, text="Saved", bg="#000000", fg="#FFFFFF", font=self.font)
            self.save_label.place(relx=0.5, rely=0.25, anchor='center')
            self.root.after(2000, self._hide_save_label)
            self.im_gen.save()

    def _hide_save_label(self):
        self.save_label.destroy()

    def get_image(self, size=None, bg=None, text=None):
        if size is None:
            size = self.size
        if bg is None:
            bg = self.get_random_background()
        elif bg == -1:  # Use last selected image
            bg = self.bg
        if text is None:
            text = self.wg.gen_anv()

        self.img = self.im_gen.gen(size, bg, text)
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
