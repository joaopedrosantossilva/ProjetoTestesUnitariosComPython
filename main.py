from src.models.restaurant import Restaurant
from src.models.ice_cream_stand import IceCreamStand

ice_cream_stand = IceCreamStand("Soveteria do Ze", "Sorvete", ["Baunilha", "Chocolate"])
print(ice_cream_stand.flavors_available())