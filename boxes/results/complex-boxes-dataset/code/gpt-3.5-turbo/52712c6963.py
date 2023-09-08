# Initial state of boxes
boxes = {
    0: ['perfume', 'needle', 'thunder'],
    1: ['planet', 'starfish', 'sock', 'thread', 'truck'],
    2: ['river', 'glove', 'moon', 'gloves', 'blender'],
    3: ['book'],
    4: [],
    5: ['dress', 'rock', 'note', 'boat'],
    6: ['battery', 'glasses'],
    7: ['bell', 'shelf', 'skirt'],
    8: [],
    9: ['rain', 'coral', 'storm'],
    10: ['brush', 'lightning', 'jacket', 'bowl', 'helmet']
}

# Remove the bowl and the brush from Box 10.
boxes[10].remove('bowl')
boxes[10].remove('brush')

# Swap the gloves in Box 2 with the perfume in Box 0.
boxes[0].remove('perfume')
boxes[2].remove('gloves')
boxes[0].append('gloves')
boxes[2].append('perfume')

# Swap the storm in Box 9 with the dress in Box 5.
boxes[5].remove('dress')
boxes[9].remove('storm')
boxes[5].append('storm')
boxes[9].append('dress')

# Remove the thunder from Box 0.
boxes[0].remove('thunder')

# Swap the gloves in Box 0 with the jacket in Box 10.
boxes[0].remove('gloves')
boxes[10].remove('jacket')
boxes[0].append('jacket')
boxes[10].append('gloves')

# Put the comb into Box 2.
boxes[2].append('comb')

# Move the book from Box 3 to Box 10.
boxes[3].remove('book')
boxes[10].append('book')

# Put the belt into Box 8.
boxes[8].append('belt')

# Remove the needle and the jacket from Box 0.
boxes[0].remove('needle')
boxes[0].remove('jacket')

# Empty Box 7.
boxes[7] = []

# Move the perfume and the glove and the comb from Box 2 to Box 10.
items_to_move = ['perfume', 'glove', 'comb']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[10].append(item)

# Empty Box 1.
boxes[1] = []

# Swap the book in Box 10 with the glasses in Box 6.
boxes[10].remove('book')
boxes[6].remove('glasses')
boxes[10].append('glasses')
boxes[6].append('book')

# Replace the glove with the boat in Box 10.
boxes[10].remove('glove')
boxes[10].append('boat')

# Replace the belt with the river in Box 8.
boxes[8].remove('belt')
boxes[8].append('river')

# Replace the rain and the dress with the car and the makeup in Box 9.
boxes[9].remove('rain')
boxes[9].remove('dress')
boxes[9].append('car')
boxes[9].append('makeup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")