"""
solidprincipleza illustre comment appliquer les meilleures pratiques de conception suivantes :
- SRP : The Single-Responsibility Principle - le principe de responsabilité unique
- OCP : The Open-Closed Principle - Le principe de l'ouverture et de la fermeture
- LSP : The Liskov Substitution Principle - le principe de substitution de Liskov
- ISP : The Interface Segregation Principle - Le principe de ségrégation d'interface
- DiP : The Dependency inversion Principle - Le principe d'inversion de dépendance
"""
from logza import LogZa
import numpy as np
from abc import ABC, abstractmethod

"""
------------------------SOLID blessé--------------------------
"""


def do_math_operations_za(list_za: list) -> None:
    """
    Fonction responsable de calculer la moyenne et le maximum.
    Mauvaise pratique, parce qu'elle ne respecte pas SRP.
    """
    LogZa.log_za("do_math_operations_za calcule la moyenne")
    LogZa.log_za(f"La moyenne est : {np.mean(list_za)}")
    LogZa.log_za("do_math_operations_za calcule le maximum")
    LogZa.log_za(f"Le maximum est : {np.max(list_za)}")


"""
---------------SRP respecté et OCP blessé------------------------
"""


def get_mean_za(list_za: list):
    LogZa.log_za("get_mean_za calcule la moyenne")
    LogZa.log_za(f"La moyenne est : {np.mean(list_za)}")


def get_max_za(list_za: list):
    LogZa.log_za("get_max_za calcule le maximum")
    LogZa.log_za(f"Le maximum est : {np.max(list_za)}")


def main_za(list_za: list):
    LogZa.log_za("main_za calcule la moyenne")
    get_mean_za(list_za)
    LogZa.log_za("main_za calcule la moyenne")
    get_max_za(list_za)


"""
--------------------------SRP + OCP--------------------------
"""


class OperationZa(ABC):
    """
    OperationZa vous donne des recettes d'opérations
    """

    @abstractmethod
    def do_operation_za(self):
        """
        Implémenter ceci pour effectuer un calcul mathématique.
        """
        raise NotImplementedError("Vous devriez implémenter cette méthode pour effectuer un calcul mathématique.")


class MeanZa(OperationZa):
    """
    Calcule la moyenne des éléments d'une séquence.
    """

    def __init__(self):
        LogZa.log_za(f"Constructeur de MeanZa")

    def do_operation_za(self, list_za: list):
        LogZa.log_za(f"La moyenne est : {np.mean(list_za)}")


class MaxZa(OperationZa):
    """
    Détermine le maximum parmi les éléments d'une séquence.
    """

    def __init__(self):
        LogZa.log_za(f"Constructeur de MaxZa")

    def do_operation_za(self, list_za: list):
        LogZa.log_za(f"Le maximum est : {np.max(list_za)}")

class MedianZa(OperationZa):
    """
    Détermine le médiane parmi les éléments d'une séquence.
    """

    def __init__(self):
        LogZa.log_za(f"Constructeur de MedianZa")

    def do_operation_za(self, list_za: list):
        LogZa.log_za(f"La médiane est : {np.median(list_za)}")


class MainZa:
    """
    Effectue une opération
    """

    @abstractmethod
    def get_operations_za(self, list_za: list):
        LogZa.log_za(f"La sous-classes :{OperationZa.__subclasses__()}")
        # La sous-classes :[<class '__main__.MeanZa'>, <class '__main__.MaxZa'>]
        for operation_za in OperationZa.__subclasses__():
            LogZa.log_za(f"La classe :{operation_za}")
            # La classe :<class '__main__.MeanZa'>
            # La classe :<class '__main__.MaxZa'>
            LogZa.log_za(f"L'object :{operation_za()}")
            # L'object :<__main__.MeanZa object at 0x00000196073B7520>
            # L'object :<__main__.MaxZa object at 0x00000196073B7520>
            operation_za().do_operation_za(list_za)

    @abstractmethod
    def get_one_operation_za(self, list_za: list, operation_za: OperationZa):
        if OperationZa.__subclasscheck__(operation_za):
            operation_za().do_operation_za(list_za)


"""
----------------------MAIN------------------
"""
if __name__ == "__main__":
    print()
    LogZa.log_za("Mauvaise pratique, parce SRP n'est pas respecté dans la fonction do_math_operations_za")
    do_math_operations_za([3, 5, 11, 7, 1])

    print()
    LogZa.log_za("Mauvaise pratique, parce OCP n'est pas respecté dans la fonction main_za")
    main_za([3, 5, 11, 7, 1])

    print()
    LogZa.log_za("Mauvaise pratique, parce OCP n'est pas respecté dans la fonction main_za")
    main_za = MainZa()
    print("--------Effectuer toutes opérations------------")
    main_za.get_operations_za([3, 5, 11, 7, 1])
    print("--------Effectuer une opération spécifique------------")
    main_za.get_one_operation_za([3, 5, 11, 7, 1], MeanZa)
    print("+++++Extension de OperationZa, avec le calcul de la médiane, sans necessité de modifier un partie du code déjà implémenté+++++++++")
    main_za.get_one_operation_za([3, 5, 11, 7, 1], MedianZa)
