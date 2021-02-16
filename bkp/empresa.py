# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
# Arquivo: empresa.py
# Prof. Rafael Maximo
#
# e-mail: 

from funcionarios import Programador, Estagiario, Vendedor

class Empresa:
    def __init__(self, nome, cnpj, area_atuacao, equipe):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__area_atuacao = area_atuacao
        self.__equipe = equipe

    def contrata(self, novo_funcionario):
        funcionario = novo_funcionario
        self.__equipe.append(funcionario)

    @property
    def equipe(self):
        return self.__equipe

    def folha_pagamento(self):
        soma = 0
        for x in range (len(self.__equipe)):
            soma = soma + self.__equipe[x].calcula_salario()
        return soma
         
    def dissidio_anual(self):
        for x in range (len(self.__equipe)):
            self.__equipe[x].aumenta_salario()
    
    def listar_visitas(self):
        dic = {}
        for x in range (len(self.__equipe)):
            if isinstance (self.__equipe[x], Vendedor):
                dic [self.__equipe[x].email] = self.__equipe[x].visitas
        return dic
           
    
    def zerar_visitas_vendedores(self):
        for x in range (len(self.__equipe)):
            if isinstance (self.__equipe[x], Vendedor):
                self.__equipe[x].zerar_visitas()
       