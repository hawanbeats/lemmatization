import stanza # type: ignore

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
