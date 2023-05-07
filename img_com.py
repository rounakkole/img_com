def img_com():
    from PIL import Image
    import math

    counter = 0

    while counter < 10:
	#get a new image
        image = Image.open('ip_img.jpeg')
        size_in = (len(image.fp.read()) / (1024))
        print(f"input file size: {image.size} {size_in}")
        pix_in1, pix_in2 = image.size
        reso_in = pix_in1 * pix_in2

        size_r = int(input("enter output size % "))
        size_out_est = int(size_in * size_r / 100)
        print(f"approx output size: {size_out_est}")
        reso_out_est = int(reso_in * (size_r / 100))

        correction_r = (1-(size_r / 100))/10
        pix_out1 = int(math.sqrt((reso_out_est / pix_in2 * pix_in1))*(1-correction_r))
        pix_out2 = int(pix_out1 * pix_in2 / pix_in1)

        
        image_resized = image.resize((pix_out1, pix_out2))
        image_resized.save('op_img_compressed.jpeg')
        image_resized = Image.open('op_img_compressed.jpeg')
        size_out = (len(image_resized.fp.read()) / 1024)

        print(f"resized: {image_resized.size} {size_out}")

        #if (size_out > (size_out_est * 0.95) and size_out < (size_out_est * 1.05)):
            #print("successfully resized upto 5% accuracy")

        while (pix_in1 / pix_in2) != (pix_out1 / pix_out2):
            pix_out1 += 1
            pix_out2 = int(pix_out1 * pix_in2 / pix_in1)
        #print(f"final resolution: {pix_out1}, {pix_out2} \n")
        #reso_out = pix_out1 * pix_out2

        counter += 1
        
        

