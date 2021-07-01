class Player:
    def __init__(self, name):
        self.name = name
        self.worth = 1500
        self.x = 11
        self.y = 11
        self.houses_owned = 0
        self.hotels_owned = 0
        self.get_out_of_jail_cards_owned = 0
        self.is_bankrupt = False
        self.properties = []

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_name(self):
        return self.name

    def buy_house(self, house_price, can_buy):
        if (house_price > self.worth) or not can_buy:
            return False
        else:
            self.worth = self.worth - house_price
            self.houses_owned = self.houses_owned + 1
            return True

    def buy_property(self, property_worth):
        if property_worth > self.worth:
            return False
        else:
            self.worth = self.worth - property_worth
            return True
