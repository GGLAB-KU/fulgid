# Initial state of boxes
boxes = {
    0: ['fridge', 'magnet', 'phone', 'coin'],
    1: ['apple', 'sock', 'planet', 'drum', 'horse'],
    2: [],
    3: ['toaster', 'thunder'],
    4: ['blanket'],
    5: ['camera', 'star'],
    6: ['storm', 'vase'],
    7: ['coat', 'octopus', 'comb', 'boot'],
    8: ['flute', 'shoe', 'starfish', 'shoes', 'earring'],
    9: ['laptop'],
    10: ['umbrella', 'beach', 'wire'],
    11: [],
    12: ['console', 'towel', 'island']
}

# Replace the blanket with the controller in Box 4.
boxes[4].remove('blanket')
boxes[4].append('controller')

# Remove the drum from Box 1.
boxes[1].remove('drum')

# Replace the camera with the wire in Box 5.
boxes[5].remove('camera')
boxes[5].append('wire')

# Swap the comb in Box 7 with the controller in Box 4.
boxes[7].remove('comb')
boxes[4].remove('controller')
boxes[7].append('controller')
boxes[4].append('comb')

# Swap the flute in Box 8 with the wire in Box 10.
boxes[8].remove('flute')
boxes[10].remove('wire')
boxes[8].append('wire')
boxes[10].append('flute')

# Replace the storm with the apple in Box 6.
boxes[6].remove('storm')
boxes[6].append('apple')

# Replace the starfish and the shoes with the game and the rain in Box 8.
boxes[8].remove('starfish')
boxes[8].remove('shoes')
boxes[8].append('game')
boxes[8].append('rain')

# Remove the comb from Box 4.
boxes[4].remove('comb')

# Remove the umbrella and the beach from Box 10.
boxes[10].remove('umbrella')
boxes[10].remove('beach')

# Move the toaster from Box 3 to Box 0.
boxes[3].remove('toaster')
boxes[0].append('toaster')

# Replace the coin with the bicycle in Box 0.
boxes[0].remove('coin')
boxes[0].append('bicycle')

# Move the laptop from Box 9 to Box 11.
boxes[9].remove('laptop')
boxes[11].append('laptop')

# Swap the thunder in Box 3 with the shoe in Box 8.
boxes[3].remove('thunder')
boxes[8].remove('shoe')
boxes[3].append('shoe')
boxes[8].append('thunder')

# Remove the horse and the sock and the apple from Box 1.
items_to_remove = ['horse', 'sock', 'apple']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the laptop from Box 11 to Box 7.
boxes[11].remove('laptop')
boxes[7].append('laptop')

# Replace the towel with the wallet in Box 12.
boxes[12].remove('towel')
boxes[12].append('wallet')

# Replace the planet with the violin in Box 1.
boxes[1].remove('planet')
boxes[1].append('violin')

# Remove the wallet from Box 12.
boxes[12].remove('wallet')

# Replace the shoe with the fish in Box 3.
boxes[3].remove('shoe')
boxes[3].append('fish')

# Remove the fish from Box 3.
boxes[3].remove('fish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")