FaceCraft - Metin Tabanlı İnsan Yüzü Modeli Çizimi

Bu proje, metin tabanlı girdileri kullanarak bu girdilere uygun, gerçekçi insan yüzü modelleri çizmeyi amaçlayan bir yapay zeka uygulamasıdır. Kullanıcıların belirlediği anahtar kelimelerle, istenilen özelliklere sahip yüzler otomatik olarak oluşturulur.
Proje Amacı

Kullanıcıların doğal dil girdileri (anahtar kelimeler) aracılığıyla, tanımlanan özelliklere uygun, yüksek kaliteli ve çeşitli insan yüzü görselleri üretmek. Bu proje, özellikle görsel içerik üretimi, karakter tasarımı ve kişiselleştirilmiş avatar oluşturma gibi alanlarda potansiyel kullanım alanları sunmaktadır.
Özellikler

    Metinden Yüze Üretim: Anahtar kelime tabanlı etiketleme kullanarak metin girdilerinden insan yüzü görselleri üretir.

    Yüksek Kaliteli Çıktı: Üretilen yüz modelleri, StyleGAN3-Fun GAN modelinin gücü sayesinde yüksek fotogerçekçilik ve detay seviyesine sahiptir.

    Öznitelik Kontrolü: Veri setindeki 40 farklı etiket sayesinde, üretilen yüzlerin yaş, cinsiyet, saç rengi, göz rengi gibi birçok özelliğini kontrol etme yeteneği.

    Web Arayüzü: Kullanıcı dostu bir web arayüzü aracılığıyla kolay erişim ve etkileşim imkanı sunar.

Teknolojiler ve Modeller

Bu proje aşağıdaki ana teknolojiler ve modeller kullanılarak geliştirilmiştir:

    Programlama Dili: Python

    Web Çatısı: Flask (Web arayüzü için)

    Derin Öğrenme Çatısı: PyTorch (Torch kütüphanesi)

    Görüntü İşleme: Pillow

    Sayısal İşlemler: NumPy

    GAN Modeli: StyleGAN3-Fun GAN

        Model, CelebA veri seti üzerinde 30.000 fotoğraf ve her fotoğraf için 40 etiket kullanılarak eğitilmiştir.

        Eğitim sonucunda FID (Fréchet Inception Distance) değeri 26'ya kadar düşürülerek yüksek üretim kalitesi elde edilmiştir.

    Metin İşleme: Anahtar kelime tabanlı etiketleme sistemi kullanılmıştır.

Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:
Gereksinimler

    Python 3.8 veya üzeri

    CUDA uyumlu bir GPU (eğitim ve hızlı üretim için önerilir)

    Gerekli Python kütüphaneleri (aşağıda belirtilmiştir)

Kurulum Adımları

    Projeyi klonlayın:
    git clone https://github.com/Ferbman/FaceCraft.git

    Proje dizinine gidin:
    cd FaceCraft

    Gerekli kütüphaneleri yükleyin:
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 (GPU için, CUDA sürümünüze göre ayarlayın)
    pip install pillow numpy flask

    Model indirme linki https://drive.google.com/file/d/1A8A3RqPdZqmj0PApPI6iZPdEjdHP7AT3/view?usp=drive_link

    Modeli indirin ve dosya dizinine taşıyın
   


Kullanım

    Python app.py ile projeyi çalıştırın ve console da cıkan linke gidin 
Web Arayüz
FaceCraft, kullanıcıların kolayca etkileşim kurabilmesi için bir Flask web arayüzüne sahiptir. Bu arayüz üzerinden metin girdileri sağlanarak yüz modelleri oluşturulabilir ve görüntülenebilir.

![resim](https://github.com/user-attachments/assets/b72a139a-94c1-42ec-9d5d-2c211de3de2d)


Veri Seti

    Adı: CelebA (Large-scale CelebFaces Attributes Dataset)

    Kullanım: 30.000 adet fotoğraf

    Etiketler: Her fotoğraf için 40 farklı öznitelik etiketi (örn. yaş, cinsiyet, saç rengi, gözlük, gülümseme vb.)

Performans

Model, StyleGAN3-Fun GAN mimarisi kullanılarak eğitilmiş ve üretim kalitesi FID (Fréchet Inception Distance) metriği ile değerlendirilmiştir. Elde edilen FID değeri 26'dır, bu da üretilen görsellerin gerçekçi ve çeşitli olduğunu göstermektedir.
Lisans
