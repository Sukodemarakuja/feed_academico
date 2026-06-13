import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def rodar_bot():
    url = "http://export.arxiv.org/api/query?search_query=all:videogames&max_results=3"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print('🟢Conectado ao ArXIV!')
        print("Esses foram os artigos encontrados:")

        sopa = BeautifulSoup(resposta.text, "xml")
        artigo = sopa.find_all("entry")


        for item in artigo:
            procura_titulo = item.find("title")
            titulo_limpo= procura_titulo.text.strip()
            print(titulo_limpo)

            procura_resumo = item.find("summary")
            resumo_limpo= procura_resumo.text.strip()

            texto_pt=GoogleTranslator(source="en",
            target='pt').translate(resumo_limpo)

            print(texto_pt)

    else:
        print('❌Não foi possivel conectar.')

    


if __name__ == "__main__":
    rodar_bot()