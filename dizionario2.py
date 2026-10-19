meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "BADDIE" : "significa originariamente “cattivo” o “villain”"
            }
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
if parola in meme_dict.keys():
    print(meme_dict[parola])
else:
    print("Queasta parola non esiste o non ce nel dizionario")
