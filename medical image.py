import numpy as np, matplotlib.pyplot as plt

img = np.random.normal(100, 15, (256,256))
x,y = np.ogrid[:256,:256]
img[(x-130)**2+(y-140)**2<25**2] += 80
tumar = img > 160

plt.figure(figsize=(9,3))
for i ,(d,t) in enumerate([(img,"MRI"),(tumar,"Tumar"),(img,"Overlay")],1):

    plt.subplot(1,3,i)
    plt.imshow(d,"gray");
    plt.imshow(tumar,"read", .4) if i==3 else None
    plt.title(t); plt.axis("off")
plt.show()

