box_0 = ['shorts']
box_1 = ['toaster']
box_2 = ['cup', 'basket', 'grinder', 'oven', 'bus']
box_3 = ['lion', 'tape', 'brush', 'button']
box_4 = ['pen']
box_5 = ['candle', 'whistle']
box_6 = ['submarine', 'laptop', 'headphone', 'table', 'watch']
box_7 = ['sun', 'meteor', 'beach']
box_8 = ['ship']
box_9 = ['flute', 'wire']
box_10 = ['drum', 'pants', 'shoes', 'hat', 'comb']
box_11 = ['glove', 'sandals']
box_12 = ['lightning', 'towel', 'necklace', 'cloud']
box_13 = ['pillow']
box_14 = ['rocket']

def print_box(box_index):
    if box_index == 0:
        print("Box 0:", box_0)
    elif box_index == 1:
        print("Box 1:", box_1)
    elif box_index == 2:
        print("Box 2:", box_2)
    elif box_index == 3:
        print("Box 3:", box_3)
    elif box_index == 4:
        print("Box 4:", box_4)
    elif box_index == 5:
        print("Box 5:", box_5)
    elif box_index == 6:
        print("Box 6:", box_6)
    elif box_index == 7:
        print("Box 7:", box_7)
    elif box_index == 8:
        print("Box 8:", box_8)
    elif box_index == 9:
        print("Box 9:", box_9)
    elif box_index == 10:
        print("Box 10:", box_10)
    elif box_index == 11:
        print("Box 11:", box_11)
    elif box_index == 12:
        print("Box 12:", box_12)
    elif box_index == 13:
        print("Box 13:", box_13)
    elif box_index == 14:
        print("Box 14:", box_14)
    else:
        print("Invalid box index")

# Put the basket and the mixer into Box 3
box_3.extend(['basket', 'mixer'])

# Put the glove and the bear into Box 0
box_0.extend(['glove', 'bear'])

# Swap the pillow in Box 13 with the toaster in Box 1
box_13.remove('pillow')
box_1.remove('toaster')
box_13.append('toaster')
box_1.append('pillow')

# Replace the shoes and the pants and the drum with the desert and the tiger and the lock in Box 10
box_10.remove('shoes')
box_10.remove('pants')
box_10.remove('drum')
box_10.extend(['desert', 'tiger', 'lock'])

# Move the whistle and the candle from Box 5 to Box 0
box_5.remove('whistle')
box_5.remove('candle')
box_0.extend(['whistle', 'candle'])

# Put the sculpture into Box 0
box_0.append('sculpture')

# Remove the pen from Box 4
box_4.remove('pen')

# Empty Box 14
box_14 = []

# Move the ship from Box 8 to Box 13
box_8.remove('ship')
box_13.append('ship')

# Replace the mixer and the brush with the tape and the tie in Box 3
box_3.remove('mixer')
box_3.remove('brush')
box_3.extend(['tape', 'tie'])

# Put the game into Box 14
box_14.append('game')

# Replace the glove with the island in Box 11
box_11.remove('glove')
box_11.append('island')

# Replace the bus and the cup and the basket with the battery and the headphone and the sock in Box 2
box_2.remove('bus')
box_2.remove('cup')
box_2.remove('basket')
box_2.extend(['battery', 'headphone', 'sock'])

# Put the truck into Box 13
box_13.append('truck')

# Replace the sandals with the zipper in Box 11
box_11.remove('sandals')
box_11.append('zipper')

# Move the game from Box 14 to Box 11
box_14.remove('game')
box_11.append('game')

# Remove the bear and the sculpture and the shorts from Box 0
box_0.remove('bear')
box_0.remove('sculpture')
box_0.remove('shorts')

# Put the charger into Box 2
box_2.append('charger')

# Swap the flute in Box 9 with the beach in Box 7
box_9.remove('flute')
box_7.remove('beach')
box_9.append('beach')
box_7.append('flute')

# Swap the toaster in Box 13 with the button in Box 3
box_13.remove('toaster')
box_3.remove('button')
box_13.append('button')
box_3.append('toaster')

# Swap the tape in Box 3 with the candle in Box 0
box_3.remove('tape')
box_0.remove('candle')
box_3.append('candle')
box_0.append('tape')

# Put the console and the pan into Box 8
box_8.extend(['console', 'pan'])

# Print the contents of each box
print_box(0)
print_box(1)
print_box(2)
print_box(3)
print_box(4)
print_box(5)
print_box(6)
print_box(7)
print_box(8)
print_box(9)
print_box(10)
print_box(11)
print_box(12)
print_box(13)
print_box(14)