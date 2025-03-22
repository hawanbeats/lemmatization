# Lemmatization Example with Stanza

## Proje Özeti
Bu Python kodu, **Stanza** kütüphanesini kullanarak verilen metindeki her kelimenin kök halini elde eder. Kullanıcıdan alınan metin üzerinde lemmatization işlemi yapılır ve kelimeler köklerine dönüştürülerek ekrana yazdırılır.

## Çalıştırma Adımları
1. Python ve Gerekli Kütüphaneleri Yükleme
- Python'un yüklü olduğundan emin olun. Python 3.x sürümü önerilir.
- Stanza kütüphanesini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:
``
pip install stanza
``
2. Stanza Veri Setlerini İndirme
- İlk defa kullanıyorsanız, Stanza'nın dil modeli verisini indirmeniz gerekebilir. Aşağıdaki komutla İngilizce dil modeli indirilebilir:
```python
import stanza
stanza.download('en')  # İngilizce için
```
Türkçe dil modeli için ise şu komut kullanılabilir:
```python
stanza.download('tr')  # Türkçe için
```
3. Kodun Çalıştırılması
- ``text`` değişkenine istediğiniz metni girin. Kod, metindeki kelimeleri lemmatize ederek sonucu ekrana yazdıracaktır.

## Kod Açıklaması
```python
import stanza  # type: ignore

# NLP pipeline başlat
nlp = stanza.Pipeline("en")  # İngilizce için
# nlp = stanza.Pipeline("tr")  # Türkçe için kullan (Önerilir)

# Kullanıcıdan metin al
text = input("Lütfen bir metin girin: ")

# Stanza ile analiz et
doc = nlp(text)

# Lemmatization işlemi
lemmatized_words = [word.lemma for sent in doc.sentences for word in sent.words]

# Sonucu ekrana yazdır
print("Lemmatized Metin:", " ".join(lemmatized_words))
```
- ``stanza.Pipeline("en")``: Bu komut, Stanza'nın İngilizce dil modelini başlatır. Türkçe için ``stanza.Pipeline("tr")`` kullanılabilir.
- Lemmatization: Bu işlem, her kelimeyi kök haline getirir. Örneğin, "running" kelimesi "run" olarak dönüştürülür.

## Örnek Çıktı
- Girdi:
```
The boys are running in the park.
```
- Çıktı:
```
Lemmatized Metin: the boy be run in the park.
```
## Katkıda Bulunma
Katkıda bulunmak isterseniz, önerilerinizi veya hataları GitHub issues bölümünde paylaşabilir veya pull request gönderebilirsiniz.
