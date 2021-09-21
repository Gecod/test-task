def reverse_file(filename, new_filename):
    with open(filename, 'r') as f:
        data = f.read()
    
    f = open(new_filename, 'w')
    
    for i in range(len(data)):
        f.write(data[-1])
        data = data[:-1]
    
    f.write('\n')
    
    f.close()
    
    del data
    
    print('Content of ', filename)
    with open(filename, 'r') as f:
        print(f.read())
    
    print('')
    
    print('Content of ', new_filename)
    with open(new_filename, 'r') as f:
        print(f.read())


def reverse_lines(filename, new_filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    
    if data[-1][-2:] != '\n':
        data[-1] = data[-1] + '\n'
    
    f = open(new_filename, 'w')
    
    for i in range(len(data)):
        f.write(data.pop())
    
    f.close()
    
    del data
    
    print('Content of ', filename)
    with open(filename, 'r') as f:
        print(f.read())
    
    print('')
    
    print('Content of ', new_filename)
    with open(new_filename, 'r') as f:
        print(f.read())


if __name__ == '__main__':
    reverse_file('testfile.txt', 'new_testfile.txt')
    # reverse_lines('testfile.txt', 'new_testfile.txt')
