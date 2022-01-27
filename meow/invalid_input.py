from assets import texts, texts_en

def invalid_input(language):
  if language == "br":
    print(texts.invalid_input[0] + "\n")
  elif language == "en":
    print(texts_en.invalid_input[0] + "\n")