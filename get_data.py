from selenium import webdriver #Selenium Web Driver Kütüphanesini Ekliyoruz
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #JavaScript Konsol Komutlarını Çekmek İçin Gereken Selenium Eklentisini Ekliyoruz 

class WDR(): #Kod Çakışmalarını ve Tekrarlarını önlemek için OOP(Nesne Tabanlı Programlama) Kullanıyoruz ve yazağımız fonksiyonları WDR Sınıfının içine yazıyoruz
    def __init__(self, link): #init fonksiyonu kod ilk nesneye atandığında çalışacak olan koddur, Kod çağırılırken girilen parametreler bu fonksiyon içerisinde değişkene atanır 
        self.link = link # Sınıf çağırılırken içine girilen link parametresiyle istenen linke kod üzerinde oynama yapılmadan ulaşılabilir
        self.d = DesiredCapabilities.CHROME #Selenium Tanımlamaları
        self.d['goog:loggingPrefs'] = { 'browser':'ALL' }
        self.driver = webdriver.Chrome(executable_path='/home/fuchs/Desktop/hackathon/chromedriver', desired_capabilities=self.d) #Seleniumun Webbrowsera girmesi için gereken driverin tanımlanması ve konumunun belirtilmesi
        self.driver.get(self.link) #Driverin linke gitmesini sağlar
        self.entry = " " #giriş değişkeni
        
    def get_msgs(self, sinir=500, dosya="mouse_tracking.txt"): # Mesajları Çekmek için yazılmış bu fonksiyon içine 2 adet parametre alır. Bu parametreler; kodun kaç defa çalıştırılacağını gösteren sinir parametresi ve mesajlaırn kaydedileceği dosyanın isminin girildiği parametredir 
        sayac = 0 
        dosya = str(dosya)
        while True:
            try:
                for self.entry in self.driver.get_log('browser'): #Browserdan Javascript Consoleuna giriş
                    f = open("/home/fuchs/Desktop/hackathon/data/"+dosya, "a") #Kayıt Dosyasının Açılması
                    self.deger = self.entry.get("message").split()[2] #Mesajın OKunabilir hale getirilmesi
                    self.msgs = (self.deger.replace('"',"")+"\n")
                    f.write(self.msgs) # DOsyaya Mesajların Yazılması
                    f.close() # Dosyanın verileri kaydetmesi için kapatılması 
                    sayac +=1 # Sayac arttırımı
                    print(sayac)
                if sayac >= sinir: #Sayac Kontrolu
                    break
            except IndexError: # index error aldığında programı kapat
                break

                
                
    
#                        
#link = "https://enucuzlisans.com/mhrs/mhrs/vatandas/index.html" #link Değişkeni
#chrome = WDR(link) #nesneye atama ve WDR sınıfı çağırma
#chrome.get_msgs(500) # get_msgs fonksiyonu çağğırılması