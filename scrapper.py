from tkinter import COMMAND
import requests as r
from bs4 import BeautifulSoup as bs

import UserAgents as ua
import random

baseURL = "https://knihobot.cz"
googleAnal = "?utm_source=knihobotbot&utm_medium=twitter"


def createUserAgents():
    return f"User-Agent : ${ua.UserAgents[random.randint(0,len(ua.UserAgents)-1)]}"

def get(url):
    headers = createUserAgents()
    page = r.get(url,headers)
    return page

def soup(page):
    return bs(page.content, 'html.parser')

def encode_url(base,search):
    import urllib.parse
    term = urllib.parse.quote_plus(search)
    return f"{base}?q={term}"

def sale():
    return "/kategorie/299"

def randomPick(books):
    import random
    book = books[random.randint(0, len(books))]
    return book


def bookSaleRandom():
    return soup(get("https://knihobot.cz/kategorie/299"))

def bookSearchURL(term):
    return encode_url("https://knihobot.cz/hledani",term)

def bookSearchItems(base, term):
    return soup(get(encode_url(base, term)))

def getBook(res, position,israndom=False):
    if israndom:
        books = res.find_all("h2", class_="h3")
        book = randomPick(books)
    else:
        books = res.find_all("h2", class_="h3")
        book = books[position]
    link = book.parent.get("href")
    return link

def parseMention(mention):
    try:
        mentionList = mention.split("-")
        command = mentionList[0].lower().strip()
        if command  == "hledej nahodna":
            res = bookSearchItems("https://knihobot.cz/hledani",mentionList[1].strip())
            res = getBook(res, "", True)
            return res
        elif command  == "hledej":
            serch = mentionList[1].strip()
            return bookSearchURL(serch)
        elif command  == "vyprodej nahodna":
            res = bookSaleRandom()
            res = getBook(res,  "", True)
            return res
        elif command  == "vyprodej":
            return sale()
        elif command  == "najdi":
            res = bookSearchItems("https://knihobot.cz/hledani",str(mentionList[1]).strip())
            res = getBook(res, 0, False)
            return res
        else:
            return "Nerozumím příkazu, použijte podporovanou syntax"
    except Exception as e:
        print(e)
        return("Špatně zadaný příkaz.")

def main(tweetContent): #random code here
    response = parseMention(tweetContent)
    if response[0] == "/":
        return baseURL+response+googleAnal
    else:
        return response
