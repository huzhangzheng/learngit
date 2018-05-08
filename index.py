# from PIL import Image
# import imagehash
# import sys
# hash = imagehash.average_hash(Image.open('D:\pythonspace\learnpy\h1.jpg'))
# print(hash)
# otherhash = imagehash.average_hash(Image.open('D:\pythonspace\learnpy\h2.jpg'))
# print(otherhash)

m=0
res=0
while m <100:
    if m % 2:
        res += m
    else:
        res -= m
    m+=1
print(res)