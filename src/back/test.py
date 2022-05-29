def create_new_pin(name, author_id, list, latitude, longitude, description):
    with open('filename', mode='a+') as f:
        id = len(f.readlines())
        