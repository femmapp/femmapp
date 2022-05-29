from test.back import pin_manager#, Search

def run(module):
    if hasattr(module, 'main'):
        module.main()

if __name__ == '__main__':
    run(pin_manager)
    #run(Search)