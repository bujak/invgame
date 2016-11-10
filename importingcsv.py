import csv

inv = {'rope': 1,
       'torch': 6,
       'gold coin': 42,
       'dagger': 1,
       'arrow': 12}


def import_inventory(inventory, filename):
    with open(filename, 'r') as saved_inv:
        for line in saved_inv:
            x = line.split(",")
            a = x[0]
            b = x[1]
            c = len(b)-1
            b = b[0:c]
            inventory[a] = int(b)
        """print(inv)"""


def display_inventory(inventory):
    print('\nInventory:')
    for key, value in inventory.items():
        print(key, ':', inventory[key])
    print('Total items :', sum(inventory.values()))


def add_to_inventory(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def export_inventory(inventory, filename=None):
    if filename is None:
        with open('export_inventory.csv', 'w') as f:
            writer = csv.writer(f)
            for row in inventory.items():
                writer.writerow(row)
    else:
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for row in inventory.items():
                writer.writerow(row)


def print_table(inventory, order=None):
    print("\nInventory:")
    print("{:>7} {:>12} {:>0}".format('count', 'item name','\n--------------------'))
    if order == 'count,desc':
        for key, value in sorted(inventory.items(), key=lambda x: x[1], reverse=True):
            print("{:>7} {:>12}".format(value, key))
    elif order == 'count,asc':
        for key, value in sorted(inventory.items(), key=lambda x: x[1], reverse=False):
            print("{:>7} {:>12}".format(value, key))
    else:
        for key, value in inventory.items():
            print("{:>7} {:>12}".format(value, key))
    print('--------------------\nTotal items :', sum(inventory.values()))

#
# import_inventory(inv, 'inventory.csv')
#
# display_inventory(inv)
#
# loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#
# add_to_inventory(inv, loot)
#
# display_inventory(inv)
#
# export_inventory(inv, 'rubu')

print_table(inv)
