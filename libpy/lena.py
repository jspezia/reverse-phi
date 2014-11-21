def lena():
    import pickle
    from numpy import array
    from os import path
    fname = path.join(path.dirname(__file__),'lena.dat')
    f = open(fname,'rb')
    lena = array(pickle.load(f))
    f.close()
    return lena
