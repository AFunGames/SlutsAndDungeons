label def_inventory:

    init python:
        # Item object definition
        class Item(object):
            def __init__(self, name, description, price, weight, stack = 1, size = 1):
                self.name = name
                self.description = description
                self.price = price
                self.weight = weight
                self.size = size
                self.stack = stack

        # Item in container definition
        class InvItem(object):
            def __init__(self, item, amount):
                self.item = item
                self.amount = amount

        # Container (backpacks, slots and other stuff)
        class Container(object):
            def __init__(self, slot_max, weight_max):
                self.inventory = []
                self.weight_max = weight_max
                self.slot_max = slot_max
