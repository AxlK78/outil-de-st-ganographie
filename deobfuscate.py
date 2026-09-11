from PIL import Image

def load_image(path:str)->list:
    img = Image.open(path).convert("RGB")
    pixels = list(img.get_flattened_data())
    L=[]
    for tuples in pixels:
        for val in tuples:
            L.append(int(val))
    return L

def read_message(pixels:list)->list:
    L=[]
    for pixel in pixels:
        L.append(pixel & 1)
    return L

def reconstruct_message(bits:list)->str:
    message=''
    for i in range(0,len(bits),8):
        byte=bits[i:i+8]
        if len(byte)<8:
            break
        char=chr(int(''.join(str(b) for b in byte),2))
        message+=char
    return message

def main():
    img = load_image('./image_obfusquee.png')
    bits = read_message(img)
    message = reconstruct_message(bits)
    print(message)

main()