from PIL import Image, ImageDraw, ImageFont, ImageTk
import io

def make(text):
    """Making simple and regular captcha"""
    im = Image.new("RGB", (len(text) * 13 , 27), "white")
    im.save('bin/blank', "png")
    base = Image.open('bin/blank').convert('RGBA')
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    fnt = ImageFont.truetype('bin/Ubuntu-B.ttf', 24)
    d = ImageDraw.Draw(txt)
    d.text((0,0), text, font=fnt, fill=(0,0,0,255))
    out = Image.alpha_composite(base, txt)
    out.save("bin/result", "png")
        
if __name__ == ("__main__"):
    make("one")
    
