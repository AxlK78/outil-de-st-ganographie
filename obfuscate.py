from PIL import Image

def load_image(path:str)->list:
    img = Image.open(path).convert("RGB")
    pixels = list(img.get_flattened_data())
    L=[]
    new=[]
    width , height = img.size
    for tuples in pixels:
        for val in tuples:
            L.append(val)
    for nb in L:
        new.append(int(nb))
    return new,width,height

def load_message(message:str)->list:
    L=[]
    binn=''
    for lettre in message:
        binn+=format(ord(lettre),'08b')
    for char in binn:
        L.append(char)
    return L

def verify_size(message:str,width:int,height:int)->bool:
    taille = len(message)*8
    res = width * height * 3
    if taille > res:
        return False
    return True

def obfuscate_message(pixels:list,bits:list)->list:
    for i in range(len(bits)):
        color = pixels[i]
        color =(color & 0b11111110 |int(bits[i]))
        pixels[i] = color
    return pixels

def write_image(pixels:list,width:int,height:int):
    new_img = Image.new("RGB",(width,height))
    new_pixels = [tuple(pixels[i:i+3]) for i in range(0, len(pixels), 3)]
    new_img.putdata(new_pixels)
    new_img.save("image_obfusquee.png")

def main():
    message = str(input("donnez un message à cacher : "))
    img = load_image('./image.png')
    new = load_message(message)
    if not verify_size(message,img[1],img[2]):
        return False
    res = obfuscate_message(img[0],new)
    return write_image(res,img[1],img[2])

main()