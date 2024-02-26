from deep_translator import GoogleTranslator 
tradutor = GoogleTranslator(source="pt", target="japanese")
texto = input("Digite o texto que gostaria de traduzir para japonês: ")
traducao = tradutor.translate(texto)
print (traducao) 


