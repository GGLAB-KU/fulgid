# Initial state of boxes
boxes = {
    0: ['car', 'shirt', 'storm'],
    1: ['fish', 'grinder', 'river', 'game', 'microwave'],
    2: [],
    3: ['wig', 'beach', 'jacket'],
    4: ['console', 'bracelet', 'scarf', 'helmet', 'dolphin'],
    5: ['chair'],
    6: ['dress', 'elephant', 'desert', 'headphone', 'book'],
    7: ['magnet', 'comet'],
    8: ['crown', 'sculpture', 'hat'],
    9: ['brush', 'watch'],
    10: ['starfish', 'bus', 'gloves'],
    11: ['umbrella', 'battery', 'sock'],
    12: ['usb'],
    13: ['doll']
}

# Replace the battery with the plane in Box 11.
boxes[11].remove('battery')
boxes[11].append('plane')

# Swap the bus in Box 10 with the microwave in Box 1.
boxes[10].remove('bus')
boxes[1].remove('microwave')
boxes[10].append('microwave')
boxes[1].append('bus')

# Move the sock from Box 11 to Box 4.
boxes[11].remove('sock')
boxes[4].append('sock')

# Put the scissors and the coat and the planet into Box 4.
items_to_put = ['scissors', 'coat', 'planet']
for item in items_to_put:
    boxes[4].append(item)

# Replace the hat and the sculpture with the boot and the lion in Box 8.
boxes[8].remove('hat')
boxes[8].remove('sculpture')
boxes[8].append('boot')
boxes[8].append('lion')

# Put the flower and the sun into Box 4.
items_to_put = ['flower', 'sun']
for item in items_to_put:
    boxes[4].append(item)

# Move the umbrella from Box 11 to Box 5.
boxes[11].remove('umbrella')
boxes[5].append('umbrella')

# Swap the usb in Box 12 with the car in Box 0.
boxes[12].remove('usb')
boxes[0].remove('car')
boxes[12].append('car')
boxes[0].append('usb')

# Replace the elephant and the book and the desert with the motorcycle and the keyboard and the sandals in Box 6.
boxes[6].remove('elephant')
boxes[6].remove('book')
boxes[6].remove('desert')
boxes[6].append('motorcycle')
boxes[6].append('keyboard')
boxes[6].append('sandals')

# Put the train into Box 6.
boxes[6].append('train')

# Put the dolphin and the tiger into Box 9.
items_to_put = ['dolphin', 'tiger']
for item in items_to_put:
    boxes[9].append(item)

# Replace the boot and the lion with the wire and the shirt in Box 8.
boxes[8].remove('boot')
boxes[8].remove('lion')
boxes[8].append('wire')
boxes[8].append('shirt')

# Replace the starfish and the microwave and the gloves with the swimsuit and the console and the rocket in Box 10.
boxes[10].remove('starfish')
boxes[10].remove('microwave')
boxes[10].remove('gloves')
boxes[10].append('swimsuit')
boxes[10].append('console')
boxes[10].append('rocket')

# Move the wig and the beach from Box 3 to Box 9.
boxes[3].remove('wig')
boxes[3].remove('beach')
boxes[9].append('wig')
boxes[9].append('beach')

# Replace the umbrella and the chair with the toaster and the ship in Box 5.
boxes[5].remove('umbrella')
boxes[5].remove('chair')
boxes[5].append('toaster')
boxes[5].append('ship')

# Replace the magnet and the comet with the apple and the grass in Box 7.
boxes[7].remove('magnet')
boxes[7].remove('comet')
boxes[7].append('apple')
boxes[7].append('grass')

# Replace the shirt and the crown and the wire with the cup and the doll and the seaweed in Box 8.
boxes[8].remove('shirt')
boxes[8].remove('crown')
boxes[8].remove('wire')
boxes[8].append('cup')
boxes[8].append('doll')
boxes[8].append('seaweed')

# Move the car from Box 12 to Box 6.
boxes[12].remove('car')
boxes[6].append('car')

# Move the rocket and the swimsuit and the console from Box 10 to Box 6.
items_to_move = ['rocket', 'swimsuit', 'console']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[6].append(item)

# Replace the ship and the toaster with the cat and the toy in Box 5.
boxes[5].remove('ship')
boxes[5].remove('toaster')
boxes[5].append('cat')
boxes[5].append('toy')

# Swap the apple in Box 7 with the doll in Box 13.
boxes[7].remove('apple')
boxes[13].remove('doll')
boxes[7].append('doll')
boxes[13].append('apple')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")