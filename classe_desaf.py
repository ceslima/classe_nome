class Pessoa:
    """
    Classe que representa uma pessoa com nome e idade.
    """

    def __init__(self, nome: str, idade: int) -> None:
        """
        Construtor da classe Pessoa.

        Args:
            nome: O nome da pessoa.
            idade: A idade da pessoa.
        """
        self.nome = nome
        self.idade = idade

    def formatar_dados(self) -> str:
        """
        Retorna uma string formatada com os dados da pessoa.

        Returns:
            Uma string formatada com o nome e a idade da pessoa.
        """
        return f"Nome: {self.nome}, Idade: {self.idade}"


# Entrada de dados
nome = input()
idade = int(input())

# Cria uma instância da classe Pessoa
pessoa = Pessoa(nome, idade)

# Chama o método para formatar os dados e imprime o resultado
dados_formatados = pessoa.formatar_dados()
print(dados_formatados)
