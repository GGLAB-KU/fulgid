# Initial state of boxes
boxes = {
    0: ['mixer'],
    1: ['drum', 'shampoo', 'butterfly', 'zipper', 'submarine'],
    2: ['cat'],
    3: [],
    4: ['flute', 'grinder', 'rocket'],
    5: [],
    6: ['microwave', 'toothpaste', 'bus'],
    7: ['coin', 'starfish', 'horse', 'harmonica', 'wallet'],
    8: ['lipstick', 'sandals'],
    9: ['moon'],
    10: [],
    11: [],
    12: ['bracelet', 'necklace', 'headphone']
}

# Replace the cat with the pillow in Box 2.
boxes[2].remove('cat')
boxes[2].append('pillow')

# Replace the pillow with the ring in Box 2.
boxes[2].remove('pillow')
boxes[2].append('ring')

# Swap the headphone in Box 12 with the toothpaste in Box 6.
boxes[12].remove('headphone')
boxes[6].remove('toothpaste')
boxes[12].append('toothpaste')
boxes[6].append('headphone')

# Put the doll and the storm into Box 6.
boxes[6].append('doll')
boxes[6].append('storm')

# Replace the mixer with the star in Box 0.
boxes[0].remove('mixer')
boxes[0].append('star')

# Replace the lipstick with the shorts in Box 8.
boxes[8].remove('lipstick')
boxes[8].append('shorts')

# Swap the microwave in Box 6 with the star in Box 0.
boxes[6].remove('microwave')
boxes[0].remove('star')
boxes[6].append('star')
boxes[0].append('microwave')

# Move the bracelet from Box 12 to Box 1.
boxes[12].remove('bracelet')
boxes[1].append('bracelet')

# Remove the rocket and the flute and the grinder from Box 4.
items_to_remove = ['rocket', 'flute', 'grinder']
for item in items_to_remove:
    boxes[4].remove(item)

# Replace the sandals and the shorts with the basket and the tree in Box 8.
boxes[8].remove('sandals')
boxes[8].remove('shorts')
boxes[8].append('basket')
boxes[8].append('tree')

# Move the microwave from Box 0 to Box 8.
boxes[0].remove('microwave')
boxes[8].append('microwave')

# Put the lightning and the controller and the tie into Box 12.
boxes[12].append('lightning')
boxes[12].append('controller')
boxes[12].append('tie')

# Put the car and the belt into Box 3.
boxes[3].append('car')
boxes[3].append('belt')

# Swap the car in Box 3 with the microwave in Box 8.
boxes[3].remove('car')
boxes[8].remove('microwave')
boxes[3].append('microwave')
boxes[8].append('car')

# Put the spoon into Box 5.
boxes[5].append('spoon')

# Replace the moon with the keyboard in Box 9.
boxes[9].remove('moon')
boxes[9].append('keyboard')

# Move the belt and the microwave from Box 3 to Box 12.
boxes[3].remove('belt')
boxes[3].remove('microwave')
boxes[12].append('belt')
boxes[12].append('microwave')

# Replace the horse and the harmonica with the bird and the desert in Box 7.
boxes[7].remove('horse')
boxes[7].remove('harmonica')
boxes[7].append('bird')
boxes[7].append('desert')

# Put the bowl into Box 11.
boxes[11].append('bowl')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")