from PIL import Image, ImageDraw #Resim işlemleri için pillow kütüpghanesi kullanımı
import matplotlib.pyplot as plt #veri görselletirme için matplotlib kütüphanesinin kullanımı
import numpy as np #matrix yaratmak için kullanılan numpy kütüphanesi
import scipy.ndimage.filters as filters #Heatmap Hesaplamaları için kullanılan scipy kütüphanesi
from get_data import WDR # benim yazdığım getdata dosyasından WDR sınıfının eklenmesi

link = "https://enucuzlisans.com/mhrs/mhrs/" #link Değişkeni
chrome = WDR(link) #nesneye atama ve WDR sınıfı çağırma
chrome.get_msgs(100) # get_msgs fonksiyonu çağırılması
print("ikinnci siteye geçildi")
link = "https://enucuzlisans.com/mhrs/mhrs/vatandas/index.html" #link Değişkeni
chrome1 = WDR(link) #nesneye atama ve WDR sınıfı çağırma
chrome1.get_msgs(100, "400.txt") # get_msgs fonksiyonu çağğırılması



def generateMouseHeatmap(dosya, template, heatmap):
    template = template #Isı haritaszının uygulanacağı resim
    mouseFile = open("/home/fuchs/Desktop/hackathon/data/"+dosya, "r") #dataların olduğu dosya
    displayArray = np.empty([1150, 1300]) # resim boyutlarının girildiği matrix
    for line in mouseFile: #dosyanın satır satır okunması
        if "-" in line: #veri ayıklama
            continue
        x = int(line.split("#")[0])
        y = int(line.split("#")[1])

        displayArray[y][x] = displayArray[y][x] + 1

    mouseHeatmap = Image.open("/home/fuchs/Desktop/hackathon/data/"+template+".png") # Isı haritasının uygulanacağı resimin açılması
    mouseHeatmap.save("/home/fuchs/Desktop/hackathon/data/"+heatmap) # kayıt işlemi
    plt.figure()#dosyanın gösterilmesi
    img = plt.imread("/home/fuchs/Desktop/hackathon/data/"+heatmap)#dosyanın kod üzerinden tekrar açılması
    #------------------------------ Dosyaının heatmapinin önce grafil olarak oluşturulup sonra resmin üzerine uygulanması
    plt.imshow(img, alpha=1) 
    plt.axis("off")

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    smoothed = filters.gaussian_filter(displayArray, sigma=50)
    plt.imshow(smoothed, cmap="jet", alpha=.5, extent=(xmin,xmax,ymin,ymax))
    plt.savefig("/home/fuchs/Desktop/hackathon/data/"+heatmap, bbox_inches="tight", dpi=300)
    plt.close()

generateMouseHeatmap("mouse_tracking.txt", "ss", "mhrs.png") # fonksiyonun çağırılması
generateMouseHeatmap("400.txt", "sss", "randevu.png") # fonksiyonun çağırılması
