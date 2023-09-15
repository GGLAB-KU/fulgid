box_0 = ['console']
box_1 = ['starfish', 'hat', 'bicycle']
box_2 = []
box_3 = ['comb', 'candle', 'perfume', 'star']
box_4 = ['makeup', 'desert', 'puzzle', 'apple', 'cat']
box_5 = []
box_6 = ['crown', 'meteor', 'dice']
box_7 = ['keyboard', 'telescope', 'dress', 'mirror', 'guitar']
box_8 = ['shark', 'doll', 'bowl', 'shirt', 'earring']
box_9 = ['piano', 'car']
box_10 = ['ring', 'shorts', 'bear']

def print_box(box_index, box):
    if len(box) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box}")

# Put the mixer into Box 2
box_2.append('mixer')
print_box(2, box_2)

# Empty Box 6
box_6.clear()
print_box(6, box_6)

# Replace the makeup with the brush in Box 4
box_4.remove('makeup')
box_4.append('brush')
print_box(4, box_4)

# Swap the desert in Box 4 with the guitar in Box 7
box_4.remove('desert')
box_7.remove('guitar')
box_4.append('guitar')
box_7.append('desert')
print_box(4, box_4)
print_box(7, box_7)

# Swap the console in Box 0 with the starfish in Box 1
box_0.remove('console')
box_1.remove('starfish')
box_0.append('starfish')
box_1.append('console')
print_box(0, box_0)
print_box(1, box_1)

# Move the mixer from Box 2 to Box 1
box_2.remove('mixer')
box_1.append('mixer')
print_box(1, box_1)

# Replace the keyboard with the ring in Box 7
box_7.remove('keyboard')
box_7.append('ring')
print_box(7, box_7)

# Move the puzzle and the guitar from Box 4 to Box 9
box_4.remove('puzzle')
box_4.remove('guitar')
box_9.append('puzzle')
box_9.append('guitar')
print_box(4, box_4)
print_box(9, box_9)

# Move the brush and the cat from Box 4 to Box 6
box_4.remove('brush')
box_4.remove('cat')
box_6.append('brush')
box_6.append('cat')
print_box(4, box_4)
print_box(6, box_6)

# Remove the brush from Box 6
box_6.remove('brush')
print_box(6, box_6)

# Replace the candle with the sun in Box 3
box_3.remove('candle')
box_3.append('sun')
print_box(3, box_3)

# Remove the dress and the desert and the telescope from Box 7
box_7.remove('dress')
box_7.remove('desert')
box_7.remove('telescope')
print_box(7, box_7)

# Move the starfish from Box 0 to Box 7
box_0.remove('starfish')
box_7.append('starfish')
print_box(0, box_0)
print_box(7, box_7)

# Move the star from Box 3 to Box 10
box_3.remove('star')
box_10.append('star')
print_box(3, box_3)
print_box(10, box_10)

# Replace the starfish and the ring with the headphone and the cow in Box 7
box_7.remove('starfish')
box_7.remove('ring')
box_7.append('headphone')
box_7.append('cow')
print_box(7, box_7)

# Move the ring and the star and the bear from Box 10 to Box 1
box_10.remove('ring')
box_10.remove('star')
box_10.remove('bear')
box_1.append('ring')
box_1.append('star')
box_1.append('bear')
print_box(10, box_10)
print_box(1, box_1)

# Empty Box 7
box_7.clear()
print_box(7, box_7)