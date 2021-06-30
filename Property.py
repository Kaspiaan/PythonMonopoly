class Property():
    def __init__(self, name, acronym, price):
        self.name = name
        self.acroymn = acronym
        self.price = int(price)
        self.owner = ""
        self.is_Mortgaged = False

    def get_name(self):
        return self.name

    def get_acronym(self):
        return self.acroymn

    def get_price(self):
        return self.price

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner

class Location(Property):
    def __init__(self, name, acronym, price, colour_set, rent, one_b_r, two_b_r, three_b_r, four_b_r, hotel_r, house_cost, hotel_cost):
        super().__init__(name, acronym, price)
        self.colour_set = colour_set
        self.rent_amount = int(rent)
        self.one_building_rent = int(one_b_r)
        self.two_building_rent = int(two_b_r)
        self.three_building_rent = int(three_b_r)
        self.four_building_rent = int(four_b_r)
        self.hotel_rent = int(hotel_r)
        self.house_cost = int(house_cost)
        self.hotel_cost = int(hotel_cost)

class Transport(Property):
    def __init__(self, name, acronym, price, one_o_p, two_o_p, three_o_p, four_o_p):
        super().__init__(name, acronym, price)
        self.one_owned_price = one_o_p
        self.two_owned_price = two_o_p
        self.three_owned_price = three_o_p
        self.four_owned_price = four_o_p

class Utility(Property):
    def __init__(self, name, acronym, price, one_o_m, two_o_m):
        super().__init__(name, acronym, price)
        self.one_owned_multiplier = one_o_m
        self.two_owned_multiplier = two_o_m