box_0 = ['beach', 'plane']
box_1 = ['meteor', 'wire', 'forest', 'sculpture', 'sandals']
box_2 = []
box_3 = []
box_4 = ['pants', 'frame', 'sun']
box_5 = ['scarf', 'thunder', 'dice']
box_6 = ['microscope', 'blanket', 'harmonica']
box_7 = ['swimsuit', 'seaweed']
box_8 = ['makeup']
box_9 = ['boot', 'moon', 'cup', 'train', 'gloves']
box_10 = ['belt']
box_11 = ['toothpaste', 'keyboard']
box_12 = ['earring', 'butterfly', 'headphone', 'candle', 'bag']

# Swap the makeup in Box 8 with the moon in Box 9
box_8, box_9 = box_9, box_8

# Remove the harmonica from Box 6
box_6.remove('harmonica')

# Put the fish into Box 10
box_10.append('fish')

# Replace the blanket with the lightning in Box 6
box_6.remove('blanket')
box_6.append('lightning')

# Replace the seaweed with the swimsuit in Box 7
box_7.remove('seaweed')
box_7.append('swimsuit')

# Put the ocean and the glasses and the thread into Box 6
box_6.extend(['ocean', 'glasses', 'thread'])

# Move the pants from Box 4 to Box 6
box_4.remove('pants')
box_6.append('pants')

# Move the keyboard from Box 11 to Box 3
box_11.remove('keyboard')
box_3.append('keyboard')

# Put the shorts and the game and the comb into Box 0
box_0.extend(['shorts', 'game', 'comb'])

# Swap the keyboard in Box 3 with the swimsuit in Box 7
box_3, box_7 = box_7, box_3

# Swap the comb in Box 0 with the frame in Box 4
box_0.remove('comb')
box_4.remove('frame')
box_0.append('frame')
box_4.append('comb')

# Put the fish and the jungle and the umbrella into Box 12
box_12.extend(['fish', 'jungle', 'umbrella'])

# Put the shorts and the drum into Box 9
box_9.extend(['shorts', 'drum'])

# Swap the candle in Box 12 with the swimsuit in Box 3
box_12.remove('candle')
box_3.remove('swimsuit')
box_12.append('swimsuit')
box_3.append('candle')

# Remove the game and the shorts and the beach from Box 0
box_0.remove('game')
box_0.remove('shorts')
box_0.remove('beach')

# Move the dice and the scarf and the thunder from Box 5 to Box 11
box_5.remove('dice')
box_5.remove('scarf')
box_5.remove('thunder')
box_11.extend(['dice', 'scarf', 'thunder'])

# Remove the shorts and the cup and the boot from Box 9
box_9.remove('shorts')
box_9.remove('cup')
box_9.remove('boot')

# Swap the keyboard in Box 7 with the makeup in Box 9
box_7, box_9 = box_9, box_7

# Replace the sculpture with the microwave in Box 1
box_1.remove('sculpture')
box_1.append('microwave')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)