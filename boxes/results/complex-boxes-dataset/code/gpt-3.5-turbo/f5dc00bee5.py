# Initial state of boxes
boxes = {
    0: ['rock', 'speaker', 'card'],
    1: [],
    2: ['bell', 'chair', 'mixer', 'lightning', 'horse'],
    3: ['button', 'key', 'car', 'shorts', 'perfume'],
    4: ['bicycle', 'ocean', 'fork', 'magnet'],
    5: ['earring', 'coat', 'comet', 'violin', 'tape'],
    6: ['ring', 'elephant', 'spoon'],
    7: ['crown', 'storm', 'dog', 'shoes'],
    8: ['coin', 'bear', 'pants', 'island'],
    9: [],
    10: [],
    11: ['table', 'tie'],
    12: ['frame', 'boot', 'sun'],
    13: ['blender', 'tree', 'vase', 'star', 'clock'],
    14: ['boat']
}

# Put the wallet and the wire into Box 1.
boxes[1].append('wallet')
boxes[1].append('wire')

# Replace the chair and the horse and the bell with the sculpture and the shark and the whistle in Box 2.
boxes[2].remove('chair')
boxes[2].remove('horse')
boxes[2].remove('bell')
boxes[2].append('sculpture')
boxes[2].append('shark')
boxes[2].append('whistle')

# Swap the sculpture in Box 2 with the frame in Box 12.
boxes[2].remove('sculpture')
boxes[12].remove('frame')
boxes[2].append('frame')
boxes[12].append('sculpture')

# Remove the magnet and the ocean from Box 4.
boxes[4].remove('magnet')
boxes[4].remove('ocean')

# Swap the tie in Box 11 with the shoes in Box 7.
boxes[11].remove('tie')
boxes[7].remove('shoes')
boxes[11].append('shoes')
boxes[7].append('tie')

# Swap the wire in Box 1 with the table in Box 11.
boxes[1].remove('wire')
boxes[11].remove('table')
boxes[1].append('table')
boxes[11].append('wire')

# Remove the spoon and the ring from Box 6.
boxes[6].remove('spoon')
boxes[6].remove('ring')

# Move the bicycle from Box 4 to Box 11.
boxes[4].remove('bicycle')
boxes[11].append('bicycle')

# Put the flower into Box 12.
boxes[12].append('flower')

# Remove the tape and the violin from Box 5.
boxes[5].remove('tape')
boxes[5].remove('violin')

# Replace the bear with the needle in Box 8.
boxes[8].remove('bear')
boxes[8].append('needle')

# Remove the perfume and the car and the button from Box 3.
boxes[3].remove('perfume')
boxes[3].remove('car')
boxes[3].remove('button')

# Move the boat from Box 14 to Box 3.
boxes[14].remove('boat')
boxes[3].append('boat')

# Replace the storm with the ship in Box 7.
boxes[7].remove('storm')
boxes[7].append('ship')

# Replace the dog and the crown and the ship with the mirror and the truck and the dice in Box 7.
boxes[7].remove('dog')
boxes[7].remove('crown')
boxes[7].remove('ship')
boxes[7].append('mirror')
boxes[7].append('truck')
boxes[7].append('dice')

# Replace the wire with the shorts in Box 11.
boxes[11].remove('wire')
boxes[11].append('shorts')

# Put the octopus and the cat into Box 4.
boxes[4].append('octopus')
boxes[4].append('cat')

# Swap the needle in Box 8 with the flower in Box 12.
boxes[8].remove('needle')
boxes[12].remove('flower')
boxes[8].append('flower')
boxes[12].append('needle')

# Replace the elephant with the wire in Box 6.
boxes[6].remove('elephant')
boxes[6].append('wire')

# Swap the truck in Box 7 with the sculpture in Box 12.
boxes[7].remove('truck')
boxes[12].remove('sculpture')
boxes[7].append('sculpture')
boxes[12].append('truck')

# Replace the dice and the tie with the doll and the grass in Box 7.
boxes[7].remove('dice')
boxes[7].remove('tie')
boxes[7].append('doll')
boxes[7].append('grass')

# Remove the earring and the coat from Box 5.
boxes[5].remove('earring')
boxes[5].remove('coat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")