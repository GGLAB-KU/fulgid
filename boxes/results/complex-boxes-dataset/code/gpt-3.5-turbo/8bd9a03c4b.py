# Initial state of boxes
boxes = {
    0: ['butterfly'],
    1: ['lipstick', 'desert', 'fork', 'skirt'],
    2: ['bicycle', 'watch', 'apple'],
    3: ['comb', 'bell', 'lightning', 'moon'],
    4: ['horn'],
    5: ['coral', 'needle', 'shelf', 'rain', 'coat'],
    6: ['dolphin', 'flute', 'game', 'boat', 'bus'],
    7: [],
    8: ['branch', 'snow', 'basket', 'frame'],
    9: ['fish'],
    10: ['helmet', 'battery']
}

# Remove the skirt from Box 1.
boxes[1].remove('skirt')

# Swap the apple in Box 2 with the moon in Box 3.
boxes[2].remove('apple')
boxes[3].remove('moon')
boxes[2].append('moon')
boxes[3].append('apple')

# Remove the battery from Box 10.
boxes[10].remove('battery')

# Swap the needle in Box 5 with the fork in Box 1.
boxes[5].remove('needle')
boxes[1].remove('fork')
boxes[5].append('fork')
boxes[1].append('needle')

# Put the octopus and the drum into Box 0.
boxes[0].append('octopus')
boxes[0].append('drum')

# Replace the watch and the bicycle with the zipper and the note in Box 2.
boxes[2].remove('watch')
boxes[2].remove('bicycle')
boxes[2].append('zipper')
boxes[2].append('note')

# Put the tree and the coin and the phone into Box 5.
items_to_move = ['tree', 'coin', 'phone']
for item in items_to_move:
    boxes[5].append(item)

# Move the frame and the branch from Box 8 to Box 2.
items_to_move = ['frame', 'branch']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[2].append(item)

# Empty Box 0.
boxes[0] = []

# Swap the needle in Box 1 with the fish in Box 9.
boxes[1].remove('needle')
boxes[9].remove('fish')
boxes[1].append('fish')
boxes[9].append('needle')

# Move the note and the moon and the frame from Box 2 to Box 5.
items_to_move = ['note', 'moon', 'frame']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Replace the fish with the gloves in Box 1.
boxes[1].remove('fish')
boxes[1].append('gloves')

# Move the lipstick and the desert and the gloves from Box 1 to Box 3.
items_to_move = ['lipstick', 'desert', 'gloves']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Swap the needle in Box 9 with the zipper in Box 2.
boxes[9].remove('needle')
boxes[2].remove('zipper')
boxes[9].append('zipper')
boxes[2].append('needle')

# Remove the needle from Box 2.
boxes[2].remove('needle')

# Remove the horn from Box 4.
boxes[4].remove('horn')

# Swap the helmet in Box 10 with the coat in Box 5.
boxes[10].remove('helmet')
boxes[5].remove('coat')
boxes[10].append('coat')
boxes[5].append('helmet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")