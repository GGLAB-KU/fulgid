# Initial state of boxes
boxes = {
    0: ['skirt', 'violin', 'rocket'],
    1: ['freezer', 'flute', 'watch', 'harmonica', 'moon'],
    2: ['meteor', 'jungle', 'shoe'],
    3: ['controller', 'fridge', 'boot'],
    4: ['desert', 'sculpture', 'mountain'],
    5: ['bicycle'],
    6: ['oven', 'plane', 'bear', 'camera', 'plate'],
    7: ['tiger', 'jacket', 'snow', 'thread', 'needle'],
    8: ['truck', 'earring', 'table', 'coin'],
    9: ['coral'],
    10: ['guitar', 'mixer', 'planet']
}

# Move the bicycle from Box 5 to Box 3.
boxes[5].remove('bicycle')
boxes[3].append('bicycle')

# Put the necklace and the note and the horse into Box 4.
items_to_move = ['necklace', 'note', 'horse']
for item in items_to_move:
    boxes[4].append(item)

# Move the mixer and the guitar and the planet from Box 10 to Box 7.
items_to_move = ['mixer', 'guitar', 'planet']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[7].append(item)

# Move the note and the mountain and the sculpture from Box 4 to Box 6.
items_to_move = ['note', 'mountain', 'sculpture']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Replace the rocket and the violin with the pot and the battery in Box 0.
boxes[0].remove('rocket')
boxes[0].remove('violin')
boxes[0].append('pot')
boxes[0].append('battery')

# Put the shoes and the brush into Box 0.
items_to_move = ['shoes', 'brush']
for item in items_to_move:
    boxes[0].append(item)

# Replace the pot with the dress in Box 0.
boxes[0].remove('pot')
boxes[0].append('dress')

# Move the necklace and the desert and the horse from Box 4 to Box 7.
items_to_move = ['necklace', 'desert', 'horse']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[7].append(item)

# Put the pot and the bus into Box 5.
items_to_move = ['pot', 'bus']
for item in items_to_move:
    boxes[5].append(item)

# Put the lipstick and the pot into Box 3.
items_to_move = ['lipstick', 'pot']
for item in items_to_move:
    boxes[3].append(item)

# Replace the jacket and the planet and the snow with the bicycle and the comb and the rock in Box 7.
boxes[7].remove('jacket')
boxes[7].remove('planet')
boxes[7].remove('snow')
boxes[7].append('bicycle')
boxes[7].append('comb')
boxes[7].append('rock')

# Move the bus from Box 5 to Box 3.
boxes[5].remove('bus')
boxes[3].append('bus')

# Swap the rock in Box 7 with the bear in Box 6.
boxes[7].remove('rock')
boxes[6].remove('bear')
boxes[7].append('bear')
boxes[6].append('rock')

# Swap the coral in Box 9 with the freezer in Box 1.
boxes[9].remove('coral')
boxes[1].remove('freezer')
boxes[9].append('freezer')
boxes[1].append('coral')

# Remove the dress and the battery from Box 0.
boxes[0].remove('dress')
boxes[0].remove('battery')

# Put the seaweed and the beach and the bear into Box 10.
items_to_move = ['seaweed', 'beach', 'bear']
for item in items_to_move:
    boxes[10].append(item)

# Replace the meteor and the shoe and the jungle with the guitar and the bracelet and the frame in Box 2.
boxes[2].remove('meteor')
boxes[2].remove('shoe')
boxes[2].remove('jungle')
boxes[2].append('guitar')
boxes[2].append('bracelet')
boxes[2].append('frame')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")