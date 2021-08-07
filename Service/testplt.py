import matplotlib.pyplot as plt
import matplotlib.image as img


file = 'C:/Users/User/Service/TestPPT/page1.png'
ndarray = img.imread(file)
plt.imshow(ndarray)
plt.show()