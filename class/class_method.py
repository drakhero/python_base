class A:
    v = 0

    @classmethod
    def get_v(cls):
        return cls.v

    @classmethod
    def set_v(cls,a):
        cls.v = a

print('A.v = ',A.get_v())
