lista_zakupów = {
"piekarnia" : ["chleb", "pączek", "bułki"],
"warzywniak" : ["marchew", "seler", "rukola"]
}
print ("Lista zakupów")
for i in lista_zakupów.items():
    print (f"Idę do {i[0].capitalize()}. Kupuję tu następujące rzeczy: {[towar.capitalize() for towar in i[1]]}")
    