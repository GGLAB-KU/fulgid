def what_was_used_to_hold_papers():
    items = {
        'desks': 'place_to_take_tests',
        'pencils': 'tool_to_hold_papers'
    }

    for item, description in items.items():
        if description == 'tool_to_hold_papers':
            return item

print(what_was_used_to_hold_papers())  # This should print 'pencils'