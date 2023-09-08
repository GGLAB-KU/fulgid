# Initial state of boxes
boxes = {
    0: ['chair', 'lightning'],
    1: ['star'],
    2: ['piano', 'crown', 'rocket', 'spoon'],
    3: ['candle', 'mixer'],
    4: ['plate', 'necklace', 'paint'],
    5: ['wallet', 'rock'],
    6: ['toaster', 'car', 'tree', 'dog', 'table'],
    7: ['whistle', 'comb', 'shampoo'],
    8: [],
    9: ['speaker', 'lion'],
    10: ['shorts', 'cup', 'microwave'],
    11: ['apple', 'submarine', 'clock', 'earring', 'rain'],
    12: ['watch', 'button', 'bell']
}

# Replace the rain and the submarine and the apple with the microscope and the paint and the cup in Box 11.
boxes[11].remove('rain')
boxes[11].remove('submarine')
boxes[11].remove('apple')
boxes[11].append('microscope')
boxes[11].append('paint')
boxes[11].append('cup')

# Move the clock from Box 11 to Box 0.
boxes[11].remove('clock')
boxes[0].append('clock')

# Replace the rocket and the spoon and the piano with the horse and the skirt and the bowl in Box 2.
boxes[2].remove('rocket')
boxes[2].remove('spoon')
boxes[2].remove('piano')
boxes[2].append('horse')
boxes[2].append('skirt')
boxes[2].append('bowl')

# Put the scissors and the dog into Box 7.
boxes[7].append('scissors')
boxes[7].append('dog')

# Remove the microscope and the paint from Box 11.
boxes[11].remove('microscope')
boxes[11].remove('paint')

# Replace the rock with the sandals in Box 5.
boxes[5].remove('rock')
boxes[5].append('sandals')

# Replace the dog with the coin in Box 7.
boxes[7].remove('dog')
boxes[7].append('coin')

# Remove the candle and the mixer from Box 3.
boxes[3].remove('candle')
boxes[3].remove('mixer')

# Empty Box 9.
boxes[9] = []

# Swap the bell in Box 12 with the sandals in Box 5.
boxes[12].remove('bell')
boxes[5].remove('sandals')
boxes[12].append('sandals')
boxes[5].append('bell')

# Put the horn and the meteor into Box 5.
boxes[5].append('horn')
boxes[5].append('meteor')

# Move the cup and the earring from Box 11 to Box 7.
boxes[11].remove('cup')
boxes[11].remove('earring')
boxes[7].append('cup')
boxes[7].append('earring')

# Swap the microwave in Box 10 with the toaster in Box 6.
boxes[10].remove('microwave')
boxes[6].remove('toaster')
boxes[10].append('toaster')
boxes[6].append('microwave')

# Swap the shorts in Box 10 with the car in Box 6.
boxes[10].remove('shorts')
boxes[6].remove('car')
boxes[10].append('car')
boxes[6].append('shorts')

# Swap the plate in Box 4 with the watch in Box 12.
boxes[4].remove('plate')
boxes[12].remove('watch')
boxes[4].append('watch')
boxes[12].append('plate')

# Replace the clock with the phone in Box 0.
boxes[0].remove('clock')
boxes[0].append('phone')

# Replace the cup and the car and the toaster with the harmonica and the doll and the card in Box 10.
boxes[10].remove('cup')
boxes[10].remove('car')
boxes[10].remove('toaster')
boxes[10].append('harmonica')
boxes[10].append('doll')
boxes[10].append('card')

# Replace the earring with the sock in Box 7.
boxes[7].remove('earring')
boxes[7].append('sock')

# Remove the phone and the lightning and the chair from Box 0.
boxes[0].remove('phone')
boxes[0].remove('lightning')
boxes[0].remove('chair')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")