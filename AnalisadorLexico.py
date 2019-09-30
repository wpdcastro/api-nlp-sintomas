from unicodedata import normalize
from tabulate import tabulate
import json
import nltk 
from nltk.stem import RSLPStemmer

class AnalisadorLexico():

    reservados = [
                    "azia", 
                    "palpitacao", 
                    "Pressão Alta",
                    "falta de ar",
                    "fadiga" ,
                    "vomito",
                    "dor nas juntas",
                    "tosse",
                    "vermelidao"
    ]

    lista_sintomas = []

    simbolos_especiais = [",", ".","*",":","-","\"", "\'"] 

    def remover_acentos(self,txt):

        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')   

    def tokenizar(self, frase) :

        frase = frase.split()

        array_tokenizado = []
        sintomas = []
        # arvore de derivação
        linha_tokenizado = []
        for token in frase:
            token_lower = token.lower()
            token_lower = self.remover_acentos(token_lower)

            if token_lower in self.reservados:
                #linha_tokenizado = [token,frase]
                #linha_tokenizado = {"token" : token, "frase" : frase}
                if token not in sintomas : 
                    sintomas.append(token) 


        return sintomas  
            #array_tokenizado.append(linha_tokenizado)

f = open("consulta.txt","r+")

al = AnalisadorLexico()

frases = ["Tenho azia","tenho palpitacao", "tosse", "tenho tosse e azia"]

frase = "Tenho azia e palpitacao , uma tosse leve e só"

res = al.tokenizar(frase)

par_json = {"sintomas" : res}

par_json = json.dumps(par_json)

print(par_json)