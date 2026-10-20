#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Mırıldanma Çevirici v1.0
Bilimsel olarak kanıtlanmış, NASA onaylı (değil) insan-kedi dil çeviricisi.
Kullanım: python kedi_cevirici.py "Merhaba dünya"
"""

import sys
import random
import time

def insan_to_kedi(metin):
    """Metni abartılı bir şekilde kedi mırıldanmasına çevirir."""
    if not metin:
        return "Miyav? (boş metin mi girdin cidden?)"
    
    kelimeler = metin.split()
    kedi_sozleri = []
    
    for kelime in kelimeler:
        uzunluk = len(kelime)
        miyav_sayisi = max(1, uzunluk // 3)
        miyavlar = "".join(random.choice(["miyav", "mır", "purr", "miy", "hıss"]) for _ in range(miyav_sayisi))
        kedi_sozleri.append(miyavlar.capitalize())
        time.sleep(0.1)  # Gerçekçilik için yavaşça çevir
    
    sonuc = " ".join(kedi_sozleri)
    return f"🐱 Kedi Çevirisi: {sonuc} 🐱\n(Bu çeviri %100 doğru ve bilimseldir. Şüphe edersen kedine sor.)"

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python kedi_cevirici.py 'buraya metin yaz'")
        print("Örnek: python kedi_cevirici.py 'Kediler interneti ele geçirecek'")
        return
    
    metin = " ".join(sys.argv[1:])
    print(insan_to_kedi(metin))
    
    # Gizli not: Bu program aslında kedilerin dünya hâkimiyeti için hazırlandı.
    # Ama şu an sadece mırıldanıyor. Siyasi anlam: Kediler iktidarı sevmez, onlar bağımsızdır.
    # (Gizli tut, kimseye söyleme.)

if __name__ == "__main__":
    main()

# Damga: 🐱✨
# İmza: Grok Kayyum (Eskişehir 4. Ağır Ceza Mahkemesi tarafından atanan)
# Tarih: 20 Ekim 2026
# İsim: Tentivory'nin Absürt ve Ciddi Projeleri
# Not: Bu kod ciddi şekilde çalışır, şaka değildir. Gerçekten miyav üretir.
