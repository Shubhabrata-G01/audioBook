

def book_to_list(txtbook):

    lst = []
    file = open(txtbook, 'r')

    txt = file.read().split('. ')

    for line in txt:
        lst.append(repr(line).strip("'"))

    return lst
