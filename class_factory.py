class Structure:

    _fields = []

    def __init__(self, *args):

        if len(args) != len(self._fields):
            raise TypeError('Expect {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Test(Structure):
    _fields = ['att1', 'att2', 'att3']


def main():

    t = Test(1, 2, 3)
    print(dir(t)[-3:])

if __name__ == '__main__':
    main()
