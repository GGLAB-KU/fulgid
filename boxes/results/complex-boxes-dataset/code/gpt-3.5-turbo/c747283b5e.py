# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['bicycle', 'speaker', 'bag'],
    3: [],
    4: [],
    5: ['violin'],
    6: ['game'],
    7: ['note', 'mountain', 'fridge'],
    8: [],
    9: ['dog'],
    10: ['necklace', 'forest', 'book', 'sculpture'],
    11: ['seaweed', 'guitar', 'keyboard', 'cat']
}

# Swap the mountain in Box 7 with the dog in Box 9.
boxes[7].remove('mountain')
boxes[9].remove('dog')
boxes[7].append('dog')
boxes[9].append('mountain')

# Swap the mountain in Box 9 with the game in Box 6.
boxes[9].remove('mountain')
boxes[6].remove('game')
boxes[9].append('game')
boxes[6].append('mountain')

# Put the apple and the pot into Box 6.
boxes[6].append('apple')
boxes[6].append('pot')

# Replace the game with the dress in Box 9.
boxes[9].remove('game')
boxes[9].append('dress')

# Swap the seaweed in Box 11 with the note in Box 7.
boxes[11].remove('seaweed')
boxes[7].remove('note')
boxes[11].append('note')
boxes[7].append('seaweed')

# Put the apple and the scissors and the grass into Box 9.
boxes[9].append('apple')
boxes[9].append('scissors')
boxes[9].append('grass')

# Put the elephant into Box 5.
boxes[5].append('elephant')

# Put the lightning and the bracelet and the planet into Box 4.
boxes[4].append('lightning')
boxes[4].append('bracelet')
boxes[4].append('planet')

# Swap the planet in Box 4 with the necklace in Box 10.
boxes[4].remove('planet')
boxes[10].remove('necklace')
boxes[4].append('necklace')
boxes[10].append('planet')

# Remove the book and the sculpture and the forest from Box 10.
items_to_remove = ['book', 'sculpture', 'forest']
for item in items_to_remove:
    boxes[10].remove(item)

# Remove the necklace and the bracelet and the lightning from Box 4.
items_to_remove = ['necklace', 'bracelet', 'lightning']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the seaweed and the dog from Box 7.
boxes[7].remove('seaweed')
boxes[7].remove('dog')

# Empty Box 11.
boxes[11] = []

# Move the pot and the apple from Box 6 to Box 11.
boxes[6].remove('pot')
boxes[6].remove('apple')
boxes[11].append('pot')
boxes[11].append('apple')

# Remove the mountain from Box 6.
boxes[6].remove('mountain')

# Swap the fridge in Box 7 with the pot in Box 11.
boxes[7].remove('fridge')
boxes[11].remove('pot')
boxes[7].append('pot')
boxes[11].append('fridge')

# Put the earring and the mountain and the desert into Box 2.
boxes[2].append('earring')
boxes[2].append('mountain')
boxes[2].append('desert')

# Move the pot from Box 7 to Box 0.
boxes[7].remove('pot')
boxes[0].append('pot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")