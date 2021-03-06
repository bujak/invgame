"""
Inventory
Tomasz Bujakowski
Codecool Kraków 2016
"""


import csv

inv = {'rope': 1,
       'torch': 6,
       'gold coin': 42,
       'dagger': 1,
       'arrow': 12}


def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, 'r') as saved_inv:
        for line in saved_inv:
            line = line.split(",")  # putting line from csv file to list
            item = line[0]  #initalizing items in list as variables
            count = line[1]
            count_len = len(count) - 1
            count = count[0:count_len]  #cutting \n from count string
            importing={}
            importing[item] = int(count)  #putting items and count in temporary dict.
            for item in importing:  #adding items to main inventory
                if item not in inventory:
                    inventory[item] = int(count)
                else:
                    inventory[item] += int(count)
        #print(inv) #just for control


# printing unsorted inventory with for loop
def display_inventory(inventory):
    print('\nInventory:')
    for key, value in inventory.items():
        print(key, ':', inventory[key])
    print('Total items :', sum(inventory.values()))


# adding items from loot list to inventory
def add_to_inventory(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


#saving inventory to external file
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


#print inventory, sorted or not, depending on second parameter
def print_table(inventory, order=None):
    print("\nInventory:")
    print("{:>7} {:>12} {:>0}".format('count', 'item name', '\n--------------------'))
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


if __name__ == '__main__':

    import_inventory(inv)

    display_inventory(inv)

    loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    add_to_inventory(inv, loot)

    display_inventory(inv)

    export_inventory(inv, 'rubu')

    print_table(inv)
