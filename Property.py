import random


class Property:
    def __init__(self, name, acronym, price):
        self.name = name
        self.acronym = acronym
        self.price = int(price)
        self.owner = None
        self.is_Mortgaged = False
        self.all_owned = False

    def __repr__(self):
        return self.acronym

    def get_name(self):
        return self.name

    def get_acronym(self):
        return self.acronym

    def get_price(self):
        return self.price

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner


class Location(Property):
    def __init__(self, name, acronym, price, colour_set, rent, one_b_r, two_b_r, three_b_r, four_b_r, hotel_r,
                 house_cost, hotel_cost):
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

    def action(self, player):
        if self.owner is not None:
            if not self.is_Mortgaged:
                player.worth = player.worth - self.rent_amount
                if player.worth < 0:
                    player.is_bankrupt = True
        else:
            yes_no = input(
                "Do you wish to buy " + self.name + "? You have " + player.worth + " in the bank and the property cost" + self.price + "\n(Y/N)")
            if yes_no == "Y":
                player.worth = player.worth - self.price
                player.properties.append(self)
                self.owner = player
                count = 0
                same_colour = []
                for i in player.properties:
                    if i.colour_set == self.colour_set:
                        count = count + 1
                        same_colour.append(self)
                if (not self.colour_set == "Brown" or "Dark Blue") and count == 3:
                    for i in same_colour:
                        i.all_owned = True
                elif (self.colour_set == "Brown" or "Dark Blue") and count == 2:
                    for i in same_colour:
                        i.all_owned = True


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


class Special:
    def __init__(self, name, acronym):
        self.name = name
        self.acronym = acronym

    def __repr__(self):
        return self.acronym


class CommunityChest(Special):
    def __init__(self, name="Community Chest", acronym="CMC"):
        super().__init__(name, acronym)

    def action(self, player):
        print("HELLO")


class Chance(Special):
    def __init__(self, name="Chance", acronym="CHE"):
        super().__init__(name, acronym)

    def action(self, player):
        print("HELLO")


class Go(Special):
    def __init__(self, name="GO", acronym="GO"):
        super().__init__(name, acronym)

    def action(self, player):
        player.worth = player.worth + 200


class FreeSpace(Special):
    def __init__(self, name="Free Space", acronym="FRS"):
        super().__init__(name, acronym)

    def action(self):
        number = random.randint(0, 1000000)
        if number == 696969:
            print("XD FUNNY NUMBER XD")


class Tax(Special):
    def __init__(self, name, acronym, tax_amount):
        super().__init__(name, acronym)
        self.tax_amount = tax_amount

    def action(self, player):
        player.worth = player.worth - self.tax_amount


class Jail(Special):
    def __init__(self, name="Jail/Just Visiting", acronym="JAL"):
        super().__init__(name, acronym)

    def action(self):
        print("lol you get shanked")


class GoToJail(Special):
    def __init__(self, name="Go To Jail", acronym="GTJ"):
        super().__init__(name, acronym)

    def action(self, player):
        player.x = 0
        player.y = 10

