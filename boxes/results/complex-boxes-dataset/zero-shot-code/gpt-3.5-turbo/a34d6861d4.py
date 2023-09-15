box_0 = ['meteor', 'button', 'basket', 'headphone', 'phone']
box_1 = ['cup']
box_2 = ['camera', 'bicycle', 'coin', 'tape', 'lightning']
box_3 = ['console', 'magnet', 'lamp', 'grass', 'planet']
box_4 = ['rocket', 'shoe', 'skirt', 'puzzle']
box_5 = ['tiger', 'paint', 'shirt', 'belt']
box_6 = ['whistle']
box_7 = []
box_8 = ['game', 'flute', 'blender']

# Swap the lamp in Box 3 with the cup in Box 1
box_3.remove('lamp')
box_1.remove('cup')
box_3.append('cup')
box_1.append('lamp')

# Replace the lamp with the vase in Box 1
box_1.remove('lamp')
box_1.append('vase')

# Replace the basket and the button with the shirt and the needle in Box 0
box_0.remove('basket')
box_0.remove('button')
box_0.append('shirt')
box_0.append('needle')

# Remove the headphone and the needle and the meteor from Box 0
box_0.remove('headphone')
box_0.remove('needle')
box_0.remove('meteor')

# Remove the rocket from Box 4
box_4.remove('rocket')

# Swap the blender in Box 8 with the shirt in Box 0
box_8.remove('blender')
box_0.remove('shirt')
box_8.append('shirt')
box_0.append('blender')

# Remove the shoe and the puzzle from Box 4
box_4.remove('shoe')
box_4.remove('puzzle')

# Swap the whistle in Box 6 with the skirt in Box 4
box_6.remove('whistle')
box_4.remove('skirt')
box_6.append('skirt')
box_4.append('whistle')

# Move the camera from Box 2 to Box 0
box_2.remove('camera')
box_0.append('camera')

# Remove the tiger and the paint and the belt from Box 5
box_5.remove('tiger')
box_5.remove('paint')
box_5.remove('belt')

# Replace the skirt with the octopus in Box 6
box_6.remove('skirt')
box_6.append('octopus')

# Replace the game and the flute and the shirt with the towel and the wire and the snow in Box 8
box_8.remove('game')
box_8.remove('flute')
box_8.remove('shirt')
box_8.append('towel')
box_8.append('wire')
box_8.append('snow')

# Replace the planet and the magnet with the plate and the bell in Box 3
box_3.remove('planet')
box_3.remove('magnet')
box_3.append('plate')
box_3.append('bell')

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