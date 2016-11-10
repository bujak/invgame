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
            a=x[0]
            b=x[1]
            c=len(b)-1
            b=b[0:c]
            inventory[a]=int(b)
        #print(inv)

def display_inventory(inventory):
    print('\nInventory:')
    for key, value in inventory.items():
        print(key, ':', inventory[key])
    print('Total items :', sum(inventory.values()))


def add_to_inventory(inventory, loot):
    for item in loot:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item]=1

def export_inventory(inventory, filename):
    with open(filename, 'w') as f:  # Just use 'w' mode in 3.x
        writer = csv.writer(f)
        for row in inventory.items():
            writer.writerow(row)

def print_table(inventory, order=None):
    print("\nzzzzzzzzzInventory: \n----------")
    print("{:<1} {:<40}".format('count','item'))
    if order == 'count,desc':
        for key, value in sorted(inventory.items(), key=lambda x: x[1], reverse=True):
            print("{:<5} {:<40}".format(value, key))
    elif order == 'count,asc':
        for key, value in sorted(inventory.items(), key=lambda x: x[1], reverse=False):
            print("{:<5} {:<40}".format(value, key))
    else:
        for key, value in inventory.items():
            print("{:<5} {:<40}".format(value, key))
    print('Total items :', sum(inventory.values()))

import_inventory(inv,'inventory.csv')

display_inventory(inv)

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'adsa']

add_to_inventory(inv,loot)

display_inventory(inv)

export_inventory(inv, 'inventory.csv')

print_table(inv,'count,desc')
