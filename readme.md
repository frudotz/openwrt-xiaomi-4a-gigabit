# Mi Router 4A Gigabit için OpenWRT Kurulum Rehberi!
Bu yöntem ile Windows üzerinde Mi Router 4A Gigabit Edition routerınıza çok kısa sürede OpenWRT kurabileceksiniz.  
Kullanacağımız yöntem yalnızca MediaTek MT7621 tabanlı, Xiaomi Mi Router 4A Gigabit Edition modeli için geçerlidir.  
Gigabit Edition olmayan, diğer marka & model routerlarda bu yöntemi denemek cihazı kullanılmaz duruma getirebilir.  
*OpenWRT kurulumu cihazınızı garanti dışı bırakacak olup, oluşabilecek tüm komplikasyonlar sizin sorumluluğunuzdadır.*  
*Konu ile ilgili hiçbir sorumluluk kabul etmiyoruz. Rehberimizi kaynak göstererek paylaşmanız önemle rica olunur.* 🙏

<p align="left">
  <a href="https://discord.gg/k6y5MBKCPW"><img src="https://img.shields.io/badge/Discord-Yardım İçin-blue?logo=discord&logoColor=white"/></a>
  <a href="https://www.youtube.com/watch?v=OYliHXuUevg"><img src="https://img.shields.io/badge/Youtube-Kurulum Video Rehberi-blue?logo=youtube&logoColor=white"/></a>
</p>
  
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
      <a href="#-openwrt-kurulumu---i̇ndir">🚀 OpenWRT Kurulumu</a>
      <ul>
        <li><a href="#1%EF%B8%8F⃣-i̇lk-aşama---0start_mainbat">1️⃣ İlk Aşama - 0.start_main.bat</a></li>
        <li><a href="#2%EF%B8%8F⃣-son-aşama---5start_write_osbat">2️⃣ Son Aşama - 5.start_write_OS.bat</a></li>
      </ul>
    </li>
    <li><a href="#-merhaba-openwrt">😎 Merhaba OpenWRT!</a></li>
    <li><a href="#-özel-teşekkürler">💖 Özel Teşekkürler</a></li>
    <li><a href="#-katkıda-bulun--bağış">🤝 Katkıda Bulun / Bağış</a></li>
    <li><a href="#%EF%B8%8F-kaynaklar">🗃️ Kaynaklar</a></li>
  </ol>
</details>

