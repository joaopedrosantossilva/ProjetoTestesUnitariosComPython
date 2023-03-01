from src.models.restaurant import Restaurant

class TestRestaurant:

    def test_describe_restaurant(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        msg = "Esse restaturante chama JP Bar e serve Bar. \n" \
              "Esse restaturante está servindo 0 consumidores desde que está aberto."
        # CHAMADA
        result = restaurant.describe_restaurant()

        # AVALIACAO
        assert msg == result

    def test_open_restaurant(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        msg = "O JP Bar agora está aberto!"

        # CHAMADA
        result = restaurant.open_restaurant()

        # AVALIACAO
        assert msg == result

    def test_already_open_restaurant(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        msg = "O JP Bar já está aberto!"
        restaurant.open_restaurant()

        # CHAMADA
        result = restaurant.open_restaurant()

        # AVALIACAO
        assert msg == result

    def test_close_restaurant(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        msg = "O JP Bar agora está fechado!"
        restaurant.open_restaurant()

        # CHAMADA
        result = restaurant.close_restaurant()

        # AVALIACAO
        assert msg == result

    def test_already_close_restaurant(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        msg = "O JP Bar já está fechado!"

        # CHAMADA
        result = restaurant.close_restaurant()

        # AVALIACAO
        assert msg == result

    def test_set_number_served_with_value_valid(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        value = 3
        restaurant.open_restaurant()
        msg = "Valor registrado com sucesso."

        # CHAMADA
        result = restaurant.set_number_served(value)

        # AVALIACAO
        assert msg == result

    def test_set_number_served_with_value_negative(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        value = -3
        restaurant.open_restaurant()
        msg = "O número informado não pode ser menor que zero ou diferente de inteiro"

        # CHAMADA
        result = restaurant.set_number_served(value)

        # AVALIACAO
        assert msg == result

    def test_set_number_served_with_value_str(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        value = "teste"
        restaurant.open_restaurant()
        msg = "O número informado não pode ser menor que zero ou diferente de inteiro"

        # CHAMADA
        result = restaurant.set_number_served(value)

        # AVALIACAO
        assert msg == result

    def test_set_number_served_with_restaurant_closed(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        value = 3
        msg = "O JP Bar está fechado!"

        # CHAMADA
        result = restaurant.set_number_served(value)

        # AVALIACAO
        assert msg == result

    def test_increment_number_served_with_value_valid(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        initial_value = 5
        added_value = 15
        restaurant.open_restaurant()
        restaurant.set_number_served(initial_value)
        msg = "Valor adicionado com sucesso. O total atual é de: 20"

        # CHAMADA
        result = restaurant.increment_number_served(added_value)

        # AVALIACAO
        assert msg == result

    def test_increment_number_served_with_value_negative(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        initial_value = 4
        added_value = -4
        restaurant.open_restaurant()
        restaurant.increment_number_served(initial_value)
        msg = "O número informado não pode ser menor que zero ou diferente de inteiro"

        # CHAMADA
        result = restaurant.increment_number_served(added_value)

        # AVALIACAO
        assert msg == result

    def test_increment_number_served_with_restaurant_closed(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        value = 3
        msg = "O JP Bar está fechado!"

        # CHAMADA
        result = restaurant.increment_number_served(value)

        # AVALIACAO
        assert msg == result

    def test_increment_number_served_with_value_str(self):
        # SETUP
        restaurant = Restaurant("JP Bar", "Bar")
        initial_value = 4
        added_value = "teste"
        restaurant.open_restaurant()
        restaurant.increment_number_served(initial_value)
        msg = "O número informado não pode ser menor que zero ou diferente de inteiro"

        # CHAMADA
        result = restaurant.increment_number_served(added_value)

        # AVALIACAO
        assert msg == result

    def test_get_restaurant_name(self):
        # SETUP
        name = "JP Bar"
        cuisine_type = "Bar"
        restaurant = Restaurant(name, cuisine_type)


        # CHAMADA
        result = restaurant.get_restaurant_name()

        # AVALIACAO
        assert name == result

    def test_get_cuisine_type(self):
        # SETUP
        name = "JP Bar"
        cuisine_type = "Bar"
        restaurant = Restaurant(name, cuisine_type)

        # CHAMADA
        result = restaurant.get_cuisine_type()

        # AVALIACAO
        assert cuisine_type == result

    def test_get_number_served(self):
        # SETUP
        name = "JP Bar"
        cuisine_type = "Bar"
        restaurant = Restaurant(name, cuisine_type)
        number = 20
        restaurant.open_restaurant()
        restaurant.set_number_served(number)

        # CHAMADA
        result = restaurant.get_number_served()

        # AVALIACAO
        assert number == result

    def test_get_open(self):
        # SETUP
        name = "JP Bar"
        cuisine_type = "Bar"
        restaurant = Restaurant(name, cuisine_type)
        restaurant.open_restaurant()

        # CHAMADA
        result = restaurant.get_open()

        # AVALIACAO
        assert True == result

    def test_is_number_int_and_greater_than_zero_with_value_valid(self):
        # SETUP
        name = "JP Bar"
        cuisine_type = "Bar"
        restaurant = Restaurant(name, cuisine_type)
        value = 2

        # CHAMADA
        result = restaurant.is_number_int_and_greater_than_zero(value)

        # AVALIACAO
        assert True == result

    def test_is_number_int_and_greater_than_zero_with_value_negative(self):
        # SETUP
        name = "JP Bar"
        cuisine_type = "Bar"
        restaurant = Restaurant(name, cuisine_type)
        value = -1

        # CHAMADA
        result = restaurant.is_number_int_and_greater_than_zero(value)

        # AVALIACAO
        assert False == result

    def test_is_number_int_and_greater_than_zero_with_value_str(self):
        # SETUP
        name = "JP Bar"
        cuisine_type = "Bar"
        restaurant = Restaurant(name, cuisine_type)
        value = "Test"

        # CHAMADA
        result = restaurant.is_number_int_and_greater_than_zero(value)

        # AVALIACAO
        assert False == result



