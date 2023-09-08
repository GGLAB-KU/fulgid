# Initial state of boxes
boxes = {
    0: ['pants'],
    1: ['umbrella'],
    2: ['makeup', 'pan', 'shampoo', 'headphone', 'belt'],
    3: ['snow', 'phone', 'key', 'telescope'],
    4: [],
    5: ['moon'],
    6: ['train'],
    7: ['vase', 'basket', 'console', 'grass', 'sock'],
    8: ['blender', 'towel', 'storm'],
    9: ['rain', 'jacket'],
    10: ['comet'],
    11: ['swimsuit', 'piano', 'microscope', 'mirror'],
    12: ['scarf', 'violin', 'plane', 'wig'],
    13: ['cloud', 'perfume', 'shoes'],
    14: ['controller', 'rock', 'river']
}

# Replace the comet with the car in Box 10.
boxes[10].remove('comet')
boxes[10].append('car')

# Swap the pants in Box 0 with the cloud in Box 13.
boxes[0].remove('pants')
boxes[13].remove('cloud')
boxes[0].append('cloud')
boxes[13].append('pants')

# Replace the console and the grass with the clock and the perfume in Box 7.
boxes[7].remove('console')
boxes[7].remove('grass')
boxes[7].append('clock')
boxes[7].append('perfume')

# Put the soap into Box 5.
boxes[5].append('soap')

# Put the shampoo and the needle into Box 1.
boxes[1].append('shampoo')
boxes[1].append('needle')

# Swap the train in Box 6 with the soap in Box 5.
boxes[6].remove('train')
boxes[5].remove('soap')
boxes[6].append('soap')
boxes[5].append('train')

# Remove the shampoo and the umbrella from Box 1.
boxes[1].remove('shampoo')
boxes[1].remove('umbrella')

# Put the glove and the shark into Box 4.
boxes[4].append('glove')
boxes[4].append('shark')

# Move the storm and the towel and the blender from Box 8 to Box 3.
items_to_move = ['storm', 'towel', 'blender']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Remove the cloud from Box 0.
boxes[0].remove('cloud')

# Replace the violin and the plane with the plate and the helmet in Box 12.
boxes[12].remove('violin')
boxes[12].remove('plane')
boxes[12].append('plate')
boxes[12].append('helmet')

# Put the plate into Box 9.
boxes[9].append('plate')

# Move the snow and the key and the blender from Box 3 to Box 0.
items_to_move = ['snow', 'key', 'blender']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Move the train and the moon from Box 5 to Box 8.
items_to_move = ['train', 'moon']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[8].append(item)

# Replace the vase and the basket and the clock with the toaster and the cloud and the starfish in Box 7.
boxes[7].remove('vase')
boxes[7].remove('basket')
boxes[7].remove('clock')
boxes[7].append('toaster')
boxes[7].append('cloud')
boxes[7].append('starfish')

# Move the car from Box 10 to Box 12.
boxes[10].remove('car')
boxes[12].append('car')

# Replace the moon and the train with the boot and the oven in Box 8.
boxes[8].remove('moon')
boxes[8].remove('train')
boxes[8].append('boot')
boxes[8].append('oven')

# Remove the pants and the shoes from Box 13.
boxes[13].remove('pants')
boxes[13].remove('shoes')

# Replace the microscope and the mirror with the table and the sandals in Box 11.
boxes[11].remove('microscope')
boxes[11].remove('mirror')
boxes[11].append('table')
boxes[11].append('sandals')

# Swap the table in Box 11 with the rain in Box 9.
boxes[11].remove('table')
boxes[9].remove('rain')
boxes[11].append('rain')
boxes[9].append('table')

# Swap the sandals in Box 11 with the needle in Box 1.
boxes[11].remove('sandals')
boxes[1].remove('needle')
boxes[11].append('needle')
boxes[1].append('sandals')

# Remove the glove and the shark from Box 4.
boxes[4].remove('glove')
boxes[4].remove('shark')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")