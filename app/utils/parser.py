import logging
import requests
from datetime import datetime
from bs4 import BeautifulSoup

import app.config as config
from app.db.settings import SessionLocal
from app.exceptions import NotAvailableURL
from app.logic.news import create_news
from app.schemas import NewsCreateSchema


async def parse_news():
    """Парсинг новостей с сайта метро."""

    logging.info("start parse_news func")

    news = []
    url = config.METRO_SITE_URL

    try:
        response = requests.get(url, headers=config.PARSING_HEADERS)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logging.info(f"URL адрес {url} недоступен, ошибка: {err}")
        raise NotAvailableURL("URL адрес недоступен")

    soup_runner = BeautifulSoup(response.content, "html.parser")
    main_table = soup_runner.find(
        "table",
        attrs={
            "width": "95%",
            "cellpadding": "0",
            "cellspacing": "10",
            "border": "0",
            "style": "font-family:Arial;font-size:15px",
        },
    )
    news_items = main_table.find_all("tr")
    image_prefix = config.IMAGE_PREFIX

    async with SessionLocal() as db:
        for item in news_items:
            try:
                date_element = item.find("b")
                title_parent_element = item.find("font", size="3")
                title_element = title_parent_element.find("b")
                image_element = item.find("img").get("src")
            except (AttributeError, TypeError):
                # предполагаем, что новость должна иметь все элементы
                continue

            news_data = NewsCreateSchema(
                title=title_element.text,
                image_url=image_prefix + image_element,
                publication_date=datetime.strptime(
                    date_element.text, "%d.%m.%Y"
                ).date(),
            )

            news.append(news_data)
        # можно было бы еще добавить проверку на существование новости в БД
        await create_news(db=db, news=news)
    return news
