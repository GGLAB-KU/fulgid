box0 = ['tape', 'forest']
box1 = ['jungle', 'candle', 'wig', 'battery']
box2 = []
box3 = ['lightning', 'storm', 'lamp', 'rain']
box4 = ['octopus', 'cow', 'dice', 'helmet', 'mask']
box5 = ['blender', 'telescope', 'shorts', 'frame']

# Swap rain in Box 3 with candle in Box 1
box1.remove('candle')
box3.remove('rain')
box1.append('rain')
box3.append('candle')

# Put jacket, gloves, and tie into Box 5
box5.extend(['jacket', 'gloves', 'tie'])

# Empty Box 4
box4 = []

# Replace tie with beach in Box 5
box5.remove('tie')
box5.append('beach')

# Remove rain, jungle, and wig from Box 1
box1.remove('rain')
box1.remove('jungle')
box1.remove('wig')

# Replace tape with jungle in Box 0
box0.remove('tape')
box0.append('jungle')

# Swap storm in Box 3 with battery in Box 1
box1.remove('battery')
box3.remove('storm')
box1.append('storm')
box3.append('battery')

# Replace storm with glove in Box 1
box1.remove('storm')
box1.append('glove')

# Swap jungle in Box 0 with gloves in Box 5
box0.remove('jungle')
box5.remove('gloves')
box0.append('gloves')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)