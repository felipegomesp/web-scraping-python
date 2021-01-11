import requests
from bs4 import BeautifulSoup
import json
#track = input('Informe o número da nota fiscal: ')
res = requests.get('https://ssw.inf.br/2/tracking/18025220000135/7463')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

# pegar os posts
posts = soup.find(class_='table')
all_post = []
for post in posts.find_all('tr'):
    for td in post.find_all('td'):
#pegar a div com todas as informações
        info = td.find_all('p')
        tdb = posts.find_all(class_='tdb')
        # #pegar o title que esta com a tag 'h3'
        #title = tdb.p.text
        # #pegar o conteudo com tag 'p'
        # preview = info.p.text
        # #pegar imagem com src
        # img =  post.find(class_='wp-post-image')['src']
        #
    all_post.append({
        'Situacao': info,
        #   '\n Descricao': tdb
        #     'preview':preview,
        #     'img': img
         })
print(all_post)
#print(all_post)
# with open('posts.json', 'w') as json_file:
#     json.dump(str(all_post), json_file, indent=3, ensure_ascii=False)
arquivo = open('teste2.txt', 'w')
arquivo.write(str(all_post))
arquivo.close()