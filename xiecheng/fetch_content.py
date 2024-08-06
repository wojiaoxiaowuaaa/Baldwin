# coding:utf-8
import asyncio
import os
import sys
import time
import aiohttp
from bs4 import BeautifulSoup

# if (BASE_PATH := os.path.abspath('.')) not in sys.path: sys.path.insert(0, BASE_PATH)
from gongju.mysql_operate import *


async def fetch_content(url):
    # 异步获取URL内容并返回文本数据
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, "lxml")

    movie_names, urls_to_fetch, movie_dates = [], [], []

    all_movies = init_soup.find("div", id="showing-soon")

    for each_movie in all_movies.find_all("div", class_="item"):
        all_a_tag = each_movie.find_all("a")
        all_li_tag = each_movie.find_all("li")

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]["href"])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in urls_to_fetch]
    # 建一个任务列表，每个任务都是获取一个电影详情页的内容。使用asyncio.gather并行执行所有任务
    pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, "lxml")
        img_tag = soup_item.find("img")
        print("{} {} {}".format(movie_name, movie_date, img_tag["src"]))
        # 将数据写到MySQL(测试通过)
        # db.execute_db("INSERT INTO movies(movie_name, movie_, img_url) VALUES (%s, %s, %s)", (movie_name, movie_date, img_tag["src"]))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print("协程爬虫运行耗时{}秒".format(end - start))
