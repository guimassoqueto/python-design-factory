"""
O padrão de Factory Method é um padrão de projeto de criação que fornece uma interface para criar objetos em uma superclasse,
mas permite que as subclasses alterem o tipo de objetos que serão criados.
"""


from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):
    """
    Classe Abstrata representando uma seção de um documento.
    """

    @abstractmethod
    def descreve(self):
        """
        Método abstrato que descreve a seção do documento.
        """
        pass


#################################### Concrete Product ####################################

class SecaoPessoal(Secao):
    """Uma classe que representa uma seção pessoal de um documento."""
    def descreve(self):
        """Exibe na tela a descrição de uma seção pessoal."""
        print("Seção Pessoal")


class SecaoAlbum(Secao):
    """Uma classe que representa uma seção de álbum de fotos de um documento."""
    def descreve(self):
        """Exibe na tela a descrição de uma seção de álbum de fotos."""
        print("Seção Album")


class SecaoPatente(Secao):
    """Uma classe que representa uma seção de patente de um documento."""
    def descreve(self):
        """Exibe na tela a descrição de uma seção de patente."""
        print("Seção Patente")


class SecaoPublicacao(Secao):
    """Uma classe que representa uma seção de publicação de um documento."""
    def descreve(self):
        """Exibe na tela a descrição de uma seção de publicação."""
        print("Seção Publicação")


class Perfil(metaclass=ABCMeta):
    """
    Classe Abstrata representando um perfil de uma rede social.
    """

    def __init__(self):
        self.secoes = []
        self.cria_perfil()

    @abstractmethod
    def cria_perfil(self):
        """
        Método abstrato que cria um perfil de uma rede social.
        """
        pass

    def get_secoes(self):
        """
        Método que retorna as seções de um perfil de uma rede social.
        """
        return self.secoes

    def add_secao(self, secao):
        """
        Método que adiciona uma seção a um perfil de um documento.
        """
        self.secoes.append(secao)



#################################### Concrete Creator ####################################

class Linkedin(Perfil):
    """Uma classe que representa um perfil do LinkedIn."""
    def cria_perfil(self):
        """Cria um perfil do LinkedIn."""
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoPatente())
        self.add_secao(SecaoPublicacao())


class Facebook(Perfil):
    """Uma classe que representa um perfil do Facebook."""
    def cria_perfil(self):
        """Cria um perfil do Facebook."""
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoAlbum())


#################################### Cliente ####################################

def run():
    """
    Executa o exemplo do padrão Factory Method.

    Esta função solicita ao usuário que digite o tipo de perfil que deseja criar (Facebook ou LinkedIn).
    Em seguida, cria uma instância do tipo de perfil selecionado usando o padrão Factory Method.
    Por fim, imprime o tipo de perfil sendo criado e as seções do perfil.
    """
    tipo_perfil = input("Qual perfil deseja criar? [Facebook ou LinkedIn]: ")
    perfil = eval(tipo_perfil.title())()
    print("Criando perfil... ", type(perfil).__name__)
    print("Seções do perfil: ", perfil.get_secoes())