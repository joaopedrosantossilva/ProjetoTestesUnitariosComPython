from src.models.ice_cream_stand import IceCreamStand

class TestIceCreamStand:

    def test_flavors_available_with_stock(self):
        # SETUP
        nome = "Sorvete do Ze"
        cuisine_type = "Sorveteria"
        flavors = ['Chocolate', "Flocos"]
        iceCreamStand = IceCreamStand(nome, cuisine_type, flavors)

        # CHAMADA
        result = iceCreamStand.flavors_available()

        # AVALIACAO
        assert flavors == result
    def test_flavors_available_out_of_stock(self):
        # SETUP
        nome = "Sorvete do Ze"
        cuisine_type = "Sorveteria"
        flavors = []
        iceCreamStand = IceCreamStand(nome, cuisine_type, flavors)
        msg = 'Estamos sem estoque atualmente!'

        # CHAMADA
        result = iceCreamStand.flavors_available()

        # AVALIACAO
        assert msg == result
    def test_find_flavor_out_of_stock(self):
        # SETUP
        nome = "Sorvete do Ze"
        cuisine_type = "Sorveteria"
        flavors = []
        iceCreamStand = IceCreamStand(nome, cuisine_type, flavors)
        msg = 'Estamos sem estoque atualmente!'

        # CHAMADA
        result = iceCreamStand.find_flavor('Chocolate')

        # AVALIACAO
        assert msg == result
    def test_find_flavor_ok(self):
        # SETUP
        nome = "Sorvete do Ze"
        cuisine_type = "Sorveteria"
        flavors = ['Chocolate', "Flocos"]
        iceCreamStand = IceCreamStand(nome, cuisine_type, flavors)
        msg = 'Temos no momento Chocolate!'

        # CHAMADA
        result = iceCreamStand.find_flavor('Chocolate')

        # AVALIACAO
        assert msg == result
        # SETUP
        nome = "Sorvete do Ze"
        cuisine_type = "Sorveteria"
        flavors = ['Chocolate', "Flocos"]
        iceCreamStand = IceCreamStand(nome, cuisine_type, flavors)
        msg = 'Não temos no momento Limão!'

        # CHAMADA
        result = iceCreamStand.find_flavor('Limão')

        # AVALIACAO
        assert msg == result
    def test_add_flavor_out_of_stock(self):
        # SETUP
        nome = "Sorvete do Ze"
        cuisine_type = "Sorveteria"
        flavors = []
        iceCreamStand = IceCreamStand(nome, cuisine_type, flavors)
        msg = 'Estamos sem estoque atualmente!'

        # CHAMADA
        result = iceCreamStand.add_flavor('Limão')

        # AVALIACAO
        assert msg == result
    def test_add_flavor_already_available(self):
        # SETUP
        nome = "Sorvete do Ze"
        cuisine_type = "Sorveteria"
        flavors = ['Chocolate', "Flocos"]
        iceCreamStand = IceCreamStand(nome, cuisine_type, flavors)
        msg = 'Sabor já disponivel!'

        # CHAMADA
        result = iceCreamStand.add_flavor('Chocolate')

        # AVALIACAO
        assert msg == result
    def test_add_flavor_ok(self):
        # SETUP
        nome = "Sorvete do Ze"
        cuisine_type = "Sorveteria"
        flavors = ['Chocolate', "Flocos"]
        iceCreamStand = IceCreamStand(nome, cuisine_type, flavors)
        msg = 'Limão adicionado ao estoque!'
        new_flavor = 'Limão'

        # CHAMADA
        result = iceCreamStand.add_flavor(new_flavor)

        # AVALIACAO
        assert msg == result


