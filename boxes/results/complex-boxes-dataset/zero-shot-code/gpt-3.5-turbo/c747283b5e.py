box = {
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

def swap_items(box, box_index_1, item_index_1, box_index_2, item_index_2):
    item_1 = box[box_index_1][item_index_1]
    item_2 = box[box_index_2][item_index_2]
    box[box_index_1][item_index_1] = item_2
    box[box_index_2][item_index_2] = item_1

def remove_item(box, box_index, item):
    box[box_index].remove(item)

def empty_box(box, box_index):
    box[box_index] = []

def move_item(box, source_box_index, item_index, destination_box_index):
    item = box[source_box_index][item_index]
    box[source_box_index].remove(item)
    box[destination_box_index].append(item)

# Swap the mountain in Box 7 with the dog in Box 9
swap_items(box, 7, box[7].index('mountain'), 9, box[9].index('dog'))

# Swap the mountain in Box 9 with the game in Box 6
swap_items(box, 9, box[9].index('mountain'), 6, box[6].index('game'))

# Put the apple and the pot into Box 6
box[6].extend(['apple', 'pot'])

# Replace the game with the dress in Box 9
box[9][box[9].index('game')] = 'dress'

# Swap the seaweed in Box 11 with the note in Box 7
swap_items(box, 11, box[11].index('seaweed'), 7, box[7].index('note'))

# Put the apple and the scissors and the grass into Box 9
box[9].extend(['apple', 'scissors', 'grass'])

# Put the elephant into Box 5
box[5].append('elephant')

# Put the lightning and the bracelet and the planet into Box 4
box[4].extend(['lightning', 'bracelet', 'planet'])

# Swap the planet in Box 4 with the necklace in Box 10
swap_items(box, 4, box[4].index('planet'), 10, box[10].index('necklace'))

# Remove the book and the sculpture and the forest from Box 10
remove_item(box, 10, 'book')
remove_item(box, 10, 'sculpture')
remove_item(box, 10, 'forest')

# Remove the necklace and the bracelet and the lightning from Box 4
remove_item(box, 4, 'necklace')
remove_item(box, 4, 'bracelet')
remove_item(box, 4, 'lightning')

# Remove the seaweed and the dog from Box 7
remove_item(box, 7, 'seaweed')
remove_item(box, 7, 'dog')

# Empty Box 11
empty_box(box, 11)

# Move the pot and the apple from Box 6 to Box 11
move_item(box, 6, box[6].index('pot'), 11)
move_item(box, 6, box[6].index('apple'), 11)

# Remove the mountain from Box 6
remove_item(box, 6, 'mountain')

# Swap the fridge in Box 7 with the pot in Box 11
swap_items(box, 7, box[7].index('fridge'), 11, box[11].index('pot'))

# Put the earring and the mountain and the desert into Box 2
box[2].extend(['earring', 'mountain', 'desert'])

# Move the pot from Box 7 to Box 0
move_item(box, 7, box[7].index('pot'), 0)

# Print the contents of each box
for box_index, items in box.items():
    print(f"Box {box_index}: {items}")