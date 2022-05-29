from ast import literal_eval

def create_new_pin(name, author_id, list_categories, latitude, longitude, description):
    id = -1
    with open('src/data/places.tsv', mode='r') as f:
        for line in f:
            id += 1
    categories = [[1*x]*2 for x in list_categories]
    pin = f"\n{id}\t{name}\t{author_id}\t{categories}\t{latitude}\t{longitude}\t{description}"
    with open('src/data/places.tsv', mode='a') as f:
        f.write(pin)

def review_pin(id, category_id, is_positive):
    lines = ""
    with open('src/data/places.tsv', mode='r') as f:
        lines = f.readlines()
        id += 1
        if id < len(lines):
            values = lines[id].split('\t')
            categories = literal_eval(values[3])
            if category_id < len(categories):
                if is_positive:
                    categories[category_id][0] += 1
                categories[category_id][1] += 1
                values[3] = str(categories)
                lines[id] = '\t'.join(values)
    with open('src/data/places.tsv', mode='w') as f:
        f.writelines(lines)

def unreview_pin(id, category_id, was_positive):
    lines = ""
    with open('src/data/places.tsv', mode='r') as f:
        lines = f.readlines()
        id += 1
        if id < len(lines):
            values = lines[id].split('\t')
            categories = literal_eval(values[3])
            if category_id < len(categories):
                if was_positive:
                    categories[category_id][0] -= 1
                categories[category_id][1] -= 1
                values[3] = str(categories)
                lines[id] = '\t'.join(values)
    with open('src/data/places.tsv', mode='w') as f:
        f.writelines(lines)
    