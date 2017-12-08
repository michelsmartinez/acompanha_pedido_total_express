#coding: utf-8

import requests
import os
from bs4 import BeautifulSoup
import re
import emailpy
import time


def get(url, de, senha, para):
    r = requests.get(url)
    html_source = r.text
    soup = BeautifulSoup(html_source, 'html.parser')
    td_tags = soup.find_all('font')
    cont = 1
    msg = ""
    while cont < len(td_tags) - 2:
        data = re.sub(r"<.+?>", "", str(td_tags[cont])).strip()
        cont += 1
        hora = re.sub(r"<.+?>", "", str(td_tags[cont])).strip()
        cont += 1
        status = re.sub(r"<.+?>", "", str(td_tags[cont])).strip()
        cont += 1
        msg += ("{} {} ->  {}.\n".format(data, hora, status))

    log = open('./status.log', 'r')
    status_anterior = ''.join(log.readlines())

    if status_anterior != msg:
        log.close()
        emailpy.send(de, senha, para, 'Status modificado', msg)
        log = open('./status.log', 'w')
        log.write(msg)
    log.close()


if __name__ == '__main__':
    frequencia = int(os.sys.argv[5])
    while True:
        get(str(os.sys.argv[1]),
            str(os.sys.argv[2]),
            str(os.sys.argv[3]),
            str(os.sys.argv[4]))
        time.sleep(frequencia)
