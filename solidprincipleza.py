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
        pass


class MeanZa(OperationZa):
    """
    Calcule la moyenne des éléments d'une séquence.
    """

    def do_operation_za(self, list_za):
        LogZa.log_za(f"La moyenne est : {np.mean(list_za)}")


class MaxZa(OperationZa):
    """
    Détermine le maximum parmi les éléments d'une séquence.
    """

    def do_operation_za(self, list_za):
        LogZa.log_za(f"Le maximum est : {np.max(list_za)}")


class MainZa:
    """
    Effectue une opération
    """

    @abstractmethod
    def get_operations_za(self, list_za):
        # __subclasses__ trouvera toutes les enfants d'OperationZa
        for operation in OperationZa.__subclasses__():
            operation.do_operation_za(list_za)

"""
----------------------MAIN------------------
"""
if __name__ == "__main__":
    LogZa.log_za("Mauvaise pratique, parce SRP n'est pas respecté dans la fonction do_math_operations_za")
    do_math_operations_za([3, 5, 11, 7, 1])

    LogZa.log_za("Mauvaise pratique, parce OCP n'est pas respecté dans la fonction main_za")
    main_za([3, 5, 11, 7, 1])

    LogZa.log_za("Mauvaise pratique, parce OCP n'est pas respecté dans la fonction main_za")
    MainZa.get_operations_za([3, 5, 11, 7, 1])
