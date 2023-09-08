# Initial state of boxes
boxes = {
    0: ['fork', 'toothpaste', 'toy', 'car', 'boat'],
    1: ['blanket'],
    2: ['candle', 'sandals'],
    3: ['pants', 'bracelet', 'boot', 'battery', 'pot'],
    4: [],
    5: [],
    6: [],
    7: ['necklace', 'shoes', 'drum'],
    8: ['mixer', 'key', 'sun', 'bicycle'],
    9: ['brush', 'harmonica'],
    10: ['doll', 'bus', 'table']
}

# Remove the candle and the sandals from Box 2.
boxes[2].remove('candle')
boxes[2].remove('sandals')

# Move the brush from Box 9 to Box 7.
boxes[9].remove('brush')
boxes[7].append('brush')

# Remove the necklace from Box 7.
boxes[7].remove('necklace')

# Remove the drum and the shoes from Box 7.
boxes[7].remove('drum')
boxes[7].remove('shoes')

# Swap the brush in Box 7 with the toothpaste in Box 0.
boxes[7].remove('brush')
boxes[0].remove('toothpaste')
boxes[7].append('toothpaste')
boxes[0].append('brush')

# Move the toothpaste from Box 7 to Box 2.
boxes[7].remove('toothpaste')
boxes[2].append('toothpaste')

# Put the fork into Box 9.
boxes[0].remove('fork')
boxes[9].append('fork')

# Remove the blanket from Box 1.
boxes[1].remove('blanket')

# Swap the doll in Box 10 with the brush in Box 0.
boxes[10].remove('doll')
boxes[0].remove('brush')
boxes[10].append('brush')
boxes[0].append('doll')

# Move the key and the bicycle from Box 8 to Box 0.
boxes[8].remove('key')
boxes[8].remove('bicycle')
boxes[0].append('key')
boxes[0].append('bicycle')

# Replace the bicycle and the key with the bag and the zipper in Box 0.
boxes[0].remove('bicycle')
boxes[0].remove('key')
boxes[0].append('bag')
boxes[0].append('zipper')

# Replace the table with the desert in Box 10.
boxes[10].remove('table')
boxes[10].append('desert')

# Move the boot and the bracelet from Box 3 to Box 5.
boxes[3].remove('boot')
boxes[3].remove('bracelet')
boxes[5].append('boot')
boxes[5].append('bracelet')

# Move the mixer from Box 8 to Box 6.
boxes[8].remove('mixer')
boxes[6].append('mixer')

# Remove the harmonica and the fork from Box 9.
boxes[9].remove('harmonica')
boxes[9].remove('fork')

# Put the hat and the dog and the grass into Box 0.
items_to_add = ['hat', 'dog', 'grass']
for item in items_to_add:
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")