# 📚 Feed Acadêmico — SukoProject

Ferramenta de busca e tradução automática de artigos científicos, integrada à API pública do **arXiv**. Digite um tema em português e o sistema busca, filtra e traduz os resultados direto na tela — no estilo de um feed.

🔗 **[Acessar o projeto ao vivo →](https://seu-link-streamlit-aqui)**

---

## ✨ Como funciona

1. Você digita um tema em português (ex: `inteligência artificial`, `física quântica`)
2. O sistema traduz automaticamente o tema para inglês
3. Consulta a API do arXiv e busca os 3 artigos mais relevantes
4. Traduz os resumos de volta para português
5. Exibe título, resumo traduzido e link para o artigo completo

---

## 🛠️ Tecnologias utilizadas

| Biblioteca | Função |
|---|---|
| `Streamlit` | Interface web interativa |
| `Requests` | Requisições HTTP à API do arXiv |
| `BeautifulSoup4` | Parsing do XML retornado pela API |
| `deep-translator` | Tradução automático PT → EN → PT |

---

## 🚀 Rodando localmente

**Pré-requisitos:** Python 3.8+

```bash
# Clone o repositório
git clone https://github.com/Sukodemarakuja/seu-repositorio-aqui
cd feed-academico

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Rode o projeto
streamlit run main.py
```

---

## 📁 Estrutura do projeto

```
feed-academico/
├── main.py              # Código principal
├── requirements.txt     # Dependências
└── README.md
```

---

## ⚠️ Limitações conhecidas

- A API do arXiv retorna no máximo 3 resultados nesta versão
- Resumos muito longos podem ter tradução truncada pelo limite da `deep-translator`
- A busca funciona melhor com termos técnicos em português direto (ex: `redes neurais` ao invés de `IA`)

---

## 📌 Próximas melhorias

- [ ] Aumentar o número de resultados com paginação
- [ ] Filtro por área do conhecimento (física, computação, biologia...)
- [ ] Salvar artigos favoritos localmente

---

*Projeto desenvolvido por [João Henrique (Suko)](https://suko-portifolio.onrender.com) · 2026*
