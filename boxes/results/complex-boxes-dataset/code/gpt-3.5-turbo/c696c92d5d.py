# Initial state of boxes
boxes = {
    0: ['towel', 'piano', 'leaf', 'ship'],
    1: ['lion'],
    2: ['dog', 'jacket', 'shoes', 'pillow'],
    3: ['clock'],
    4: ['freezer'],
    5: ['toy'],
    6: ['scarf'],
    7: ['table', 'submarine', 'octopus', 'whistle', 'shirt'],
    8: ['key', 'lamp', 'helmet']
}

# Swap the clock in Box 3 with the lion in Box 1.
boxes[1].remove('lion')
boxes[3].remove('clock')
boxes[1].append('clock')
boxes[3].append('lion')

# Replace the lion with the tie in Box 3.
boxes[3].remove('lion')
boxes[3].append('tie')

# Replace the scarf with the bowl in Box 6.
boxes[6].remove('scarf')
boxes[6].append('bowl')

# Put the game into Box 0.
boxes[0].append('game')

# Move the dog and the pillow and the shoes from Box 2 to Box 4.
items_to_move = ['dog', 'pillow', 'shoes']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[4].append(item)

# Move the towel from Box 0 to Box 8.
boxes[0].remove('towel')
boxes[8].append('towel')

# Swap the jacket in Box 2 with the dog in Box 4.
boxes[2].remove('jacket')
boxes[4].remove('dog')
boxes[2].append('dog')
boxes[4].append('jacket')

# Move the dog from Box 2 to Box 6.
boxes[2].remove('dog')
boxes[6].append('dog')

# Put the makeup into Box 8.
boxes[8].append('makeup')

# Move the toy from Box 5 to Box 6.
boxes[5].remove('toy')
boxes[6].append('toy')

# Swap the clock in Box 1 with the leaf in Box 0.
boxes[0].remove('leaf')
boxes[1].remove('clock')
boxes[0].append('clock')
boxes[1].append('leaf')

# Move the game from Box 0 to Box 6.
boxes[0].remove('game')
boxes[6].append('game')

# Put the tie and the frame into Box 0.
boxes[0].append('tie')
boxes[0].append('frame')

# Put the river into Box 7.
boxes[7].append('river')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")