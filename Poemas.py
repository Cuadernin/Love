import re
import urllib.request
from bs4 import BeautifulSoup
from random import randint

def value(filename="var.dat"):
    with open(filename, "a+") as fn:
        fn.seek(0)
        valor=int(fn.read() or 0)+1
        fn.seek(0)
        fn.truncate()
        fn.write(str(valor))
        return valor

def poema():
    valor=value()
    url='https://www.frasess.net/poemas-de-amor-cortos-y-romanticos-78.html'
    content=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(content,'html.parser')
    mydivs=soup.findAll("div",{"class":"quote_text"})
    s=[]
    for divs in mydivs:
        s.append(divs.text)
    poema=s[randint(0,len(s))]
    Subject=f'Poema {valor} de 30'
    message="""Subject:%s
    %s
    """ %(Subject,poema)
    return poema,Subject

#archivo=open("song.txt","w") 
#rchivo.write(fn)
