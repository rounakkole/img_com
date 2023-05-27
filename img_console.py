def img_console():
    from PIL import Image
    
    width = 50
    step = 20
    img = Image.open('corner_border.jpg')
    
    pix1, pix2 = img.size
    pixo1 = width
    pixo2 = int(pixo1 * pix2 / pix1)
    resized_img = img.resize((pixo1, pixo2))
    
    gray_img = resized_img.convert("L")
    gray_img.save('gray_img.jpeg')
    gray_img = Image.open('gray_img.jpeg')

    i = j = -1
    while (j < (pixo2 - 1)):
        i = 0
        j = j + 1
        print(end = "\n")
        while (i < (pixo1 - 1)):
            i = i + 1
            ip_rgb = (gray_img.load()[i, j]) #00 to 255
            for k in range(14):
                ip_window = (k * step)
                if(abs(ip_rgb - ip_window) <= (step / 2)):
                    if(ip_window >= 160):
                        print(end = "  ")
                    elif(ip_window >= 100):
                        print(end = "0 ")
                    else:
                        print(end = "00")
                    break
            
