lista_zakupów = {
"piekarnia" : ["chleb", "pączek", "bułki"],
"warzywniak" : ["marchew", "seler", "rukola"]
}
print ("Lista zakupów")
s = 0
for i in lista_zakupów.items():
    print (f"Idę do {i[0].capitalize()}. Kupuję tu następujące rzeczy: {[towar.capitalize() for towar in i[1]]}")
    s = s + len (i[1])
print (f"W sumie kupuję {s} produktów.")
print ("Jestem zadowolona z takich zakupów.")
    