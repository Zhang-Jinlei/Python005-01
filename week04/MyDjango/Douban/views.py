from django.shortcuts import render

# Create your views here.
import requests
from .models import Movies
from lxml import etree

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
}


def index(request, mid=1291818, title='饮食男女'):
    movie = Movies.objects.filter(stars__gt=3, name=title).all()
    if movie:
        data = movie
    else:
        _crawl_movies(mid, title)
        data = Movies.objects.filter(stars__gt=3, name=title).all()
    return render(request, 'index.html', locals())


def _crawl_movies(mid, title):
    url = f"https://movie.douban.com/subject/{mid}/comments"
    response = requests.get(url, headers=HEADERS).text
    htmls = etree.HTML(response).xpath('//div[@class="comment-item "]')
    for html in htmls:
        comment = html.xpath('.//p/span/text()')[0]
        time = html.xpath('.//h3/span[2]/span[3]/@title')[0]
        stars = html.xpath('.//h3/span[2]/span[2]/@title')[0]

        # print(comment, time, stars, mid)

        _insert(name=title, comment=comment, create_time=time, stars=get_star(stars))


def _insert(**kwargs):
    Movies.objects.create(**kwargs)


def get_star(star):
    if star == '力荐':
        return 5
    elif star == '推荐':
        return 4
    elif star == '还行':
        return 3
    elif star == '较差':
        return 2
    elif star == '很差':
        return 1
