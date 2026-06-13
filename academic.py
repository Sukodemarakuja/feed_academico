import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import streamlit as st

def rodar_bot():

    st.title("SukoProjec -Insta Feed Acadêmico")


    tema = st.text_input('Por qual tipo de artigo você esta pesquisando?')
    tema_en = GoogleTranslator(source="pt", target="en").translate (tema)
    tema_ajustado = tema_en.replace(" ", "+")


    if tema:
        url = f"http://export.arxiv.org/api/query?search_query=all:{tema_ajustado}&max_results=3"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            st.write('🟢Conectado ao ArXIV!')
            st.write("Esses foram os artigos encontrados:")

            sopa = BeautifulSoup(resposta.text, "xml")
            artigo = sopa.find_all("entry")

            if len(artigo) == 0:
                st.write("Nenhum artigo foi encontrado.")
            
            else:
                for item in artigo:
                    procura_titulo = item.find("title")
                    titulo_limpo= procura_titulo.text.strip()
                    st.subheader(titulo_limpo)

                    procura_resumo = item.find("summary")
                    resumo_limpo= procura_resumo.text.strip()

                    texto_pt=GoogleTranslator(source="en",
                    target='pt').translate(resumo_limpo)

                    st.write(texto_pt)

                    procura_link = item.find("id")
                    link_limpo = procura_link.text.strip()
                    st.link_button("Ler artigo completo ↗️", link_limpo)

        else:
            st.write('❌Não foi possivel conectar.')


if __name__ == "__main__":
    rodar_bot()