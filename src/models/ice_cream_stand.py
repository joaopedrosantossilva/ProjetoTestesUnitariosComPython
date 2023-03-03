from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        # Excluido o print e o for, para retornar a lista de sabores disponiveis
        # Alterado o print do else para retornar a mensagem
        if self.flavors:
            return self.flavors
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        # Ajustado os prints para return
        # Ajustado o valor que estava sendo passado nos returns, pra retornar o nome do valor pesquisado
        if self.flavors:
            if flavor in self.flavors:
                return "Temos no momento {}!".format(flavor)
            else:
                return "Não temos no momento {}!".format(flavor)
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        # Ajustado os prints para return
        if self.flavors:
            if flavor in self.flavors:
                return "Sabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return "{} adicionado ao estoque!".format(flavor)
        else:
            return "Estamos sem estoque atualmente!"
