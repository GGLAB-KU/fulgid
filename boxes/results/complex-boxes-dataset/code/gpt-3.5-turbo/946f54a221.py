# Initial state of boxes
boxes = {
    0: ['headphone', 'puzzle', 'pen', 'skirt', 'tree'],
    1: ['harmonica', 'pillow'],
    2: ['scissors', 'piano', 'phone', 'apple'],
    3: ['coin', 'snow', 'bus', 'bicycle', 'microwave'],
    4: [],
    5: ['hat', 'forest', 'ship', 'bracelet'],
    6: ['planet', 'shark'],
    7: ['wallet', 'speaker', 'usb', 'bag'],
    8: ['boat'],
    9: [],
    10: ['shirt', 'sandals', 'toothpaste', 'island']
}

# Put the shoe and the microscope and the submarine into Box 3.
boxes[3].append('shoe')
boxes[3].append('microscope')
boxes[3].append('submarine')

# Move the coin and the shoe and the bus from Box 3 to Box 5.
items_to_move = ['coin', 'shoe', 'bus']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Swap the shark in Box 6 with the wallet in Box 7.
boxes[6].remove('shark')
boxes[7].remove('wallet')
boxes[6].append('wallet')
boxes[7].append('shark')

# Swap the speaker in Box 7 with the island in Box 10.
boxes[7].remove('speaker')
boxes[10].remove('island')
boxes[7].append('island')
boxes[10].append('speaker')

# Replace the boat with the glove in Box 8.
boxes[8].remove('boat')
boxes[8].append('glove')

# Move the skirt and the headphone from Box 0 to Box 1.
items_to_move = ['skirt', 'headphone']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Replace the shoe with the blanket in Box 5.
boxes[5].remove('shoe')
boxes[5].append('blanket')

# Replace the phone and the apple and the piano with the sculpture and the thunder and the cloud in Box 2.
boxes[2].remove('phone')
boxes[2].remove('apple')
boxes[2].remove('piano')
boxes[2].append('sculpture')
boxes[2].append('thunder')
boxes[2].append('cloud')

# Put the scissors and the earring into Box 6.
boxes[6].append('scissors')
boxes[6].append('earring')

# Replace the pen and the tree and the puzzle with the cow and the tie and the horse in Box 0.
boxes[0].remove('pen')
boxes[0].remove('tree')
boxes[0].remove('puzzle')
boxes[0].append('cow')
boxes[0].append('tie')
boxes[0].append('horse')

# Replace the bracelet and the forest with the ring and the ocean in Box 5.
boxes[5].remove('bracelet')
boxes[5].remove('forest')
boxes[5].append('ring')
boxes[5].append('ocean')

# Remove the headphone from Box 1.
boxes[1].remove('headphone')

# Replace the glove with the game in Box 8.
boxes[8].remove('glove')
boxes[8].append('game')

# Move the game from Box 8 to Box 10.
boxes[8].remove('game')
boxes[10].append('game')

# Swap the toothpaste in Box 10 with the tie in Box 0.
boxes[10].remove('toothpaste')
boxes[0].remove('tie')
boxes[10].append('tie')
boxes[0].append('toothpaste')

# Remove the cloud and the thunder from Box 2.
boxes[2].remove('cloud')
boxes[2].remove('thunder')

# Replace the bicycle and the microwave with the helmet and the lightning in Box 3.
boxes[3].remove('bicycle')
boxes[3].remove('microwave')
boxes[3].append('helmet')
boxes[3].append('lightning')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")