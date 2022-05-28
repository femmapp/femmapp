def create_new_pin(name, author_id, list_categories, latitude, longitude, description):
    id = -1
    with open('./src/data/places.tsv', mode='r') as f:
        for line in f:
            id += 1
    categories = [[1*x]*2 for x in list_categories]
    pin = f"\n{id}\t{name}\t{author_id}\t{categories}\t{latitude}\t{longitude}\t{description}"
    with open('./src/data/places.tsv', mode='a') as f:
        f.write(pin)
    