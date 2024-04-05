"""
O padrão de projeto Abstract Factory, em design de software, é um padrão criacional que
fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar
suas classes concretas. Esse padrão é fundamentalmente sobre criar fábricas de fábricas; ou seja,
uma fábrica abstrata define uma interface para criar várias fábricas, cada uma capaz de criar diferentes
objetos dentro de uma família de produtos.

A ideia principal é isolar a criação dos objetos da sua utilização, permitindo que sistemas sejam configurados
com múltiplas famílias de produtos, sem a necessidade de modificar o código que utiliza os produtos.
Isso é particularmente útil para bibliotecas e frameworks onde os detalhes de implementação dos objetos
criados não devem ser expostos ao código cliente.

O padrão Abstract Factory permite que um sistema seja independente de como seus produtos são criados,
compostos e representados. Ele promove a consistência entre produtos, já que todos os objetos de uma
família são garantidos para trabalhar juntos. É especialmente útil em casos onde um sistema deve ser
configurado com uma entre várias famílias de produtos, fornecendo uma maneira de configurar o sistema
com a família apropriada.
"""


from  abc import ABCMeta, abstractmethod


#################################### FACTORIES ####################################

class PizzaFactory(metaclass=ABCMeta):
    """Classe abstrata para a fábrica de pizzas."""

    @abstractmethod
    def cria_pizza_vegana(self):
        """Cria uma pizza vegana.

        Retorna uma instância de uma pizza vegana.
        """
        pass

    @abstractmethod
    def cria_pizza_tradicional(self):
        """Cria uma pizza tradicional.

        Retorna uma instância de uma pizza tradicional.
        """
        pass


class IndianaPizzaFactory(PizzaFactory):
    """Uma fábrica de pizzas de indianas que implementa a interface PizzaFactory."""

    def cria_pizza_vegana(self):
        """Cria uma pizza vegana luxuosa.

        Returns:
            PizzaVeganaLuxuosa: Uma instância da classe PizzaVeganaLuxuosa.
        """
        return PizzaVeganaLuxuosa()

    def cria_pizza_tradicional(self):
        """Cria uma pizza tradicional de frango.

        Returns:
            PizzaFrango: Uma instância da classe PizzaFrango.
        """
        return PizzaFrango()


class AmericanaPizzaFactory(PizzaFactory):
    """Uma fábrica de pizzas de americanas que implementa a interface PizzaFactory."""

    def cria_pizza_vegana(self):
        """Cria uma pizza vegana no estilo americano."""
        return PizzaVeganaMexicana()

    def cria_pizza_tradicional(self):
        """Cria uma pizza tradicional no estilo americano."""
        return PizzaCalabresa()


#################################### PRODUCTS ####################################

class PizzaVegana(metaclass=ABCMeta):
    """
    Classe abstrata que representa uma pizza vegana.

    Métodos abstratos:
    - prepara(): Prepara a pizza vegana.
    """
    @abstractmethod
    def prepara(self):
        """
        Método abstrato que define como a pizza vegana é preparada.
        """
        pass


class PizzaTradicional(metaclass=ABCMeta):
    """
    Classe abstrata que representa uma pizza tradicional.
    """

    @abstractmethod
    def prepara(self):
        """
        Método abstrato que define a preparação da pizza tradicional.
        """
        pass


class PizzaVeganaLuxuosa(PizzaVegana):
    """
    Representa uma pizza vegana luxuosa.

    Esta classe herda da classe PizzaVegana e define o comportamento específico
    para a preparação de uma pizza vegana luxuosa.
    """

    def prepara(self):
        """
        Prepara a pizza vegana luxuosa.
        """
        print("Preparando pizza vegana luxuosa...")


class PizzaVeganaMexicana(PizzaVegana):
    """
    Representa uma pizza vegana mexicana.

    Esta classe herda da classe PizzaVegana e define o comportamento específico
    para a preparação de uma pizza vegana mexicana.
    """
    def prepara(self):
        """
        Prepara a pizza vegana mexicana.
        """
        print("Preparando pizza vegana mexicana...")


class PizzaFrango(PizzaTradicional):
    """
    Representa uma pizza vegana mexicana.

    Esta classe herda da classe PizzaTradicional e define o comportamento específico
    para a preparação de uma pizza de frango.
    """
    def prepara(self):
        """
        Prepara a pizza vegana de frango.
        """
        print("Preparando pizza de frango...")


class PizzaCalabresa(PizzaTradicional):
    """
    Representa uma pizza vegana mexicana.

    Esta classe herda da classe PizzaTradicional e define o comportamento específico
    para a preparação de uma pizza de frango.
    """
    def prepara(self):
        """
        Prepara a pizza vegana de calabresa.
        """
        print("Preparando pizza de calabresa...")


#################################### CLIENTE ####################################

class Pizzaria:
    """
    Classe que representa uma pizzaria.

    Métodos:
        faz_pizzas: Cria e prepara pizzas veganas e tradicionais usando fábricas específicas.
    """
    def __init__(self):
        pass

    def faz_pizzas(self):
        """
        Cria e prepara pizzas veganas e tradicionais usando fábricas específicas.
        """
        for fabrica in (IndianaPizzaFactory(), AmericanaPizzaFactory()):
            pizza_vegana = fabrica.cria_pizza_vegana()
            pizza_vegana.prepara()

            pizza_tradicional = fabrica.cria_pizza_tradicional()
            pizza_tradicional.prepara()


def run():
    pizzaria = Pizzaria()
    pizzaria.faz_pizzas()