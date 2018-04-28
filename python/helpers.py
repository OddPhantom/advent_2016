
def read_file(filename):

    data = []
    expected_answer = None

    with file(filename) as fp:
        for l in fp:
            if l != '\n':
                l = l
                data.append(l.strip())
            else:
                break

    return data
