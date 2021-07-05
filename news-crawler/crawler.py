# News Crawler
# Forked from https://github.com/SyphonArch/news-relay

import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from sender import send

BASE_ADDRESS = "https://news.naver.com/"

NEWS_DIRECTORY = "/news"


def get(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_section_name(section):
    return section.find("h4").text


def get_articles(section):
    entries = section.find_all("li")
    links = [entry.find("a") for entry in entries]
    articles = {}
    for link in links:
        title = link.text.strip()
        url = link["href"]
        articles[title] = url
    return articles


def get_overview(section, expanded=False):
    section_name = get_section_name(section)
    articles = get_articles(section)
    separator = "\n-------------------\n"
    return section_name + separator + "||\n".join(articles.keys()) + "||\n"


def get_body_text(article, chars=300):
    html = str(article.find("div", {"id": "articleBodyContents"}))
    edited_html = re.sub("<br/>", "\n", html)
    article_contents = BeautifulSoup(edited_html, "html.parser").text
    formatted = re.sub("\n", " ", article_contents)
    formatted = re.sub("\t", "", formatted)
    formatted = re.sub(" +", " ", formatted)
    formatted = re.sub(r"\.\s", r".\n", formatted)

    return formatted[:chars].strip()


def get_details(section):
    articles = get_articles(section)
    details = []
    for title in articles:
        url = articles[title]
        article = get(BASE_ADDRESS + url)
        details.append("----------------------------")
        details.append(f"[{title}]")
        details.append(get_body_text(article) + "\n")
    return "\n".join(details)


soup = get(BASE_ADDRESS + "main/home.nhn")
sections = soup.find_all("div", {"class": "main_component droppable"})

overview = []
for section in sections:
    overview.append(get_overview(section))

overview_output = "\n".join(overview)

headline_section = sections[0]
headlines_details_output = get_details(headline_section)


now = "{:%Y-%m-%d_%H}H".format(datetime.now())
send(f"[NEWS] NEWS OVERVIEW ({now})", overview_output)
send(f"[NEWS] ARTICLE SNIPPETS ({now})", headlines_details_output)


with open(f"{NEWS_DIRECTORY}/overview/{now}_overview.txt", "w") as f:
    f.write(overview_output)
with open(f"{NEWS_DIRECTORY}/details/{now}_details.txt", "w") as f:
    f.write(headlines_details_output)
