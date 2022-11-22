# Mi Router 4A için Türkçe OpenWRT rehberi 
Bu rehberimiz ile Windows üzerinden Xiaomi Mi Router 4A Gigabit Edition model routerınıza çok kısa bir süre içinde OpenWRT kurabileceksiniz.  
Paylaştığımız yöntem yalnızca MediaTek MT7621 SoC tabanlı, Mi 4A Gigabit modeli için geçerlidir, diğer modellerde denemek cihazı kullanılmaz hale getirebilir.
*Bu işlemlerde karşılaşabileceğiniz tüm komplikasyonlar sizin sorumluluğunuzdadır. Konuyla hiçbir sorumluluk kabul etmiyorum...*  

# ✨ Başlarken
OpenWRT kurulumu öncesi Mi 4A Giga routerımızın kendi yazılımıyla ilk kurulumunu tamamlamamız gerekiyor.  
Modemimizin LAN portundan alacağımız çıkışı routerın WAN portuna, routerın LAN portundan alacağımız çıkışı da bilgisayarımızın ethernet portuna takıyoruz.  
Tarayıcınızdaki açık sekmede "İnternete erişebilmek için önce bu ağa giriş yapmalısınız." uyarısıyla karşılaşabilirsiniz.  
Uyarıyla karşılaşırsanız yanındaki butona tıklayabilir ya da kendiniz [router.miwifi.com](https://router.miwifi.com/) veya [192.168.31.1](https://192.168.31.1/) adresine gidebilirsiniz.  

### MiWifi Kurulumu
> MiWifi kurulum sekmesine ulaştığınızda sağ üstten dilinizi seçerek başlayın.  
> Alt kısımdan ülke seçimini de yaptıktan sonra tikleri işaretleyip ilerleyin.  
> Router kablolu bağlantıyı tespit edip otomatik olarak DHCP modunu seçecektir ilerleyin.  
> Mod seçiminde bir hata olursa kendiniz maneul olarak DHCP seçebilirsiniz.  
> Wi-Fi Ayarları sekmesini kurulumu bitirebilmek için basitçe doldurun. (Şifrenizi unutmayın.)  
> Kurulum tamamlandığında cihaz yeniden başlayacaktır, ışıklar maviye döndüğünde sayfayı yenileyin.  
> Router giriş sayfası sizi karşılayacaktır, bu arayüzdeki işimizi tamamlamış bulunuyoruz.  

# 🚀 OpenWRT Kurulumu
Paylaştığımız linkten indirdiğiniz OpenWRTKurulum klasörünü açın, firmwares klasörü altında OpenWRT'nin en güncel sürümü bulunmalıdır.  
Rehberi paylaştığımız tarih itibarıyla en güncel sürümü sizler için bıraktık, en güncel sürümü [buradaki linkten](https://openwrt.org/inbox/toh/xiaomi/xiaomi_mi_router_4a_gigabit_edition#installation) kontrol edebilir ve indirebilirsiniz.  
