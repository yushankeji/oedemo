#-*- coding:utf-8 -*-

def add(a,b):
    ''' 这个函数是验证加法
        >>> add(1,1)
        2
        >>> add(1,-1)
        1
    '''
    return a+b

if __name__ == '__main__' :
    import doctest
    doctest.testmod(name='add')
    