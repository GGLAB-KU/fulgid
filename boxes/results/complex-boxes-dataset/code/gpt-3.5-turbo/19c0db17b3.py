# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['chair', 'bracelet', 'usb'],
    3: ['comb', 'watch', 'meteor', 'earring'],
    4: ['rain', 'cup', 'dolphin', 'car'],
    5: ['thread', 'grinder', 'candle', 'tie'],
    6: ['doll', 'dice', 'bird'],
    7: [],
    8: [],
    9: ['dog', 'bicycle', 'blanket', 'dress', 'scissors'],
    10: ['submarine', 'mask', 'fridge', 'piano'],
    11: ['lamp', 'rock'],
    12: []
}

# Replace the rock and the lamp with the charger and the ocean in Box 11.
boxes[11].remove('rock')
boxes[11].remove('lamp')
boxes[11].append('charger')
boxes[11].append('ocean')

# Remove the dolphin from Box 4.
boxes[4].remove('dolphin')

# Move the bicycle from Box 9 to Box 4.
boxes[9].remove('bicycle')
boxes[4].append('bicycle')

# Put the helmet and the moon into Box 2.
boxes[2].append('helmet')
boxes[2].append('moon')

# Replace the bird with the clock in Box 6.
boxes[6].remove('bird')
boxes[6].append('clock')

# Put the frame into Box 5.
boxes[5].append('frame')

# Move the ocean from Box 11 to Box 3.
boxes[11].remove('ocean')
boxes[3].append('ocean')

# Replace the moon with the horn in Box 2.
boxes[2].remove('moon')
boxes[2].append('horn')

# Move the bicycle from Box 4 to Box 11.
boxes[4].remove('bicycle')
boxes[11].append('bicycle')

# Move the blanket and the dog and the dress from Box 9 to Box 4.
items_to_move = ['blanket', 'dog', 'dress']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[4].append(item)

# Replace the candle and the tie and the grinder with the pants and the basket and the jungle in Box 5.
boxes[5].remove('candle')
boxes[5].remove('tie')
boxes[5].remove('grinder')
boxes[5].append('pants')
boxes[5].append('basket')
boxes[5].append('jungle')

# Replace the pants and the thread with the earring and the grinder in Box 5.
boxes[5].remove('pants')
boxes[5].remove('thread')
boxes[5].append('earring')
boxes[5].append('grinder')

# Move the dice and the doll from Box 6 to Box 1.
boxes[6].remove('dice')
boxes[6].remove('doll')
boxes[1].append('dice')
boxes[1].append('doll')

# Empty Box 6.
boxes[6] = []

# Empty Box 1.
boxes[1] = []

# Replace the dress and the blanket and the rain with the lightning and the microscope and the butterfly in Box 4.
boxes[4].remove('dress')
boxes[4].remove('blanket')
boxes[4].remove('rain')
boxes[4].append('lightning')
boxes[4].append('microscope')
boxes[4].append('butterfly')

# Remove the fridge from Box 10.
boxes[10].remove('fridge')

# Remove the earring from Box 3.
boxes[3].remove('earring')

# Put the watch and the thread into Box 7.
boxes[7].append('watch')
boxes[7].append('thread')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")