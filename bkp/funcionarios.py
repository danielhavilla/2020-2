# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
# Arquivo: funcionarios.py
# Prof. Rafael Maximo
#
# e-mail: 


class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


class Funcionario(Pessoa):

    def __init__(self, nome, idade, email, carga_horaria_semanal):
        super().__init__(nome, idade)
        self.__email = email
        self.carga_horaria = carga_horaria_semanal

        '''
        Construtor da classe Funcionário - lembre-se de usar o super para acessar o construtor
        da classe mãe e criar atributos que já estão definidos lá.
        '''


    @property
    def carga_horaria(self):
        '''
        Retorna a carga horária de trabalho do funcionário
        '''
        return self.__carga_horaria_semanal


    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, de acordo com o cargo, levanta um ValueError
        - Este método não possui retorno;
        '''
        if isinstance(nova_carga_horaria, int):
          if nova_carga_horaria < 20 or nova_carga_horaria > 40:
            raise ValueError 
          self.__carga_horaria_semanal = nova_carga_horaria
        else:
          raise ValueError


    def aumenta_salario(self):
        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        - Este método não possui retorno;
        '''
        raise NotImplementedError


'''
DICAS:

Se uma classe não possui um método definido, mas este método é definido em
alguma classe mãe acima, a classe irá herdar e usar tal método exatamente como
ele está definido na classe acima.

Isto também se aplica ao construtor, se Programador não define um __init__, então
esta classe está automaticamente usando o __init__ da classe Funcionário (se
funcionário tampouco definisse um __init__, então seria usado o de Pessoa, e se
pessoa tampouco o fizesse, seria usado o de `object`, que é a classe base do Python
usada automaticamente para todos as classes que criamos).

Caso você queira ou precise adicionar atributos extras na classe Programador
(ou qualquer outra classe filha de Funcionário), defina o método construtor,
faça a utilização do super e adicione os atributos extra que serão específicos
daquela classe, sejam eles recebidos por parâmetros ou não.

Lembrando sempre que o enunciado define quais são os parâmetros obrigatórios
de uma classe, então se forem criados parâmetros obrigatórios extras, isso
irá gerar erros nos testes de correção.
'''


class Programador(Funcionario):
    '''
    Funcionário do tipo Programador:
    - salario base por hora 35.00;
    - regime de trabalho entre 20h e 40h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal através do número de horas
      trabalhadas na semana e o sálario base (por hora) e considere que o mês
      possui sempre 4.5 semanas.
    '''
    def __init__(self, nome, idade, email, carga_horaria):
      super().__init__(nome, idade, email, carga_horaria)
      self.carga_horaria = carga_horaria
      self.salario_hora = 35
      self.salario_mensal = (self.salario_hora * self.carga_horaria) * 4.5


    def calcula_salario(self):
      
      '''
      Calcula e retorna o salário do mês para o funcionário
      '''
      if self.carga_horaria >= 20 or self.carga_horaria <= 40:
        salario_mensal = (self.salario_hora * self.carga_horaria) * 4.5
        return salario_mensal
      else:
        raise ValueError

    def aumenta_salario(self):

      '''
      Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
      - Este método não possui retorno;
      '''
      self.salario_hora = (self.salario_hora * 0.05) + self.salario_hora


