"""
O padrão de projeto Simple Factory é um padrão de projeto de criação que fornece uma interface para criar objetos em uma
superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. Ele é um dos padrões de projeto
mais simples e mais comumente usados.

As pessoas costumam confundir fábricas simples com fábricas gerais ou com um dos padrões de design criacionais.
Na maioria dos casos, uma fábrica simples é um passo intermediário para introduzir os padrões Método de Fábrica ou Fábrica Abstrata.

Uma fábrica simples é geralmente representada por um único método em uma única classe.
Com o tempo, esse método pode se tornar muito grande, então você pode decidir extrair partes do método para subclasses.
Uma vez que você faça isso várias vezes, pode descobrir que o conjunto se transformou no clássico padrão de método de fábrica.
"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """
    Classe Abstrata representando um animal.
    """

    @abstractmethod
    def do_say(self):
        """
        Método abstrato que define o som que o animal faz.
        """
        pass


class Cachorro(Animal):
    """Uma classe que representa um cachorro."""
    def do_say(self):
        """Exibe na tela o som que um cachorro faz."""
        print("Au-au")


class Gato(Animal):
    """Uma classe que representa um gato."""
    def do_say(self):
        """Exibe na tela o som que um gato faz."""
        print("Miau")


class PetFactory(object):
    """
    Uma classe de fábrica para criar objetos de animais em uma floresta.
    """

    def make_sound(self, object_type: str):
        """
        Cria um objeto de animal do tipo especificado e faz ele emitir seu som.

        Args:
            object_type (str): O tipo de animal a ser criado.

        Returns:
            str: O som emitido pelo animal criado.

        Raises:
            Exception: Se o object_type especificado não for um tipo de animal válido.
        """
        try:
            return eval(object_type.title())().do_say()
        except:
            print("Erro! Animal desconhecido!")


def run() -> None:
    ff = PetFactory()
    animal = input("Qual animal deve emitir som? Cachorro ou Gato?: ")
    ff.make_sound(animal)
