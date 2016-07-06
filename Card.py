
class Card(object):

    def __init__(self, name, colors, rules, types, cost, subtypes=None, power_toughness=None, loyalty=None):

        self.name = name
        self.colors = colors
        self.rules = rules
        self.types = types
        self.subtypes = subtypes
        self.cost = cost
        self.power_toughness = power_toughness
        self.loyalty = loyalty

    def __str__(self):
        return '{}: {{ Colors: {}, Rules: {}, Types: {}, Subtypes: {}, Cost: {}, PT: {}, Loyalty: {}}}'.format(
        self.name,
        self.colors,
        self.rules,
        self.types,
        self.subtypes,
        self.cost,
        self.power_toughness,
        self.loyalty)
