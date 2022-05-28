def create_new_pin():
    with open('filename', mode='a+') as f:
        id = len(f.readlines())
        