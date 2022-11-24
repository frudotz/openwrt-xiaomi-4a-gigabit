# Xiaomi 4A Giga için Türkçe OpenWRT Kurulum Rehberi!
Bu yöntem ile Windows üzerinde Mi Router 4A Gigabit Edition routerınıza çok kısa sürede OpenWRT kurabileceksiniz.  
Kullanacağımız yöntem yalnızca MediaTek MT7621 tabanlı, Xiaomi Mi Router 4A Gigabit Edition modeli için geçerlidir.  
Gigabit Edition olmayan, diğer marka & model routerlarda bu yöntemi denemek cihazı kullanılmaz duruma getirebilir.  
*OpenWRT kurulumu cihazınızı garanti dışı bırakacak olup, oluşabilecek tüm komplikasyonlar sizin sorumluluğunuzdadır.*  
*Konu ile ilgili hiçbir sorumluluk kabul etmiyorum.*  

<details>
  <summary>İçindekiler</summary>
  <ol>
    <li>
      <a href="#-başlarken">✨ Başlarken</a>
      <ul>
        <li><a href="#-miwifi-kurulumu">🪄 MiWifi Kurulumu</a></li>
      </ul>
    </li>
    <li>
      <a href="#-openwrt-kurulumu">🚀 OpenWRT Kurulumu</a>
      <ul>
        <li><a href="#1%EF%B8%8F⃣-i̇lk-aşama---0start_mainbat">1️⃣ İlk Aşama - 0.start_main.bat</a></li>
        <li><a href="#2%EF%B8%8F⃣-son-aşama---5start_write_osbat">2️⃣ Son Aşama - 5.start_write_OS.bat</a></li>
      </ul>
    </li>
    <li><a href="#-merhaba-openwrt">😎 Merhaba OpenWRT!</a></li>
    <li><a href="#4">4</a></li>
    <li><a href="#5">5</a></li>
    <li><a href="#6">6</a></li>
    <li><a href="#7">7</a></li>
    <li><a href="#8">8</a></li>
  </ol>
</details>

# ✨ Başlarken
Cihazınıza OpenWRT kurmadan önce önyüklü gelen MiWifi'ın ilk kurulum aşamasını gerçekleştirmeniz gerekiyor.  
Modemin LAN portundan routerın WAN portuna, routerın LAN portundan bilgisayarın ethernet portuna kablo takın.  
Tarayıcınızdaki açık sekmede "İnternete erişebilmek için önce bu ağa giriş yapmalısınız." uyarısıyla karşılaşabilirsiniz.  
Karşılaşırsanız yanındaki butona tıklayın ya da kendiniz [router.miwifi.com](http://router.miwifi.com/)/[192.168.31.1](http://192.168.31.1/) adreslerine gidin.  

- ### 🪄 MiWifi Kurulumu
> - MiWifi kurulum sekmesine ulaştığınızda sağ üstten dilinizi seçerek başlayın.  
> - Alt kısımdan ülke seçimini de yaptıktan sonra tikleri işaretleyip ilerleyin.  
> - Router kablolu bağlantıyı tespit edip otomatik olarak DHCP modunu seçecektir, ilerleyin.  
> - Mod seçiminde bir hata olursa kendiniz maneul olarak DHCP seçebilirsiniz.  
> - Wi-Fi Ayarları sekmesini kurulumu bitirebilmek için basitçe doldurun. (Şifrenizi unutmayın.)  
> - Kurulum tamamlandığında cihaz yeniden başlayacaktır, ışıklar maviye döndüğünde sayfayı yenileyin.  
> - Router giriş sayfası sizi karşılayacaktır, bu aşamada buradaki işimizi tamamlamış bulunuyoruz.  

# 🚀 OpenWRT Kurulumu
Paylaştığımız linkten indirdiğiniz **OpenWRTKurulum** klasörünü açın, `firmwares` klasörü altında OpenWRT'nin en güncel sürümü bulunmalıdır.  
Rehberi paylaştığımız tarih itibarıyla en güncel sürümü sizler için bıraktık, en güncel sürümü [buradaki linkten](https://openwrt.org/inbox/toh/xiaomi/xiaomi_mi_router_4a_gigabit_edition#installation) kontrol edebilir ve indirebilirsiniz.  
Güncel dosyayı yerleştirdikten sonra ana dizindeki `0.start_main.bat` ve `5.start_write_OS.bat` dosyalarını sırayla çalıştırıyoruz.  

- #### 1️⃣ İlk Aşama - 0.start_main.bat
> - `Enter router password:` kısmı ile kurulum scripti sizden MiWifi kurulumunda belirlediğiniz admin şifresini isteyecektir.  
> - Şifreyi girdikten sonra bir konfigürasyon güncellemesi ile routera telnet üzerinden erişim sağlayabilir hale geleceksiniz.  
> - Scriptten `Done` yanıtını aldığınızda herhangi bir tuşa basarak komut istemi sekmesini kapatabilirsiniz.  

- #### 2️⃣ Son Aşama - 5.start_write_OS.bat
> - Bu scripti çalıştırdığınızda karşınıza seçim alternatifiniz olmayan bir seçim ekranı gelecektir, **`1`**'i tuşlayıp devam ediniz.  
> - Birkaç işlem akabinde router OpenWRT'den başlamak için birkaç kez yeniden başlar, bu aşamada cihaz asla güçten ayırılmamalıdır.  

# 😎 Merhaba OpenWRT!
Her şeyi doğru yaptıysanız cihaz birkaç kez yeniden başladıktan sonra tüm ışıkları maviye döner ve internete erişebilirsiniz.  
Tebrikler! Artık doğruca [192.168.1.1](http://192.168.1.1/) adresine giderek OpenWRT'ye merhaba diyebilirsiniz! \*alkış efekti\*  

