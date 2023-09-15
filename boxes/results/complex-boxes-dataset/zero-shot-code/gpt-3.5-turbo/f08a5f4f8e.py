box_0 = ['gloves']
box_1 = ['skirt', 'piano', 'speaker', 'wire']
box_2 = ['crown', 'scarf', 'drum', 'microwave']
box_3 = ['mountain', 'oven', 'wig', 'bear', 'shampoo']
box_4 = []
box_5 = ['flower', 'rock', 'umbrella', 'candle', 'grinder']
box_6 = []
box_7 = ['blanket']
box_8 = ['dice', 'violin']
box_9 = []
box_10 = ['branch']

def print_box(box_index, box_items):
    print(f"Box {box_index}: {box_items}")

# Put the toothbrush and the zipper and the dice into Box 7
box_7.extend(['toothbrush', 'zipper', 'dice'])
print_box(7, box_7)

# Put the horn and the basket and the star into Box 4
box_4.extend(['horn', 'basket', 'star'])
print_box(4, box_4)

# Remove the gloves from Box 0
box_0.remove('gloves')
print_box(0, box_0)

# Put the button and the cup and the tie into Box 4
box_4.extend(['button', 'cup', 'tie'])
print_box(4, box_4)

# Move the violin and the dice from Box 8 to Box 1
box_1.extend(box_8)
box_8.clear()
print_box(1, box_1)
print_box(8, box_8)

# Put the cat into Box 8
box_8.append('cat')
print_box(8, box_8)

# Remove the zipper and the blanket from Box 7
box_7.remove('zipper')
box_7.remove('blanket')
print_box(7, box_7)

# Remove the cat from Box 8
box_8.remove('cat')
print_box(8, box_8)

# Put the note and the storm into Box 6
box_6.extend(['note', 'storm'])
print_box(6, box_6)

# Put the blender and the shelf and the pants into Box 10
box_10.extend(['blender', 'shelf', 'pants'])
print_box(10, box_10)

# Swap the microwave in Box 2 with the skirt in Box 1
box_1.remove('skirt')
box_2.remove('microwave')
box_1.append('microwave')
box_2.append('skirt')
print_box(1, box_1)
print_box(2, box_2)

# Put the glove into Box 1
box_1.append('glove')
print_box(1, box_1)

# Replace the drum with the laptop in Box 2
box_2.remove('drum')
box_2.append('laptop')
print_box(2, box_2)

# Remove the storm from Box 6
box_6.remove('storm')
print_box(6, box_6)

# Move the note from Box 6 to Box 8
box_6.remove('note')
box_8.append('note')
print_box(6, box_6)
print_box(8, box_8)

# Replace the wig and the bear and the mountain with the vase and the toaster and the beach in Box 3
box_3.remove('wig')
box_3.remove('bear')
box_3.remove('mountain')
box_3.extend(['vase', 'toaster', 'beach'])
print_box(3, box_3)