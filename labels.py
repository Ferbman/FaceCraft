etiket_kelimeleri = {
    "5_o_Clock_Shadow": ["gölge sakal", "hafif sakal", "gögle sakallı", "hafif sakallı", "kirli sakallı"],
    "Arched_Eyebrows": ["kavisli kaş", "yay kaş", "kavisli kaşlı", "yay kaşlı"],
    "Attractive": ["çekici", "güzel", "yakışıklı"],
    "Bags_Under_Eyes": ["göz altı torbası", "yorgun gözler", "göz altı torbalı", "yorgun gözlü"],
    "Bald": ["kel", "saçsız", "dazlak"],
    "Bangs": ["perçem", "alın saçı", "perçemli", "alın açık", "kaküllü", "kahküllü"],
    "Big_Lips": ["kalın dudaklı", "dolgun dudak", "kalın dudak", "dolgun dudaklı"],
    "Big_Nose": ["büyük burun", "koca burun", "büyük burunlu", "koca burunlu", "karadenizli"],
    "Black_Hair": ["siyah saç", "kara saç", "siyah saçlı", "kara saçlı"],
    "Blond_Hair": ["sarışın", "sarı saç", "sarı saçlı"],
    "Blurry": ["bulanık", "net değil"],
    "Brown_Hair": ["kahverengi saç", "kızıl kahve saç", "kahverengi saçlı"],
    "Bushy_Eyebrows": ["kalın kaş", "yoğun kaş", "kalın kaşlı"],
    "Chubby": ["şişman", "tombul", "balık etli", "dombili"],
    "Double_Chin": ["çift gıdı", "gıdılı"],
    "Eyeglasses": ["gözlük", "gözlüklü"],
    "Goatee": ["top sakal", "keçi sakalı", "top sakallı", "keçi sakallı"],
    "Gray_Hair": ["gri saç", "beyaz saç", "beyaz saçlı", "gri saçlı"],
    "Heavy_Makeup": ["ağır makyaj", "yoğun makyaj", "çok makyajlı", "makyajlı", "ağır makyajlı", "yoğun makyajlı"],
    "High_Cheekbones": ["belirgin elmacık", "yüksek elmacık kemiği", "elmacık kemikli"],
    "Male": ["erkek", "adam"],
    "Mouth_Slightly_Open": ["açık ağız", "hafif açık ağız", "ağzı hafif açık"],
    "Mustache": ["bıyık", "bıyıklı"],
    "Narrow_Eyes": ["çekik göz", "dar göz", "çekik gözlü", "çinli", "japon", "koreli", "dar gözlü", "vietnamlı"],
    "No_Beard": ["sakalsız"],
    "Oval_Face": ["oval yüz", "yuvarlak yüz", "oval yüzlü", "yuvarlak yüzlü"],
    "Pale_Skin": ["soluk ten", "açık ten", "beyaz ten", "soluk tenli", "açık tenli"],
    "Pointy_Nose": ["sivri burun", "ince burun", "sivri burunlu", "ince burunlu"],
    "Receding_Hairline": ["açılmış alın", "gerileyen saç", "geriye atılmış saç"],
    "Rosy_Cheeks": ["pembe yanak", "al yanak", "pembe yanaklı", "al yanaklı"],
    "Sideburns": ["favori", "yan sakal", "favorili"],
    "Smiling": ["gülümseyen", "gülümsüyor", "güler yüzlü", "gülen"],
    "Straight_Hair": ["düz saç", "düz saçlı"],
    "Wavy_Hair": ["dalgalı saç", "dalgalı saçlı"],
    "Wearing_Earrings": ["küpe takmış", "küpeli"],
    "Wearing_Hat": ["şapka", "şapkalı", "kasketli"],
    "Wearing_Lipstick": ["ruj sürmüş", "rujlu"],
    "Wearing_Necklace": ["kolyeli", "kolye takmış"],
    "Wearing_Necktie": ["kravat", "kravatlı"],
    "Young": ["genç", "delikanlı", "toy"]
}

# Etiket sıralaması sabit tutulmalı
etiket_sirasi = list(etiket_kelimeleri.keys())

def metni_etiketle(text):
    text = text.lower()
    label_vector = []
    for etiket in etiket_sirasi:
        kelimeler = etiket_kelimeleri[etiket]
        if any(kelime in text for kelime in kelimeler):
            label_vector.append(1)
        else:
            label_vector.append(-1)
    return label_vector