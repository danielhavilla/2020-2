# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: banco.py
# Prof. Rafael Maximo
#
# Email Impacta: daniel.avilla@aluno.faculdadeimpacta.com.br

from conta import Conta

class Banco:   
    
    def __init__(self, nome):
        # ------------------------------ #
        # -- Atributos Privados Banco--- #
        # ------------------------------ #
        self._nome = nome
        self._contas = []       

    @property
    def nome(self):
        return self._nome
        
    @property
    def contas(self): 
        return self._contas
       
    def abre_conta(self, clientes, saldo):       
        if saldo < 0:           
            raise ValueError        
        try:
            numero = self._contas[-1].numero + 1
        except IndexError:
            numero = 1
        finally:
            c1 = Conta(clientes, numero, saldo)       
            self._contas.append(c1)
           
  