# ✨ Başlarken
Cihazınıza OpenWRT kurmadan önce önyüklü gelen MiWifi'ın ilk kurulum aşamasını gerçekleştirmeniz gerekiyor.  
Modemin LAN portundan routerın WAN portuna, routerın LAN portundan bilgisayarın ethernet portuna kablo takın.  
Tarayıcınızdaki açık sekmede "İnternete erişebilmek için önce bu ağa giriş yapmalısınız." uyarısıyla karşılaşabilirsiniz.  
Karşılaşırsanız yanındaki butona tıklayın veya kendiniz [router.miwifi.com](http://router.miwifi.com/) - [192.168.31.1](http://192.168.31.1/) adreslerinden birine gidin.  

- ### 🪄 MiWifi Kurulumu
> - MiWifi kurulum sekmesine ulaştığınızda sağ üstten dilinizi seçerek başlayın.  
> - Alt kısımdan ülke seçimini de yaptıktan sonra tikleri işaretleyip ilerleyin.  
> - Router kablolu bağlantıyı tespit edip otomatik olarak DHCP modunu seçecektir, ilerleyin.  
> - Mod seçiminde bir hata olursa kendiniz maneul olarak DHCP seçebilirsiniz.  
> - Wi-Fi Ayarları sekmesini kurulumu bitirebilmek için basitçe doldurun. (Şifrenizi unutmayın.)  
> - Kurulum tamamlandığında cihaz yeniden başlayacaktır, ışıklar maviye döndüğünde sayfayı yenileyin.  
> - Router giriş sayfası sizi karşılayacaktır, bu aşamada buradaki işimizi tamamlamış bulunuyoruz.  

<p align="left">
  <img width="auto" height="130" src="https://raw.githubusercontent.com/frudotz/openwrt-xiaomi-4a-gigabit/main/images/1.png">
  <img width="auto" height="130" src="https://github.com/frudotz/openwrt-xiaomi-4a-gigabit/blob/main/images/2-8.png">
</p>

# 🚀 OpenWRT Kurulumu - <a href="https://github.com/frudotz/openwrt-xiaomi-4a-gigabit/releases/tag/OpenWRT-23.05.0" target="_blank">İndir</a>
Paylaştığımız **OpenWRTKurulum** klasörünü açın, `firmwares` dizininde OpenWRT'nin güncel sürümü bulunmalıdır.  
Rehberi yazdığımız tarihin güncel sürümünü sizler için bıraktık, güncel sürümü [buradan](https://openwrt.org/inbox/toh/xiaomi/xiaomi_mi_router_4a_gigabit_edition#installation) kontrol edip indirebilirsiniz.  
Dosyayı yerleştirdikten sonra ana dizindeki `0.start_main.bat` ve `5.start_write_OS.bat` dosyasını sırayla açıyoruz.  
_**BAT dosyaları arasında **"5."** ile başlayan iki dosya yer almaktadır yanlış dosyayı çalıştırmamaya __dikkat ediniz.___

- #### 1️⃣ İlk Aşama - 0.start_main.bat
> - `Enter router password:` kısmında script sizden ilk kurulumda belirlediğiniz şifreyi isteyecektir.  
> - Şifreyi girdikten sonra script birkaç değişiklikle cihazın telnet erişimini açacaktır.  
> - `Done` yanıtını aldığınızda herhangi bir tuşa basarak sekmeyi kapatabilirsiniz.  

- #### 2️⃣ Son Aşama - 5.start_write_OS.bat
> - Bu scripti açtığınızda karşınıza alternatifiniz olmayan bir seçim ekranı gelir, **`1`**'i tuşlayıp devam ediniz.  
> - Router OpenWRT'den başlamak için birkaç kez yeniden başlar, bu kısımda cihaz asla güçten ayırılmamalıdır.  

<p align="left">
  <img width="200" height="auto" src="https://github.com/frudotz/openwrt-xiaomi-4a-gigabit/blob/main/images/9.png">
  <img width="200" height="auto" src="https://github.com/frudotz/openwrt-xiaomi-4a-gigabit/blob/main/images/10.png">
  <img width="200" height="auto" src="https://github.com/frudotz/openwrt-xiaomi-4a-gigabit/blob/main/images/11.png">
  <img width="200" height="auto" src="https://github.com/frudotz/openwrt-xiaomi-4a-gigabit/blob/main/images/12.png">
</p>

# 😎 Merhaba OpenWRT!
Kurulumda bir hata yapmadıysanız birkaç dakika içinde cihazın tüm ışıkları maviye döner ve internete erişebilirsiniz.  
Tebrikler! Artık doğruca [192.168.1.1](http://192.168.1.1/) adresine giderek OpenWRT'ye merhaba diyebilirsiniz! \*alkış efekti\*  

<p align="left">
  <img width="810" height="auto" src="https://github.com/frudotz/openwrt-xiaomi-4a-gigabit/blob/main/images/13.png">
</p>

> *\*OpenWRT paneline ilk girişinizde [System> Software](http://192.168.1.1/cgi-bin/luci/admin/system/opkg) altından tüm paket güncellemelerinizi kontrol edip yapınız.*  

# 💖 Özel Teşekkürler
Kaynak ve bilgi birikimiyle sağladığı destek için sevgili [@selcukssn](https://github.com/selcukssn)'e teşekkürler.  
Video rehber için [Mustafa Yücel](https://www.youtube.com/@yucellmustafa)'e teşekkürler.  

# 🤝 Katkıda Bulun / Bağış
  - Yanlış gördüğünüz veya eklemek istediğiniz şeyleri PR/Issue açarak iletebilirsiniz.  
  - Rehberimizi faydalı bulduysanız [🍻 bir bira ısmarlayarak](https://coff.ee/frudotz) bana destek olabilirsiniz.

# 🗃️ Kaynaklar
  - [OpenWRT Wiki](https://openwrt.org/inbox/toh/xiaomi/xiaomi_mi_router_4a_gigabit_edition)  
  - [Mi Router OpenWRT Ana Konusu - Donanım Haber Forum](https://forum.donanimhaber.com/xiaomi-mi-router-modelleri-ve-openwrt-firmware-ana-konu-openwrt-21-02-2-yayinlandi--135790478)  
  - [@acecilia/OpenWRTInvasion](https://github.com/acecilia/OpenWRTInvasion)  
  
-----------
🎀 Rehberimizi okuduğunuz için teşekkür ederiz!  
⭐ İçeriği faydalı bulduysanız desteklemek için **Star** verebilirsiniz.  
