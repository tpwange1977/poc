

def cau(type, n1, n2):
    
    if type == 1:
        a = n1 + n2
    elif type == 2:
        a = n1 - n2
    elif type == 3:
        a = n1    
    else:
        a = n1 * n2
    return a

if __name__ == '__main__':
    print('Call it locally')
    cau()