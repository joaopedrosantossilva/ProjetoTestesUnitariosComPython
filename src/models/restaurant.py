class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        # Melhoria - acrescentado dois undescore no começo dos atributos, para indicar que eles são privados e não podem ser acessados diretamente.
        # Correção no nome do restaurante, qeu estava rebendo title(). Ajustado para receber o valor passado
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type
        self.__number_served = 0
        self.__open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        # Correção 1 - Na primeira variavel passada no print estava self.cuisine_type, ao inves de self_restaurant_name.
        # Correcao 2 - Ajustado o texto para ficar todas as palavras em portugues.
        # Melhoria - Alterado os retornos para retornar uma string,ao invés do print.
        return "Esse restaturante chama {} e serve {}. \n" \
               "Esse restaturante está servindo {} consumidores desde que está aberto.".format(self.__restaurant_name, self.__cuisine_type, self.__number_served)

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        # Correção 1 - self.open = False - estava colocando o valor para False, ao invés de True
        # Correcao 2 - retirado o codigo self.number_served = -2, pois não fazia sentido o number_served esta recebendo -2 aqui, ja que essa função se trata apenas de abrir o restaurante..
        # Melhoria - Alterado os retornos do if e else para retornar uma string,ao invés do print.
        if not self.__open:
            self.__open = True
            return "O {} agora está aberto!".format(self.__restaurant_name)
        else:
            return "O {} já está aberto!".format(self.__restaurant_name)

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        # Correcao - retirado o codigo self.number_served = 0, pois não fazia sentido pra mim o number_served esta recebendo 0 aqui, ja que essa função se trata apenas de fechar o restaurante.
        # Melhoria - Alterado os retornos do if e else para retornar uma string,ao invés do print.
        # Melhoria - Alterado os retornos do if e else para retornar uma string,ao invés do print.
        if self.__open:
            self.__open = False
            return "O {} agora está fechado!".format(self.__restaurant_name)
        else:
            return "O {} já está fechado!".format(self.__restaurant_name)

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        # Melhoria no if, acrescentado num return uma mensagem de que o valor foi adicionado com sucesso.
        # Melhoria - Alterado os retornos do if e else para retornar uma string,ao invés do print.
        if self.is_number_int_and_greater_than_zero(total_customers):
            if self.__open:
                self.__number_served = total_customers
                return "Valor registrado com sucesso."
            else:
                return "O {} está fechado!".format(self.__restaurant_name)
        else:
            return "O número informado não pode ser menor que zero ou diferente de inteiro"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        # Melhoria - Alterado os retornos do if e else para retornar uma string,ao invés do print.
        # Correcao - ajustado o number_served para somar ao valor ja existente. Antes estava substituindo.
        if self.is_number_int_and_greater_than_zero(more_customers):
            if self.__open:
                self.__number_served += more_customers
                return "Valor adicionado com sucesso. O total atual é de: {}".format(self.__number_served)
            else:
                return "O {} está fechado!".format(self.__restaurant_name)
        else:
            return "O número informado não pode ser menor que zero ou diferente de inteiro"

    #Criado funçao para verificar se o número é maior que zero e se o valor passado é do tipo inteiro
    def is_number_int_and_greater_than_zero(self, value):
        if type(value) == int and value > 0:
            return True
        return False

    #Acrescentado as funções de get pare obter os valores de cada atributo.
    def get_restaurant_name(self):
        return self.__restaurant_name
    def get_cuisine_type(self):
        return self.__cuisine_type
    def get_number_served(self):
        return self.__number_served
    def get_open(self):
        return self.__open


