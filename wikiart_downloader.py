import requests
from bs4 import BeautifulSoup as bs
from os import mkdir
from tqdm import tqdm

# !!! ARGUMENTS !!!
image_resolution = ['!PinterestSmall.jpg', '!PinterestLarge.jpg', '!Portrait.jpg', '!Blog.jpg', '!Large.jpg', ''][0]  # В последних скобочках ставить число от 0 до 5. Чем больше число, тем больше разрешение
folder = 'van_gog'  # Имя папки, куда будут сохранены изображения
# !!! ARGUMENTS !!!

all_pics = bs(requests.get('https://www.wikiart.org/ru/vinsent-van-gog/all-works/text-list').text, "html.parser")
try:
    mkdir(folder)
except FileExistsError:
    pass

for i, link in enumerate(tqdm(list(filter(lambda x: (len(x.attrs) == 1) and ('href' in x.attrs), all_pics.findAll('a')))[:200])):
    img_link = bs(requests.get('https://www.wikiart.org{}'.format(link.attrs['href'])).text, "html.parser").findAll('img', {'itemprop': 'image'})[0].attrs['src'].split('!')[0] + image_resolution
    with open('{}/{}.jpg'.format(folder, i + 1), 'wb') as f:
        f.write(requests.get(img_link).content)
