from src.models.restaurant import Restaurant

restaurant = Restaurant("Restaurante do JP", "Fast Food")

print(restaurant.describe_restaurant())
print(restaurant.close_restaurant())
print(restaurant.open_restaurant())
print(restaurant.close_restaurant())
print(f"{restaurant.get_open()}")