box_0 = ['crown', 'towel', 'umbrella', 'planet']
box_1 = ['toothbrush', 'rain']
box_2 = ['shorts', 'magnet', 'plane', 'comb', 'mountain']
box_3 = ['octopus', 'soap', 'meteor', 'sandals']
box_4 = ['horn', 'razor', 'glove']
box_5 = ['seaweed', 'wire', 'dog']
box_6 = ['fork']
box_7 = ['butterfly', 'perfume', 'speaker', 'motorcycle', 'note', 'book', 'sculpture', 'starfish', 'submarine', 'sun']
box_8 = ['coin', 'belt', 'jungle', 'shampoo']

def print_box(box_index, box_items):
    if len(box_items) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box_items}")

# Initial state
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)

# Perform operations
box_0.remove('towel')
box_0.remove('umbrella')
box_0.remove('planet')
box_7.remove('boat')
box_7.remove('jacket')
box_7.append('speaker')
box_7.append('motorcycle')
box_2.clear()
box_0.append('umbrella')
box_0.append('planet')
box_6.remove('note')
box_7.append('note')
box_6.remove('fork')
box_1.append('fork')
box_7.append('comet')
box_7.append('book')
box_7.append('sculpture')
box_7.append('starfish')
box_7.append('submarine')
box_7.append('sun')
box_3.append('meteor')
box_3.append('sandals')
box_4.remove('horn')
box_7.remove('book')
box_4.append('book')
box_8.remove('jungle')
box_4.remove('razor')
box_8.append('razor')
box_3.remove('meteor')
box_5.remove('wire')
box_5.append('meteor')
box_1.remove('rain')
box_4.remove('jungle')
box_0.append('towel')

# Final state
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)