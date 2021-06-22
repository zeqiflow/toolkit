class Descriptor(object):

    def __init__(self, param1, name='param1'):
        self.param1 = param1
        self._name = name

    def __get__(self, obj, objtype):
        return self.param1

    def __set__(self, obj, value):
        # contrains defined here 
        '''
        if [contrains]:
            raise **Error('')
        '''
        self.param1 = value
