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
  <img width="auto" height="128" src="https://media.discordapp.net/attachments/796061773795033169/1046154532570280016/1.png">
  <img width="auto" height="128" src="https://media.discordapp.net/attachments/796061773795033169/1046152883617415258/2-8.png">
</p>

# 🚀 OpenWRT Kurulumu - <a href="https://drive.google.com/file/d/1acXFVIfmKuVZ597Adt3ZUU4ljYsQA8aM/view?usp=sharing" target="_blank">İndir</a>
Paylaştığımız **OpenWRTKurulum** klasörünü açın, `firmwares` dizininde OpenWRT'nin güncel sürümü bulunmalıdır.  
Rehberi yazdığımız tarihin güncel sürümünü sizler için bıraktık, güncel sürümü [buradan](https://openwrt.org/inbox/toh/xiaomi/xiaomi_mi_router_4a_gigabit_edition#installation) kontrol edip indirebilirsiniz.  
Dosyayı yerleştirdikten sonra ana dizindeki `0.start_main.bat` ve `5.start_write_OS.bat` dosyasını sırayla açıyoruz.  

- #### 1️⃣ İlk Aşama - 0.start_main.bat
> - `Enter router password:` kısmında script sizden ilk kurulumda belirlediğiniz şifreyi isteyecektir.  
> - Şifreyi girdikten sonra script birkaç değişiklikle cihazın telnet erişimini açacaktır.  
> - `Done` yanıtını aldığınızda herhangi bir tuşa basarak sekmeyi kapatabilirsiniz.  

<p align="left">
  <img width="auto" height="128" src="https://media.discordapp.net/attachments/796061773795033169/1046171865246339193/9.png">
  <img width="auto" height="128" src="https://media.discordapp.net/attachments/796061773795033169/1046171880903684126/10.png">
</p>

- #### 2️⃣ Son Aşama - 5.start_write_OS.bat
> - Bu scripti açtığınızda karşınıza alternatifiniz olmayan bir seçim ekranı gelir, **`1`**'i tuşlayıp devam ediniz.  
> - Router OpenWRT'den başlamak için birkaç kez yeniden başlar, bu kısımda cihaz asla güçten ayırılmamalıdır.  

<p align="left">
  <img width="auto" height="128" src="https://media.discordapp.net/attachments/796061773795033169/1046171891058098176/11.png">
  <img width="auto" height="128" src="https://media.discordapp.net/attachments/796061773795033169/1046171905318719498/12.png">
</p>

# 😎 Merhaba OpenWRT!
Kurulumda bir hata yapmadıysanız birkaç dakika içinde cihazın tüm ışıkları maviye döner ve internete erişebilirsiniz.  
Tebrikler! Artık doğruca [192.168.1.1](http://192.168.1.1/) adresine giderek OpenWRT'ye merhaba diyebilirsiniz! \*alkış efekti\*  

<p align="left">
  <img width="auto" height="128" src="https://media.discordapp.net/attachments/796061773795033169/1046171910540628048/13.png">
</p>
