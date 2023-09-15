box_0 = ['seaweed']
box_1 = ['puzzle']
box_2 = ['charger', 'jacket']
box_3 = ['telescope', 'grinder']
box_4 = ['ship', 'dice', 'river']
box_5 = ['usb', 'gloves', 'cow', 'key', 'tie']
box_6 = ['watch', 'fork']
box_7 = []
box_8 = ['jungle', 'island', 'toaster', 'rock']
box_9 = ['comet', 'towel', 'train']
box_10 = ['coin', 'glasses', 'lock', 'elephant', 'sun']
box_11 = []
box_12 = ['boat', 'speaker', 'rocket', 'octopus', 'tiger']
box_13 = []

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
    else:
        print("Invalid box index")

# Remove the octopus from Box 12
box_12.remove('octopus')

# Move the rocket from Box 12 to Box 13
box_13.append(box_12.pop(box_12.index('rocket')))

# Swap the jacket in Box 2 with the grinder in Box 3
box_2.remove('jacket')
box_3.remove('grinder')
box_2.append('grinder')
box_3.append('jacket')

# Move the seaweed from Box 0 to Box 13
box_13.append(box_0.pop(box_0.index('seaweed')))

# Swap the key in Box 5 with the grinder in Box 2
box_5.remove('key')
box_2.remove('grinder')
box_5.append('grinder')
box_2.append('key')

# Remove the telescope and the jacket from Box 3
box_3.remove('telescope')
box_3.remove('jacket')

# Swap the usb in Box 5 with the seaweed in Box 13
box_5.remove('usb')
box_13.remove('seaweed')
box_5.append('seaweed')
box_13.append('usb')

# Remove the train and the towel and the comet from Box 9
box_9.remove('train')
box_9.remove('towel')
box_9.remove('comet')

# Put the cow and the magnet and the desert into Box 3
box_3.append('cow')
box_3.append('magnet')
box_3.append('desert')

# Remove the watch from Box 6
box_6.remove('watch')

# Replace the fork with the tape in Box 6
box_6.remove('fork')
box_6.append('tape')

# Put the sandals and the lightning and the dog into Box 5
box_5.append('sandals')
box_5.append('lightning')
box_5.append('dog')

# Swap the usb in Box 13 with the desert in Box 3
box_13.remove('usb')
box_3.remove('desert')
box_13.append('desert')
box_3.append('usb')

# Replace the ship with the polish in Box 4
box_4.remove('ship')
box_4.append('polish')

# Remove the speaker from Box 12
box_12.remove('speaker')

# Put the tiger into Box 12
box_12.append('tiger')

# Move the cow and the magnet and the usb from Box 3 to Box 10
box_10.append(box_3.pop(box_3.index('cow')))
box_10.append(box_3.pop(box_3.index('magnet')))
box_10.append(box_3.pop(box_3.index('usb')))

# Replace the lightning and the seaweed and the gloves with the dog and the magnet and the butterfly in Box 5
box_5.remove('lightning')
box_5.remove('seaweed')
box_5.remove('gloves')
box_5.append('dog')
box_5.append('magnet')
box_5.append('butterfly')

# Remove the polish from Box 4
box_4.remove('polish')

# Remove the dice and the boat from Box 12
box_12.remove('dice')
box_12.remove('boat')

# Swap the jungle in Box 8 with the tiger in Box 12
box_8.remove('jungle')
box_12.remove('tiger')
box_8.append('tiger')
box_12.append('jungle')

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