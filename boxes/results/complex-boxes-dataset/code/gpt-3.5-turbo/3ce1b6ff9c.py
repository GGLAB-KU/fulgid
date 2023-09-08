# Initial state of boxes
boxes = {
    0: ['dress', 'grinder', 'vase', 'truck', 'note'],
    1: ['lion', 'comb', 'flute', 'tape'],
    2: ['car', 'swimsuit', 'bowl'],
    3: ['button', 'helmet'],
    4: ['spoon', 'brush'],
    5: ['wig'],
    6: ['boot', 'guitar', 'desert', 'coat', 'leaf'],
    7: ['cat', 'scarf', 'bracelet', 'thunder'],
    8: [],
    9: ['skirt', 'oven'],
    10: [],
    11: ['speaker', 'horse', 'forest', 'crown'],
    12: ['fork', 'river', 'flower', 'controller', 'violin'],
    13: ['bus', 'key', 'ring', 'mountain']
}

# Move the flower and the river from Box 12 to Box 8.
boxes[12].remove('flower')
boxes[12].remove('river')
boxes[8].append('flower')
boxes[8].append('river')

# Move the note and the dress from Box 0 to Box 3.
boxes[0].remove('note')
boxes[0].remove('dress')
boxes[3].append('note')
boxes[3].append('dress')

# Swap the bus in Box 13 with the cat in Box 7.
boxes[13].remove('bus')
boxes[7].remove('cat')
boxes[13].append('cat')
boxes[7].append('bus')

# Empty Box 8.
boxes[8] = []

# Remove the car from Box 2.
boxes[2].remove('car')

# Move the wig from Box 5 to Box 6.
boxes[5].remove('wig')
boxes[6].append('wig')

# Swap the bowl in Box 2 with the crown in Box 11.
boxes[2].remove('bowl')
boxes[11].remove('crown')
boxes[2].append('crown')
boxes[11].append('bowl')

# Move the controller and the violin and the fork from Box 12 to Box 2.
items_to_move = ['controller', 'violin', 'fork']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[2].append(item)

# Move the skirt from Box 9 to Box 4.
boxes[9].remove('skirt')
boxes[4].append('skirt')

# Move the key from Box 13 to Box 0.
boxes[13].remove('key')
boxes[0].append('key')

# Remove the bracelet and the thunder from Box 7.
boxes[7].remove('bracelet')
boxes[7].remove('thunder')

# Replace the bowl and the horse with the piano and the paint in Box 11.
boxes[11].remove('bowl')
boxes[11].remove('horse')
boxes[11].append('piano')
boxes[11].append('paint')

# Remove the dress from Box 3.
boxes[3].remove('dress')

# Put the lion and the note into Box 13.
boxes[1].remove('lion')
boxes[0].remove('note')
boxes[13].append('lion')
boxes[13].append('note')

# Swap the scarf in Box 7 with the lion in Box 13.
boxes[7].remove('scarf')
boxes[13].remove('lion')
boxes[7].append('lion')
boxes[13].append('scarf')

# Remove the truck and the key from Box 0.
boxes[0].remove('truck')
boxes[0].remove('key')

# Move the coat and the desert from Box 6 to Box 0.
boxes[6].remove('coat')
boxes[6].remove('desert')
boxes[0].append('coat')
boxes[0].append('desert')

# Swap the leaf in Box 6 with the cat in Box 13.
boxes[6].remove('leaf')
boxes[13].remove('cat')
boxes[6].append('cat')
boxes[13].append('leaf')

# Put the dog into Box 3.
boxes[3].append('dog')

# Remove the forest from Box 11.
boxes[11].remove('forest')

# Replace the helmet and the note and the dog with the thunder and the scarf and the meteor in Box 3.
boxes[3].remove('helmet')
boxes[3].remove('note')
boxes[3].remove('dog')
boxes[3].append('thunder')
boxes[3].append('scarf')
boxes[3].append('meteor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")