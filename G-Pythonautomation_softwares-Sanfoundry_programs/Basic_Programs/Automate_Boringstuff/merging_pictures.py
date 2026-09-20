import sys
from PIL import  Image
# list_im = ['F:\\Screen_1.png','F:\\Screen_2.png']
# new_im = Image.new('RGB', (5000,1000)) #creates a new empty image, RGB mode, and size 444 by 95
#
# for elem in list_im:
#     for i in range(0,5000,1000):
#         im=Image.open(elem)
#         new_im.paste(im, (i,0))
# new_im.save('F:\\Unsettled_PF.png')

img1=Image.open("F:\\PF_Withdrawal_app_form_pg_1.png")
w1,h1=img1.size
print(w1,h1)
# img1=img1.resize((w1,h1))
# print(type(img1))
#
img2=Image.open("F:\\PF_Withdawal_app_form_pg_2.png")#input
img3=Image.open("F:\\PF_Withdrawal_app_form_pg_3.png")#input

img1=img1.resize((w1,h1))
img2=img2.resize((w1,h1))
img3=img3.resize((w1,h1))
new_im=Image.new('RGBA',(w1,h1*3),'white')#input

new_im.paste(img1,(0,0,w1,h1))#input
# new_im.show()
#Vertical pasting of img2
new_im.paste(img2,(0,h1,w1,h1*2))#input
# new_im.show()
new_im.paste(img3,(0,h1*2,w1,h1*3))#input
# new_im.show()
# print(new_im.size)
new_im=new_im.resize((2000,2000))#input
new_im.show()
new_im.save('F:\\PF_Withdrawal_form.png')#input
print("Picture saved")
#
#
#
#
