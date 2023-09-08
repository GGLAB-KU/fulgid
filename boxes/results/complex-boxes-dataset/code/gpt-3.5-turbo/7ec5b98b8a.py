# Initial state of boxes
boxes = {
    0: ['apple'],
    1: ['octopus'],
    2: ['makeup', 'bowl', 'camera'],
    3: ['comb', 'shorts', 'grinder'],
    4: ['coral', 'leaf', 'shoe', 'coat'],
    5: ['motorcycle', 'pen', 'usb'],
    6: ['whistle', 'pants', 'bus', 'freezer'],
    7: ['lipstick', 'bird'],
    8: [],
    9: ['boot'],
    10: [],
    11: ['vase', 'moon', 'paint'],
    12: ['fridge', 'candle', 'rain'],
    13: ['dog', 'drum', 'cup', 'car'],
    14: ['microwave', 'chair', 'horse', 'hat', 'dress']
}

# Move the motorcycle and the usb and the pen from Box 5 to Box 7.
items_to_move = ['motorcycle', 'usb', 'pen']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Remove the drum and the car and the dog from Box 13.
items_to_remove = ['drum', 'car', 'dog']
for item in items_to_remove:
    boxes[13].remove(item)

# Remove the octopus from Box 1.
boxes[1].remove('octopus')

# Swap the cup in Box 13 with the apple in Box 0.
boxes[0].remove('apple')
boxes[13].remove('cup')
boxes[0].append('cup')
boxes[13].append('apple')

# Move the comb and the shorts from Box 3 to Box 11.
items_to_move = ['comb', 'shorts']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[11].append(item)

# Remove the grinder from Box 3.
boxes[3].remove('grinder')

# Put the harmonica and the river and the thread into Box 7.
items_to_add = ['harmonica', 'river', 'thread']
for item in items_to_add:
    boxes[7].append(item)

# Move the pants from Box 6 to Box 4.
boxes[6].remove('pants')
boxes[4].append('pants')

# Swap the apple in Box 13 with the cup in Box 0.
boxes[0].remove('cup')
boxes[13].remove('apple')
boxes[0].append('apple')
boxes[13].append('cup')

# Move the shorts and the paint from Box 11 to Box 10.
boxes[11].remove('shorts')
boxes[11].remove('paint')
boxes[10].append('shorts')
boxes[10].append('paint')

# Replace the apple with the puzzle in Box 0.
boxes[0].remove('apple')
boxes[0].append('puzzle')

# Move the leaf and the pants from Box 4 to Box 0.
boxes[4].remove('leaf')
boxes[4].remove('pants')
boxes[0].append('leaf')
boxes[0].append('pants')

# Move the comb and the moon and the vase from Box 11 to Box 13.
items_to_move = ['comb', 'moon', 'vase']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[13].append(item)

# Move the moon from Box 13 to Box 12.
boxes[13].remove('moon')
boxes[12].append('moon')

# Replace the chair and the hat with the tie and the bicycle in Box 14.
boxes[14].remove('chair')
boxes[14].remove('hat')
boxes[14].append('tie')
boxes[14].append('bicycle')

# Replace the leaf and the puzzle with the crown and the seaweed in Box 0.
boxes[0].remove('leaf')
boxes[0].remove('puzzle')
boxes[0].append('crown')
boxes[0].append('seaweed')

# Remove the thread from Box 7.
boxes[7].remove('thread')

# Move the boot from Box 9 to Box 4.
boxes[9].remove('boot')
boxes[4].append('boot')

# Remove the shoe and the coral and the coat from Box 4.
items_to_remove = ['shoe', 'coral', 'coat']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the bicycle from Box 14.
boxes[14].remove('bicycle')

# Remove the river and the motorcycle from Box 7.
boxes[7].remove('river')
boxes[7].remove('motorcycle')

# Remove the paint and the shorts from Box 10.
boxes[10].remove('paint')
boxes[10].remove('shorts')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")