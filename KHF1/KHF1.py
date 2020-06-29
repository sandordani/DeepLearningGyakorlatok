
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt

images=[]
for i in range(5):
    images.append(mpimg.imread("images/im%d.jpg" % (i+1)))

reds = []
greens = []
blues = []
for i in images:
    red = i[:,:,0]
    green = i[:,:,1]
    blue = i[:,:,2]
    print("red:")
    print(red)
    plt.imshow(red)
    plt.show()
    print("green:")
    print(green)
    plt.show()
    plt.imshow(green)
    print("blue:")
    print(blue)
    plt.show()
    plt.imshow(blue)
    reds.append(i[:,:,0])
    greens.append(i[:,:,1])
    blues.append(i[:,:,2])


plt.imshow(images[0])

plt.show()
