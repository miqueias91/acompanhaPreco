import requests
from Classe import Classe
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import errorcode

cl = Classe()

dados = cl.buscaProduto()
cl.buscaLojaPreco(dados)