box_0 = ['cup', 'leaf', 'phone']
box_1 = ['train', 'shirt', 'piano']
box_2 = ['comb']
box_3 = []
box_4 = []
box_5 = ['speaker']
box_6 = []
box_7 = ['headphone', 'skirt', 'flower']
box_8 = []
box_9 = ['basket']
box_10 = ['controller']
box_11 = []

# Replace the chair with the soap in Box 9
box_9.remove('basket')
box_9.append('soap')

# Swap the headphone in Box 7 with the flute in Box 8
box_7.remove('headphone')
box_7.append('flute')
box_8.remove('flute')
box_8.append('headphone')

# Swap the leaf in Box 0 with the scissors in Box 6
box_0.remove('leaf')
box_0.append('scissors')
box_6.remove('scissors')
box_6.append('leaf')

# Replace the book with the bicycle in Box 11
box_11.remove('book')
box_11.append('bicycle')

# Remove the razor from Box 8
box_8.remove('razor')

# Remove the leaf and the clock from Box 6
box_6.remove('leaf')
box_6.remove('clock')

# Replace the boat and the flute with the lock and the wallet in Box 7
box_7.remove('boat')
box_7.remove('flute')
box_7.append('lock')
box_7.append('wallet')

# Put the speaker into Box 5
box_5.append('speaker')

# Move the headphone from Box 8 to Box 1
box_8.remove('headphone')
box_1.append('headphone')

# Remove the bicycle from Box 11
box_11.remove('bicycle')

# Move the basket and the guitar and the soap from Box 9 to Box 3
box_9.remove('basket')
box_9.remove('soap')
box_9.remove('guitar')
box_3.append('basket')
box_3.append('soap')
box_3.append('guitar')

# Replace the toothpaste and the lock with the scissors and the guitar in Box 7
box_7.remove('toothpaste')
box_7.remove('lock')
box_7.append('scissors')
box_7.append('guitar')

# Move the basket from Box 3 to Box 7
box_3.remove('basket')
box_7.append('basket')

# Swap the soap in Box 3 with the truck in Box 10
box_3.remove('soap')
box_10.remove('truck')
box_3.append('truck')
box_10.append('soap')

# Replace the guitar and the truck with the grinder and the lightning in Box 3
box_3.remove('guitar')
box_3.remove('truck')
box_3.append('grinder')
box_3.append('lightning')

# Put the horn and the shoe into Box 2
box_2.append('horn')
box_2.append('shoe')

# Replace the grinder and the lightning with the note and the phone in Box 3
box_3.remove('grinder')
box_3.remove('lightning')
box_3.append('note')
box_3.append('phone')

# Remove the speaker and the shorts from Box 5
box_5.remove('speaker')
box_5.remove('shorts')

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