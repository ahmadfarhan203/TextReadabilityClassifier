import nltk
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize, sent_tokenize
# cmudict ve punkt veri setlerini indir
nltk.download('cmudict')
nltk.download('punkt')
# cmudict'i yükle
d = cmudict.dict()
# Kelimenin hece sayısını hesapla
def count_syllables(word):
  try:
# cmudict kullanarak kelimenin hece sayısını al
    return [len(list(y for y in x if y[-1].isdigit())) for x in
    d[word.lower()]][0]
  except KeyError:
# cmudict'te kelime bulunamazsa, hece sayısını tahmin etmek için ünlü
  harfleri say
  return sum(1 for letter in word if letter in 'aeiouAEIOU')
# Flesch-Kincaid Okunabilirlik Seviyesi hesaplama
def flesch_kincaid_grade_level(text):
# Metni cümlelere böl
  sentences = sent_tokenize(text)
# Metni kelimelere böl
  words = word_tokenize(text)
# Toplam hece sayısını hesapla
  syllable_count = sum(count_syllables(word) for word in words)
# Cümle sayısını hesapla
  sentence_count = len(sentences)
# Kelime sayısını hesapla
  word_count = len(words)
# Flesch-Kincaid Okunabilirlik Seviyesi formülü
  grade_level = 0.39 * (word_count / sentence_count) + 11.8 * (syllable_count /
  word_count) - 15.59
return grade_level
# Okunabilirlik seviyesini belirleme
def determine_readability_level(grade_level):
  if grade_level < 6:
    return "İlkokul"
  elif 6 <= grade_level < 9:
    return "Ortaokul"
  elif 9 <= grade_level < 12:
    return "Lise"
  elif 12 <= grade_level < 16:
    return "Üniversite"
  else:
    return "Teknik Doküman"
# Analiz edilecek metin
text = """Burada örnek bir metin olacak. Metnin okunabilirlik seviyesini
belirleyeceğiz."""
# Okunabilirlik seviyesini belirle
grade_level = flesch_kincaid_grade_level(text)
readability_level = determine_readability_level(grade_level)
print("")
print("")
# Sonuçları yazdır
print(f"Metin: {text}")
print(f"Okunabilirlik Seviyesi: {readability_level} (Flesch-Kincaid Grade Level:
{grade_level:.2f})")
