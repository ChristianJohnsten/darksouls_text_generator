from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class ImgGen:
    def __init__(self):
        self.img = None
        self.draw_obj = None
        self.font = ImageFont.truetype(r'Trajan Pro Regular.ttf', 120)
        self.text = ""

    def gen(self, size, background, text):
        self.img = Image.open(background)
        self.draw_obj = ImageDraw.Draw(self.img, 'RGBA')
        self.text = text

        self._draw_banner()
        self._draw_text(self.text)

        self.img = self.img.resize(size, Image.Resampling.LANCZOS)

        return self.img

    def tk(self):
        return ImageTk.PhotoImage(self.img)

    def save(self, path=""):
        if not path:
            if not os.path.exists("generated"):
                os.mkdir("generated")
            self.img.save(f"generated/{self.text}.png")
        else:
            self.img.save(path, format="png")


    def _draw_gradient(self, x1, y1, x2, y2, c1=(0, 0, 0, 255), c2=(0, 0, 0, 0)):
        h = y1 - y2
        rdif = c1[0] - c2[0]
        gdif = c1[1] - c2[1]
        bdif = c1[2] - c2[2]
        adif = c1[3] - c2[3]
        r, g, b, a = c1

        for i in range(abs(h)):
            if rdif > 0:
                r = rdif - int(rdif / (abs(h)-1) * i)
            elif rdif < 0:
                r = abs(int(rdif / (abs(h)-1) * i))

            if gdif > 0:
                g = gdif - int(gdif / (abs(h)-1) * i)
            elif gdif < 0:
                g = abs(int(gdif / (abs(h)-1) * i))

            if bdif > 0:
                b = bdif - int(bdif / (abs(h)-1) * i)
            elif bdif < 0:
                b = abs(int(bdif / (abs(h)-1) * i))

            if adif > 0:
                a = adif - int(adif / (abs(h)-1) * i)
            elif adif < 0:
                a = abs(int(adif / (abs(h)-1) * i))

            if h > 0:
                self.draw_obj.line([(x1, y1 - i), (x2, y1 - i)], fill=(r, g, b, a), width=0)
            elif h < 0:
                self.draw_obj.line([(x1, y2 - i), (x2, y2 - i)], fill=(r, g, b, a), width=0)


    def _draw_banner(self):
        height = self.img.height
        width = self.img.width
        y1 = height // 2 - height // 10
        y2 = height // 2 + height // 10
        self.draw_obj.rectangle([(0, y1), (width, y2)], fill=(0, 0, 0, 220))

        self._draw_gradient(0, y1 - 1, width, y1 - height // 8, c1=(0, 0, 0, 220), c2=(0, 0, 0, 0))
        self._draw_gradient(0, y2, width, y2 + height // 8, c1=(0, 0, 0, 0), c2=(0, 0, 0, 220))


    def _draw_text(self, text):
        self.draw_obj.text((self.img.width // 2, self.img.height // 2), text, fill="#860507", font=self.font, anchor="mm")


