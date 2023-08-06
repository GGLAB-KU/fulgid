def who_needed_to_get_to_the_doctor():
    people = {
        'Laura': 'used_too_much_super_glue',
        'Erin': 'had_hands_stuck_together'
    }

    for person, situation in people.items():
        if situation == 'had_hands_stuck_together':
            return person

print(who_needed_to_get_to_the_doctor())  # This should print 'Erin'