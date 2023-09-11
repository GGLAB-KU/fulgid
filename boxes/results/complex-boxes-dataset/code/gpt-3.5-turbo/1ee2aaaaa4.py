# Initial state of boxes
boxes = {
    0: ['zipper', 'lipstick', 'gloves', 'note'],
    1: ['candle', 'belt', 'skirt', 'coat', 'ship'],
    2: ['comb'],
    3: ['bag', 'rocket', 'frame', 'grinder', 'starfish'],
    4: ['meteor', 'beach', 'makeup', 'scarf'],
    5: ['rock'],
    6: ['umbrella', 'ring', 'elephant', 'pillow', 'speaker'],
    7: ['basket', 'telescope', 'fridge'],
    8: ['truck', 'oven', 'shelf', 'toaster', 'dice'],
    9: [],
    10: ['wig', 'earring', 'jacket', 'mixer', 'planet'],
    11: ['seaweed', 'bus'],
    12: []
}

# Put the bracelet and the headphone into Box 6.
boxes[6].append('bracelet')
boxes[6].append('headphone')

# Replace the shelf and the oven and the dice with the guitar and the wire and the dolphin in Box 8.
boxes[8].remove('shelf')
boxes[8].remove('oven')
boxes[8].remove('dice')
boxes[8].append('guitar')
boxes[8].append('wire')
boxes[8].append('dolphin')

# Swap the jacket in Box 10 with the comb in Box 2.
boxes[10].remove('jacket')
boxes[2].remove('comb')
boxes[10].append('comb')
boxes[2].append('jacket')

# Swap the seaweed in Box 11 with the rock in Box 5.
boxes[11].remove('seaweed')
boxes[5].remove('rock')
boxes[11].append('rock')
boxes[5].append('seaweed')

# Move the wire and the truck and the guitar from Box 8 to Box 5.
items_to_move = ['wire', 'truck', 'guitar']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[5].append(item)

# Swap the bus in Box 11 with the meteor in Box 4.
boxes[11].remove('bus')
boxes[4].remove('meteor')
boxes[11].append('meteor')
boxes[4].append('bus')

# Replace the frame and the rocket and the starfish with the rock and the cat and the sun in Box 3.
boxes[3].remove('frame')
boxes[3].remove('rocket')
boxes[3].remove('starfish')
boxes[3].append('rock')
boxes[3].append('cat')
boxes[3].append('sun')

# Replace the comb and the earring with the wig and the bicycle in Box 10.
boxes[10].remove('comb')
boxes[10].remove('earring')
boxes[10].append('wig')
boxes[10].append('bicycle')

# Remove the grinder from Box 3.
boxes[3].remove('grinder')

# Move the cat and the sun and the bag from Box 3 to Box 10.
items_to_move = ['cat', 'sun', 'bag']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[10].append(item)

# Move the fridge from Box 7 to Box 8.
boxes[7].remove('fridge')
boxes[8].append('fridge')

# Swap the skirt in Box 1 with the rock in Box 11.
boxes[1].remove('skirt')
boxes[11].remove('rock')
boxes[1].append('rock')
boxes[11].append('skirt')

# Replace the truck and the guitar with the dress and the necklace in Box 5.
boxes[5].remove('truck')
boxes[5].remove('guitar')
boxes[5].append('dress')
boxes[5].append('necklace')

# Empty Box 10.
boxes[10] = []

# Empty Box 4.
boxes[4] = []

# Remove the basket and the telescope from Box 7.
boxes[7].remove('basket')
boxes[7].remove('telescope')

# Move the seaweed and the dress from Box 5 to Box 3.
boxes[5].remove('seaweed')
boxes[5].remove('dress')
boxes[3].append('seaweed')
boxes[3].append('dress')

# Remove the meteor from Box 11.
boxes[11].remove('meteor')

# Remove the ship and the rock and the belt from Box 1.
items_to_remove = ['ship', 'rock', 'belt']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the lipstick and the note and the zipper with the guitar and the shoes and the bag in Box 0.
boxes[0].remove('lipstick')
boxes[0].remove('note')
boxes[0].remove('zipper')
boxes[0].append('guitar')
boxes[0].append('shoes')
boxes[0].append('bag')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")