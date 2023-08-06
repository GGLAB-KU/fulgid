def what_was_not_available():
    payment_methods = {
        'cash': 'not_available',
        'card': 'available'
    }

    for method, availability in payment_methods.items():
        if availability == 'not_available':
            return method

print(what_was_not_available())  # This should print 'cash'