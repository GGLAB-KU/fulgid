def what_would_be_less_noticeable():
    items = {
        'dress': 'new_item',
        'hat': 'old_item'
    }

    for item, description in items.items():
        if description == 'old_item':
            return item

print(what_would_be_less_noticeable())  # This should print 'hat'