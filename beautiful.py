from bs4 import BeautifulSoup
import requests

def funcaomemorias():

    page = requests.get('https://letterboxd.com/films/popular/').text
    soup= BeautifulSoup(page, 'lxml')
    movies = soup.find_all('div', class_ = "poster-list")

    lista = []
    id = 1 
    for movie in movies:
        
        title = movie.find('span', class_ ="frame-title")

        # preco_memoria = memoria.find('div', class_ = "col-md-1 preco").text.replace(' ','')
        # modelo_memoria = memoria.find('div', attrs= {"class": "col-md-2 center"}).text.replace(' ','')
        # descricao_memoria = memoria.find('div', class_ = "especificacao block-with-text").text.strip()
        item = {
            'title':title
        }
        lista.append(item)
        id = id + 1

    print(lista)
      
funcaomemorias()