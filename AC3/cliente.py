# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: cliente.py
# Prof. Rafael Maximo
#
# Email Impacta: daniel.avilla@aluno.faculdadeimpacta.com.br

class Cliente:
    
    def __init__(self, nome, telefone, email):

        if not isinstance(telefone,int):
            raise TypeError
        
        if not isinstance(email,str):
            raise TypeError
        
        if '@' not in email:  
            raise ValueError
    
        # ------------------------------ #
        # -- Atributos Privados Cliente- #
        # ------------------------------ #
        self._nome = nome
        self._telefone = telefone
        self._email = email

    @property
    def nome(self):        
        return self._nome
        
    @property
    def telefone(self): 
        return self._telefone
        
    @telefone.setter
    def telefone(self, novo_telefone):
        if not isinstance(novo_telefone,int):
            raise TypeError    
        self._telefone = novo_telefone
        
    @property
    def email(self):        
        return self._email      

    @email.setter
    def email(self, novo_email):
        if not isinstance(novo_email,str):
            raise TypeError
        if '@' not in novo_email:  
            raise ValueError
        self._email = novo_email
        
