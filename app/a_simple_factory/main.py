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

