box_0 = []
box_1 = ['towel', 'candle', 'lock', 'jacket', 'lightning']
box_2 = ['doll', 'brush']
box_3 = ['blanket', 'violin', 'ring']
box_4 = []
box_5 = ['console', 'pen', 'button', 'train', 'shark']
box_6 = ['skirt', 'perfume', 'boat', 'pants', 'flute']
box_7 = ['rock', 'spoon', 'tape', 'shoes']
box_8 = ['whistle', 'elephant', 'puzzle', 'coin']
box_9 = ['dog', 'speaker', 'tiger']
box_10 = []
box_11 = ['bag', 'sculpture']
box_12 = []
box_13 = ['shelf', 'apple', 'motorcycle']
box_14 = ['submarine', 'makeup', 'grass', 'harmonica', 'wallet']

def print_box(box_name, box):
    print(f"Box {box_name}: {box}")

# Move the ring from Box 3 to Box 14
box_14.append(box_3.pop(box_3.index('ring')))
print_box(14, box_14)
print_box(3, box_3)

# Remove the brush from Box 2
box_2.remove('brush')
print_box(2, box_2)

# Move the pen and the shark from Box 5 to Box 14
box_14.extend([box_5.pop(box_5.index('pen')), box_5.pop(box_5.index('shark'))])
print_box(14, box_14)
print_box(5, box_5)

# Put the vase into Box 4
box_4.append('vase')
print_box(4, box_4)

# Empty Box 11
box_11.clear()
print_box(11, box_11)

# Put the pillow and the lock into Box 0
box_0.extend(['pillow', 'lock'])
print_box(0, box_0)

# Move the rock and the spoon and the tape from Box 7 to Box 11
box_11.extend([box_7.pop(box_7.index('rock')), box_7.pop(box_7.index('spoon')), box_7.pop(box_7.index('tape'))])
print_box(11, box_11)
print_box(7, box_7)

# Swap the train in Box 5 with the flute in Box 6
box_5[box_5.index('train')], box_6[box_6.index('flute')] = box_6[box_6.index('flute')], box_5[box_5.index('train')]
print_box(5, box_5)
print_box(6, box_6)

# Replace the vase with the bell in Box 4
box_4[box_4.index('vase')] = 'bell'
print_box(4, box_4)

# Move the coin from Box 8 to Box 3
box_3.append(box_8.pop(box_8.index('coin')))
print_box(3, box_3)
print_box(8, box_8)

# Move the bell from Box 4 to Box 9
box_9.append(box_4.pop(box_4.index('bell')))
print_box(9, box_9)
print_box(4, box_4)

# Remove the candle from Box 1
box_1.remove('candle')
print_box(1, box_1)

# Move the shelf and the apple and the motorcycle from Box 13 to Box 14
box_14.extend([box_13.pop(box_13.index('shelf')), box_13.pop(box_13.index('apple')), box_13.pop(box_13.index('motorcycle'))])
print_box(14, box_14)
print_box(13, box_13)

# Replace the shoes with the lipstick in Box 7
box_7[box_7.index('shoes')] = 'lipstick'
print_box(7, box_7)

# Move the doll from Box 2 to Box 10
box_10.append(box_2.pop(box_2.index('doll')))
print_box(10, box_10)
print_box(2, box_2)

# Empty Box 14
box_14.clear()
print_box(14, box_14)

# Remove the console and the flute from Box 5
box_5.remove('console')
box_5.remove('flute')
print_box(5, box_5)

# Put the frame and the sock into Box 11
box_11.extend(['frame', 'sock'])
print_box(11, box_11)

# Move the elephant from Box 8 to Box 5
box_5.append(box_8.pop(box_8.index('elephant')))
print_box(5, box_5)
print_box(8, box_8)

# Replace the button and the elephant with the necklace and the keyboard in Box 5
box_5[box_5.index('button')] = 'necklace'
box_5[box_5.index('elephant')] = 'keyboard'
print_box(5, box_5)

# Swap the puzzle in Box 8 with the tiger in Box 9
box_8[box_8.index('puzzle')], box_9[box_9.index('tiger')] = box_9[box_9.index('tiger')], box_8[box_8.index('puzzle')]
print_box(8, box_8)
print_box(9, box_9)

# Replace the doll with the sculpture in Box 10
box_10[box_10.index('doll')] = 'sculpture'
print_box(10, box_10)