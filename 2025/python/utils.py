def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
        lines = data.split('\n')
    return lines
