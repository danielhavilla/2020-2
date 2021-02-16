# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: conta.py
# Prof. Rafael Maximo
#
# Email Impacta: daniel.avilla@aluno.faculdadeimpacta.com.br

class Conta:
   
    def __init__(self, clientes, numero, saldo):
               
        # ------------------------------ #
        # -- Atributos Privados Conta -- #
        # ------------------------------ #
        self._clientes  = clientes
        self._numero = numero
        self._saldo = saldo
        self.extrato = []
        self.extrato.append(('saldo inicial', saldo))
                    
    @property
    def clientes(self):
        return self._clientes        

    @property
    def numero(self):
        return self._numero        

    @property
    def saldo(self):
        return self._saldo   
   
    def sacar(self, saque):
        if saque > self._saldo:
            raise ValueError            
        else:
            self._saldo = self._saldo - saque
            self.extrato.append(('saque', saque))
                        
    def depositar(self, deposito):
        self._saldo = self._saldo + deposito
        self.extrato.append(('deposito', deposito))
                           
    def tirar_extrato(self):
        return self.extrato
       
         
