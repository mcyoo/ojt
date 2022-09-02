import cv2

img1 = cv2.imread('image_1.jpg')


def divid_image(file,m,n):
    img_width = file.shape[1] #이미지 가로 사이즈
    img_height = file.shape[0] #이미지 세로 사이즈
    
    resize_width = round(img_width/m)
    resize_height = round(img_height/n)
    
    resize_img_list = []

    for y in range(n):
        for x in range(m):
            resize_file = file[resize_height*y:resize_height*(y+1),resize_width*x:resize_width*(x+1)].copy()
            resize_img_list.append(resize_file)
    
    return resize_img_list


def print_output(output_list):
    for id,val in enumerate(output_list):
        cv2.imshow("test " + str(id) ,val)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

output_list = divid_image(img1,3,3)
print_output(output_list)