box_0 = ['sandals', 'watch', 'frame', 'pot']
box_1 = ['microwave', 'bicycle', 'starfish']
box_2 = ['boot']
box_3 = []
box_4 = ['bracelet']
box_5 = ['grinder', 'camera', 'plane']
box_6 = ['tree', 'shoes', 'table', 'skirt']
box_7 = ['ship', 'ring', 'scarf', 'desert', 'jacket']
box_8 = ['helmet', 'controller']

# Move the helmet and the controller from Box 8 to Box 6
box_6.extend(box_8)
box_8.clear()

# Remove the desert and the ship and the scarf from Box 7
box_7.remove('desert')
box_7.remove('ship')
box_7.remove('scarf')

# Replace the bracelet with the gloves in Box 4
box_4.remove('bracelet')
box_4.append('gloves')

# Swap the pot in Box 0 with the plane in Box 5
box_0.remove('pot')
box_5.remove('plane')
box_0.append('plane')
box_5.append('pot')

# Put the fish into Box 5
box_5.append('fish')

# Move the grinder from Box 5 to Box 6
box_5.remove('grinder')
box_6.append('grinder')

# Remove the jacket from Box 7
box_7.remove('jacket')

# Empty Box 1
box_1.clear()

# Swap the gloves in Box 4 with the tree in Box 6
box_4.remove('gloves')
box_6.remove('tree')
box_4.append('tree')
box_6.append('gloves')

# Put the belt into Box 5
box_5.append('belt')

# Replace the watch and the plane and the sandals with the shirt and the gloves and the sock in Box 0
box_0.remove('watch')
box_0.remove('plane')
box_0.remove('sandals')
box_0.append('shirt')
box_0.append('gloves')
box_0.append('sock')

# Move the frame and the shirt from Box 0 to Box 6
box_0.remove('frame')
box_0.remove('shirt')
box_6.append('frame')
box_6.append('shirt')

# Replace the fish and the pot with the necklace and the wig in Box 5
box_5.remove('fish')
box_5.remove('pot')
box_5.append('necklace')
box_5.append('wig')

# Swap the sock in Box 0 with the ring in Box 7
box_0.remove('sock')
box_7.remove('ring')
box_0.append('ring')
box_7.append('sock')

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