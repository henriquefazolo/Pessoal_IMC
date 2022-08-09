class Pessoa:

    def __init__(self):
        self.__nome = None
        self.__altura = None
        self.__peso = None
        self.__data_de_nascimento = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento

    def retonar_imc(self):
        imc = self.__peso / (self.__altura ** 2)
        classificacao = ['Baixo peso', 'Peso normal', 'Sobrepeso', 'Pré-obeso', 'Obeso I', 'Obeso II', 'Obeso III']
        risco_cormobidade = ((0, 18.5),
                             (18.5, 25),
                             (25, 30),
                             (30.0, 35),
                             (35, 40),
                             (40, 999)
                             )

        for i in range(len(risco_cormobidade)):
            imc_inicial = risco_cormobidade[i][0]
            imc_final = risco_cormobidade[i][1]

            if imc_inicial <= imc < imc_final:

                return f'{self.__nome}\n' \
                       f'IMC : {imc:.2f}\n' \
                       f'Classificação : {classificacao[i]}\n' \
                       f'Data de nascimento : {self.__data_de_nascimento}' \



pessoa = Pessoa()


pessoa.nome = 'João'
pessoa.peso = 65.5
pessoa.altura = 1.64
pessoa.data_de_nascimento = '01/01/1990'

print(pessoa.retonar_imc())
