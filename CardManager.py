from Card import Card
import json
import qrcode

class CardManager(object):

    def __init__(self):
        with open('AllCards-x.json', encoding='utf8') as json_data:
            self.cards = json.load(json_data)

    def get_card(self, card_name):
        current = self.cards[card_name.rstrip()]
        card = Card(current['name'], current['colors'], current['text'], current['types'], current['manaCost'], current.get('subtypes'))
        return card

    def _print_cards(self):
        print(json.dumps(self.cards, indent=2))

    def card_to_qr(self, card_name):
        card = self.get_card(card_name)
        qr = qrcode.make(card.name)
        return qr

    def card_to_json(self, card_name):
        card = self.get_card(card_name)
        json_object = {card.name: {"colors": card.colors, "rules": card.rules, "types": card.types, "subtypes": card.subtypes, "cost": card.cost, "pt": card.power_toughness, "loyalty": card.loyalty}}
        return json.dumps(json_object, indent=4)


