__version__ = 1.2

# EDA Utils
# Amazing quick
def expandtab(str,tab=8):
   return reduce(lambda a,b: 
                      a + ' '*(tab-len(a)%tab) + b,
                      str.split('\t')
                )
   
   
'''Support module for array and matrix use.

This module provides two classes that emulate one and two
dimentional lists with fixed sizes but mutable internals.'''


################################################################################

class Array:

    'Array(length[, value]) -> new array'

    def __init__(self, length, value=None):
        'x.__init__(...) initializes x'
        assert type(length) is int and length > 0
        self.__data = [value for index in range(length)]

    def __repr__(self):
        'x.__repr__() <==> repr(x)'
        return repr(self.__data)

    def __len__(self):
        'x.__len__() <==> len(x)'
        return len(self.__data)

    def __getitem__(self, index):
        'x.__getitem__(i) <==> x[i]'
        return self.__data[index]

    def __setitem__(self, index, value):
        'x.__setitem__(i, y) <==> x[i]=y'
        self.__data[index] = value

    def __delitem__(self, index):
        'x.__delitem__(i) <==> del x[i]'
        self.__data[index] = None

    def __iter__(self):
        'x.__iter__() <==> iter(x)'
        return iter(self.__data)

    def __contains__(self, value):
        'x.__contains__(y) <==> y in x'
        return value in self.__data

class Matrix:

    'Matrix(rows, columns[, value]) -> new matrix'

    def __init__(self, rows, columns, value=None):
        'x.__init__(...) initializes x'
        assert type(rows) is int and rows > 0
        self.__data = [Array(columns, value) for index in range(rows)]

    def __repr__(self):
        'x.__repr__() <==> repr(x)'
        return repr(self.__data)

    def __len__(self):
        'x.__len__() <==> len(x)'
        return len(self.__data)

    def __getitem__(self, index):
        'x.__getitem__(i) <==> x[i]'
        return self.__data[index]

    def __setitem__(self, index, value):
        'x.__setitem__(i, y) <==> x[i]=y'
        self.__data[index] = Array(len(self.__data[index]), value)

    def __delitem__(self, index):
        'x.__delitem__(i) <==> del x[i]'
        self.__data[index] = Array(len(self.__data[index]))

    def __iter__(self):
        'x.__iter__() <==> iter(x)'
        return iter(self.__data)

    def __contains__(self, value):
        'x.__contains__(y) <==> y in x'
        for item in self.__data:
            if value in item:
                return True
        return False
    


class CTypesList(object):
    "create a list for the given type, with optional initial preallocation space"
    def __init__(self, c_type, prealloc_size=0):
        self.c_type = c_type
        self._typesize = ctypes.sizeof(c_type)
        self.data = (c_type * prealloc_size)()
        self.size = 0
        self.prealloc_size = prealloc_size
    def __len__(self):
        return self.size
    def __getitem__(self, i):
        if i >= self.size:
            raise IndexError(i)
        if i < 0:
            i = self.size + i
            if i < 0:
                raise IndexError("list index out of range")
        return self.data[i]

    def __delitem__(self, i):
        size = self.size
        if i >= size:
            raise IndexError("list index out of range")
        
        if i < 0:
            i = size + i
            if i < 0:
                raise IndexError("list index out of range")

        # shift everything left by one
        address = ctypes.addressof(self.data)
        typesize = self._typesize
        to_address = address + i*typesize
        from_address = to_address + typesize
        ctypes.memmove(to_address, from_address, typesize*(size-i-1))

        self.size = size = size-1

        if self.prealloc_size > size*2:
            self.compact()

    def append(self, obj):
        "append to the list; the object must be assignable to the ctype"
        size = self.size
        if size >= self.prealloc_size:
            # Need to make new space.  There's no 'realloc' for
            # ctypes so this isn't as nice as it is in C.
            # I'm using Python's growth pattern, which is
            #    0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...
            if size < 9:
                newsize = (size>>3) + 3 + size
            else:
                newsize = (size>>3) + 6 + size
            newdata = (self.c_type * newsize)()
            ctypes.memmove(newdata, self.data, ctypes.sizeof(self.data))
            self.data = newdata
            self.prealloc_size = newsize
            
        self.data[size] = obj
        self.size = size+1
        
    def append_kwargs(self, **kwargs):
        "append to the list; assign each key/value to the new item"
        size = self.size
        if size >= self.prealloc_size:
            if size < 9:
                newsize = (size>>3) + 3 + size
            else:
                newsize = (size>>3) + 6 + size
            newdata = (self.c_type * newsize)()
            ctypes.memmove(newdata, self.data, ctypes.sizeof(self.data))
            self.data = newdata
            self.prealloc_size = newsize

        obj = self.data[size]
        for k, v in kwargs.iteritems():
            setattr(obj, k, v)
        self.size = size+1

    def pop(self):
        "remove the last item from the list"
        # Not handling anything other than pop from the end
        size = self.size
        if size == 0:
            raise IndexError("pop from empty list")

        if self.prealloc_size > self.size*2:
            # Too much empty space; compact.  Be careful;
            # can't dealloc the item I'm returning!
            self.compact()

        size -= 1
        obj = self.data[size]
        self.size = size
        return obj

    def compact(self):
        "remove any space preallocated for growth"
        if self.prealloc_size == self.size:
            return
        newdata = (self.c_type * self.size)()
        ctypes.memmove(newdata, self.data, self.size*self._typesize)
        self.data = newdata
        self.prealloc_size = self.size
        
        
