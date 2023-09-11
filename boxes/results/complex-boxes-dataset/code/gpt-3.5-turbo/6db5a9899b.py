# Initial state of boxes
boxes = {
    0: ['dress', 'plate'],
    1: ['keyboard', 'planet', 'flower', 'dice', 'bracelet'],
    2: ['camera', 'makeup', 'beach'],
    3: ['coin', 'shorts'],
    4: [],
    5: ['train'],
    6: ['violin', 'glasses', 'key', 'shoes', 'mixer'],
    7: [],
    8: [],
    9: ['skirt'],
    10: []
}

# Replace the skirt with the horse in Box 9.
boxes[9].remove('skirt')
boxes[9].append('horse')

# Replace the makeup and the camera with the storm and the necklace in Box 2.
boxes[2].remove('makeup')
boxes[2].remove('camera')
boxes[2].append('storm')
boxes[2].append('necklace')

# Remove the train from Box 5.
boxes[5].remove('train')

# Remove the keyboard and the bracelet from Box 1.
boxes[1].remove('keyboard')
boxes[1].remove('bracelet')

# Remove the flower and the dice from Box 1.
boxes[1].remove('flower')
boxes[1].remove('dice')

# Swap the horse in Box 9 with the mixer in Box 6.
boxes[9].remove('horse')
boxes[6].remove('mixer')
boxes[9].append('mixer')
boxes[6].append('horse')

# Move the violin and the glasses from Box 6 to Box 1.
boxes[6].remove('violin')
boxes[6].remove('glasses')
boxes[1].append('violin')
boxes[1].append('glasses')

# Swap the planet in Box 1 with the shorts in Box 3.
boxes[1].remove('planet')
boxes[3].remove('shorts')
boxes[1].append('shorts')
boxes[3].append('planet')

# Move the plate from Box 0 to Box 3.
boxes[0].remove('plate')
boxes[3].append('plate')

# Replace the dress with the tiger in Box 0.
boxes[0].remove('dress')
boxes[0].append('tiger')

# Put the seaweed into Box 5.
boxes[5].append('seaweed')

# Replace the mixer with the table in Box 9.
boxes[9].remove('mixer')
boxes[9].append('table')

# Put the keyboard and the pot into Box 8.
boxes[8].append('keyboard')
boxes[8].append('pot')

# Move the tiger from Box 0 to Box 10.
boxes[0].remove('tiger')
boxes[10].append('tiger')

# Replace the table with the rain in Box 9.
boxes[9].remove('table')
boxes[9].append('rain')

# Remove the rain from Box 9.
boxes[9].remove('rain')

# Replace the keyboard and the pot with the sandals and the horn in Box 8.
boxes[8].remove('keyboard')
boxes[8].remove('pot')
boxes[8].append('sandals')
boxes[8].append('horn')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")