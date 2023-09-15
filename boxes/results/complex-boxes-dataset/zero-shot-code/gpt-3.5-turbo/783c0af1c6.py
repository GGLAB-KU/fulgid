box_0 = []
box_1 = ['ship', 'note', 'butterfly', 'bear', 'dice']
box_2 = ['controller', 'flute']
box_3 = ['mask', 'doll', 'candle']
box_4 = ['jacket', 'river', 'swimsuit', 'helmet']
box_5 = ['cup', 'razor', 'dolphin']

# Swap ship in Box 1 with controller in Box 2
box_1.remove('ship')
box_2.remove('controller')
box_1.append('controller')
box_2.append('ship')

# Put toy into Box 4
box_4.append('toy')

# Replace note with puzzle in Box 1
box_1.remove('note')
box_1.append('puzzle')

# Move bear, dice, and controller from Box 1 to Box 4
box_1.remove('bear')
box_1.remove('dice')
box_1.remove('controller')
box_4.append('bear')
box_4.append('dice')
box_4.append('controller')

# Put lion and key into Box 0
box_0.append('lion')
box_0.append('key')

# Put cow into Box 3
box_3.append('cow')

# Remove toy from Box 4
box_4.remove('toy')

# Empty Box 0
box_0 = []

# Swap butterfly in Box 1 with controller in Box 4
box_1.remove('butterfly')
box_4.remove('controller')
box_1.append('controller')
box_4.append('butterfly')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)