if __name__ == "__main__":
    import unittest
    test_data = [1, 4, 9, 8, -1, -10, 5, 7, 12, 5, -2]
    TEST_LEN = len(test_data)
    class Range(ctypes.Structure):
        _fields_ = [ ("start", ctypes.c_int), ("end", ctypes.c_int) ]
    
    class CTypesListTest(unittest.TestCase):
        def _load(self):
            clist = CTypesList(ctypes.c_int)
            for x in test_data: clist.append(x)
            return clist
        def test_append(self):
            clist = self._load()
            for i, x in enumerate(test_data):
                self.assertEquals(clist[i], x)
        def test_append_pop(self):
            clist = self._load()
            for i, x in enumerate(test_data[::-1]):
                self.assertEquals(clist.pop(), x)
                self.assertEquals(len(clist), TEST_LEN-i-1)
            self.assertRaises(IndexError, clist.pop)
            self.assertRaises(IndexError, clist.pop)
        def test_len(self):
            clist = CTypesList(ctypes.c_int); self.assertEquals(len(clist), 0)
            for q in range(4):
                for i, x in enumerate(test_data[:5]):
                    clist.append(test_data[x])
                    self.assertEquals(len(clist), i+1)
                for i in range(4, -1, -1):
                    clist.pop()
                    self.assertEquals(len(clist), i)
        def test_getitem(self):
            import random
            clist = self._load(); indicies = range(TEST_LEN)
            for i in indicies:
                self.assertEquals(clist[i], test_data[i])
            for i in range(-1, -TEST_LEN-1, -1):
                self.assertEquals(clist[i], test_data[TEST_LEN+i])
            self.assertRaises(IndexError, lambda: clist[TEST_LEN])
            self.assertRaises(IndexError, lambda: clist[-TEST_LEN-1])
        def test_compact(self):
            clist = self._load()
            clist.compact(); clist.compact()
            clist.append(8); clist.compact(); clist.compact()
        def _cmp(self, clist, data):
            self.assertEquals(len(clist), len(data))
            for i in range(len(clist)):
                self.assertEquals(clist[i], data[i])
        def _del(self, i, clist, data):
            del clist[i]; del data[i]; self._cmp(clist, data)
        def test_delitem(self):
            clist = self._load(); data = test_data[:]; self._cmp(clist, test_data)
            self._del(1, clist, data)
            self._del(0, clist, data)
            self._del(-1, clist, data)
            self._del(-2, clist, data)
            self._del(len(clist)-1, clist, data)
            self.assertRaises(IndexError, lambda: clist.__delitem__(len(clist)))
            self.assertRaises(IndexError, lambda: clist.__delitem__(-len(clist)-1))
            while clist:
                del clist[0]
            clist.append(9); self._cmp(clist, [9])
        def test_structure(self):
            clist = CTypesList(Range, 5)
            self.assertEquals(len(clist), 0)
            clist.append_kwargs(start=4, end=9)
            self.assertEquals((clist[0].start, clist[0].end), (4,9))
            clist.append((2,3))
            self.assertEquals((clist[0].start, clist[0].end), (4,9))
            self.assertEquals((clist[1].start, clist[1].end), (2,3))

    unittest.main()

def caprefid():
    refid = "C" + "%d"% crefid
    return refid

def resrefid():
    refid = "R" + "%d"% rrefid
    return refid

def inch2sch(v):
    return v * 1000

# miliinch mil to pcb internal size
def mil2pcb(v):
    return v * 100

# milimiter to pcb internal size
def mm2pcb(v):
    return v * 3937.007874015748031496062992126
#    return v * 39.37007874015748031496062992126 * 100