class Estagiario(Funcionario):
    '''
    Funcionário do tipo Estagiario:
    - salario base por hora 15.50;
    - auxilio alimentação fixo de 250 reais por mês;
    - regime de trabalho deve estar entre 16h e 30h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal através do número de horas
      trabalhadas na semana e o sálario base (por hora) e considere que o mês
      possui sempre 4.5 semanas, e por fim calcule e adicione os auxílios.
    '''
    def __init__(self, nome, idade, email, carga_horaria):
      super().__init__(nome, idade, email, carga_horaria)
      self.carga_horaria = carga_horaria
      self.salario = 15.50
      self.auxilio = 250


    def calcula_salario(self):
      '''
      Calcula e retorna o salário do mês para o funcionário
      '''
      return ((self.salario * self.carga_horaria) * 4.5 + self.auxilio)


    def aumenta_salario(self):

      '''
      Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
      - Este método não possui retorno;
      '''
      aumento = self.salario * 1.05
      self.salario = aumento


    @property
    def carga_horaria(self):
        '''
        Retorna a carga horária de trabalho do funcionário
        '''
        return self.__carga_horaria_semanal


    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, de acordo com o cargo, levanta um ValueError
        - Este método não possui retorno;
        '''
        if isinstance(nova_carga_horaria, int):
          if nova_carga_horaria < 16 or nova_carga_horaria > 30:
            raise ValueError 
          self.__carga_horaria_semanal = nova_carga_horaria
        else:
          raise ValueError


class Vendedor(Funcionario):
    '''
    Funcionário do tipo Vendedor:
    - salario base por hora 30.00;
    - auxilio alimentação fixo de 350 reais por mês;
    - auxilio transporte de 30 reais por visita realizada ao cliente;
    - regime de trabalho deve estar entre 15h e 45h semanais, caso contrário
      levanta um ValueError;
    - possui um atributo privado que guarda o número de visitas realizadas no mês,
      começando sempre em zero;
    - cálculo do sálario mensal: calcule o pagamento semanal através do número de horas
      trabalhadas na semana e o sálario base (por hora) e considere que o mês
      possui sempre 4.5 semanas, e por fim calcule e adicione os auxílios;
    - além dos métodos de Funcionário, deve implementar os métodos:
      * realizar_visita; e
      * zerar_visitas.
    '''

    def __init__(self, nome, idade, email, carga_horaria):
      self.num_visitas = 0
      self.transporte = 30
      self.salario = 30
      self.alimentacao = 350
      super().__init__(nome, idade, email, carga_horaria)


    def calcula_salario(self):
      '''
      Calcula e retorna o salário do mês para o funcionário
      '''
      transporte = self.transporte * self.num_visitas
      salario_mensal1 = (self.salario * self.carga_horaria) * 4.5
      salario_mensal2 = transporte + self.alimentacao + salario_mensal1
      return salario_mensal2


    @property
    def carga_horaria(self):

        '''
        Retorna a carga horária de trabalho do funcionário
        '''
        return self.__carga_horaria_semanal


    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):

        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, de acordo com o cargo, levanta um ValueError
        - Este método não possui retorno;
        '''
        if isinstance(nova_carga_horaria, int):
          if nova_carga_horaria < 15 or nova_carga_horaria > 45:
            raise ValueError 
          self.__carga_horaria_semanal = nova_carga_horaria
        else:
          raise ValueError

    @property
    def visitas(self):
        """
        Retorna o número de visitas realizadas pelo vendedor até o momento
        """
        return self.num_visitas

    def realizar_visita(self, n_visitas):
        '''
        Recebe um número inteiro e incrementa o número de visitas realizadas no mês
        com o valor recebido. Antes de fazer a alteração, verifique:
        * se n_visitas é um número inteiro e levante um TypeError caso contrário;
        * se n_visitas é positivo e maior que zero, levantando um ValueError caso contrário.

        - Este método não possui retorno;
        '''
        if isinstance (n_visitas, int):
          if n_visitas > 0:
            self.num_visitas += n_visitas
          else:
             raise ValueError
        else:
           raise TypeError

    def zerar_visitas(self):
        '''
        Quando chamado deve redefinir o número de visitas realizadas pelo vendedor para zero,
        de modo a começar a contagem para o mês seguinte.
        - Este método não possui retorno;
        '''
        self.num_visitas = 0

    def aumenta_salario(self):

        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        - Este método não possui retorno;
        '''
        aumento = self.salario * 1.05
        self.salario = aumento
        
