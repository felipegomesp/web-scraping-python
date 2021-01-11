import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://www.parablogueiros.com/blog/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

#pegar links da paginacao
links = soup.find(class_="pagination").find_all('a')

all_pages = []

for link in links:
    page = res.requests.get(link.get('href'))
    all_pages.append(BeautifulSoup(page.text, 'html.parser'))




all_post = []
for posts in all_pages:
    #    posts = soup.find_all(class_='post')
    # pegar os posts
    posts = posts.find_all(class_='post')
    for post in posts:
        #pegar a div com todas as informações
        info = post.find(class_='eltdf-post-text')
        #pegar o title que esta com a tag 'h3'
        title = info.h3.text
        #pegar o conteudo com tag 'p'
        preview = info.p.text
        #pegar imagem com src
        img =  post.find(class_='wp-post-image')['src']

        all_post.append({
            'title': title,
            'preview':preview,
            'img': img
        })

print(all_post)
with open('posts.json', 'w') as json_file:
    json.dump(all_post, json_file, indent=3, ensure_ascii=False)