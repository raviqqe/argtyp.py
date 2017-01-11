def _identity(x):
    return x


def text_file(filename):
    """
    >>> text_file('test/foo.txt')
    'foo\\nbar\\n'
    """
    with open(filename) as file:
        return file.read()


def file_lines(filename):
    """
    >>> file_lines('test/foo.txt')
    ['foo', 'bar']
     """
    return text_file(filename).split()


def csv(string, type=_identity):
    """
    >>> csv('foo, bar,baz')
    ['foo', 'bar', 'baz']
    """
    return [type(x.strip()) for x in string.split(',')]


def str_list(string):
    """
    >>> string = 'foo, bar,baz'
    >>> assert str_list(string) == csv(string)
    """
    return csv(string, str)


def int_list(string):
    """
    >>> int_list("123,456")
    [123, 456]
    """
    return csv(string, int)


def float_list(string):
    """
    >>> float_list("123,456")
    [123.0, 456.0]
    """
    return csv(string, float)


def csv_file(filename):
    """
    >>> csv_file('test/foo.csv')
    [['1', '2', '3'], ['4', '5', '6']]
    """
    return [line.split(',') for line in file_lines(filename)]


def int_csv_file(filename):
    """
    >>> int_csv_file('test/foo.csv')
    [[1, 2, 3], [4, 5, 6]]
    """
    return [[int(n) for n in record] for record in csv_file(filename)]


def float_csv_file(filename):
    """
    >>> float_csv_file('test/foo.csv')
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    """
    return [[float(n) for n in record] for record in csv_file(filename)]
