# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.realpath('.'))
import mysql.connector
from mysql.connector import errorcode
import requests
from bs4 import BeautifulSoup

class Classe:

	def getInstance(self):
		try:
			db_connection = mysql.connector.connect(host='92.249.44.1', user='u949944707_agad', password='fin4278homer1002', database='u949944707_agad')
			return db_connection
		except mysql.connector.Error as error:
			if error.errno == errorcode.ER_BAD_DB_ERROR:
				return None
			elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				return None
			else:
				return error
		else:
			db_connection.close()

	def buscaProduto(self):
		db_connection = self.getInstance()
		cursor = db_connection.cursor()
		sql = ("SELECT id_acompanhapreco_item, link, idacompanhapreco_loja, nomeloja, idacompanhapreco_user, nome, email FROM acompanhapreco_item i inner join acompanhapreco_loja l on l.id_acompanhapreco_loja = i.idacompanhapreco_loja inner join acompanhapreco_user u on u.id_acompanhapreco_user = i.idacompanhapreco_user WHERE 1")
		cursor.execute(sql)
		myresult = cursor.fetchall()
		cursor.close()
		db_connection.commit()
		db_connection.close()

		return myresult

	def buscaLojaPreco(self, dados):
		if dados:
			for x in dados:
				if x[3] == 'MAGAZINE LUIZA':
					self.buscaPrecoMagazineLuiza(x)
				elif x[3] == 'AMERICANAS':
					self.buscaPrecoAmericanas(x)
				elif x[3] == 'COLOMBO':
					self.buscaPrecoColombo(x)
				elif x[3] == 'RICARDO ELETRO':
					self.buscaPrecoRicardoEletro(x)
				elif x[3] == 'O BOTICARIO':
					self.buscaPrecoBoticario(x)

	def buscaPrecoMagazineLuiza(self, dados):
		if dados:
			response = requests.get(dados[1])
			if response.status_code == 200:
				html_soup = BeautifulSoup(response.text, 'html.parser')
				type(html_soup)			
				preco_containers = html_soup.find_all('span', class_ = 'price-template__text')
				preco = preco_containers[0]
				preco = preco.text.replace(".", "")
				preco = preco.replace(",", ".")

				self.atualizaPreco(str(preco), str(dados[0]))

	def buscaPrecoAmericanas(self, dados):
		if dados:
			response = requests.get(dados[1])
			if response.status_code == 200:
				html_soup = BeautifulSoup(response.text, 'html.parser')
				type(html_soup)
				preco_containers = html_soup.find_all('span', class_ = 'price__SalesPrice-ej7lo8-2')
				preco = preco_containers[0]
				preco = preco.text.replace("R$ ", "")
				preco = preco.replace(".", "")
				preco = preco.replace(",", ".")

				self.atualizaPreco(str(preco), str(dados[0]))

	def buscaPrecoRicardoEletro(self, dados):
		if dados:
			response = requests.get(dados[1])
			if response.status_code == 200:
				html_soup = BeautifulSoup(response.text, 'html.parser')
				type(html_soup)
				preco_containers = html_soup.find_all('span', itemprop = 'lowPrice')
				preco = preco_containers[0]
				preco = preco.text.replace(".", "")
				preco = preco.replace(",", ".")

				self.atualizaPreco(str(preco), str(dados[0]))

	def buscaPrecoColombo(self, dados):
		if dados:
			response = requests.get(dados[1])
			if response.status_code == 200:
				html_soup = BeautifulSoup(response.text, 'html.parser')
				type(html_soup)
				preco_containers = html_soup.find_all('span', class_ = 'dados-preco-valor--label')
				preco = preco_containers[0]
				preco = preco.text.replace("R$ ", "")
				preco = preco.replace(".", "")
				preco = preco.replace(",", ".")

				self.atualizaPreco(str(preco), str(dados[0]))

	def buscaPrecoBoticario(self, dados):
		if dados:
			response = requests.get(dados[1])
			if response.status_code == 200:
				html_soup = BeautifulSoup(response.text, 'html.parser')
				type(html_soup)
				preco_containers = html_soup.find_all('div', class_ = 'nproduct-price-value')
				preco = preco_containers[0]
				preco = preco.text.replace("R$ ", "")
				preco = preco.replace(".", "")
				preco = preco.replace(",", ".")

				self.atualizaPreco(str(preco), str(dados[0]))

	def atualizaPreco(self, valor, item):
		db_connection = self.getInstance()
		cursor = db_connection.cursor()
		sql = ("INSERT INTO acompanhapreco_preco (valor, idacompanhapreco_item) VALUES (%s,%s)")
		values = (str(valor), str(item))
		cursor.execute(sql,values)
		cursor.close()
		db_connection.commit()
		db_connection.close()