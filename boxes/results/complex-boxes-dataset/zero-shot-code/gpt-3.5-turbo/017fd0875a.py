box_0 = ['pot', 'pan', 'microscope', 'car', 'bird']
box_1 = ['note', 'starfish', 'camera', 'chair']
box_2 = ['necklace', 'swimsuit', 'doll', 'wallet', 'polish']
box_3 = []
box_4 = ['motorcycle', 'razor']
box_5 = ['bowl']
box_6 = ['bus']
box_7 = ['wire']

# Replace the pot and the bird with the glove and the blender in Box 0
box_0.remove('pot')
box_0.remove('bird')
box_0.append('glove')
box_0.append('blender')

# Swap the razor in Box 4 with the bus in Box 6
box_4.remove('razor')
box_6.remove('bus')
box_4.append('bus')
box_6.append('razor')

# Replace the motorcycle and the bus with the tiger and the plane in Box 4
box_4.remove('motorcycle')
box_4.remove('bus')
box_4.append('tiger')
box_4.append('plane')

# Put the chair and the meteor and the speaker into Box 4
box_4.append('chair')
box_4.append('meteor')
box_4.append('speaker')

# Put the glove into Box 0
box_0.append('glove')

# Put the lion and the horse into Box 3
box_3.append('lion')
box_3.append('horse')

# Remove the meteor and the plane from Box 4
box_4.remove('meteor')
box_4.remove('plane')

# Replace the bowl with the makeup in Box 5
box_5.remove('bowl')
box_5.append('makeup')

# Swap the lion in Box 3 with the polish in Box 2
box_3.remove('lion')
box_2.remove('polish')
box_3.append('polish')
box_2.append('lion')

# Swap the horse in Box 3 with the razor in Box 6
box_3.remove('horse')
box_6.remove('razor')
box_3.append('razor')
box_6.append('horse')

# Swap the horse in Box 6 with the starfish in Box 1
box_6.remove('horse')
box_1.remove('starfish')
box_6.append('starfish')
box_1.append('horse')

# Swap the makeup in Box 5 with the wire in Box 7
box_5.remove('makeup')
box_7.remove('wire')
box_5.append('wire')
box_7.append('makeup')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)