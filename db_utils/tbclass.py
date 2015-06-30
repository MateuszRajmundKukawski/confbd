from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class TableData(object):

    Base = declarative_base()
    '''def __init__(self):
       pass
   '''
        


    class Osoby(Base):
        __tablename__ = 'osoby'
        uid = Column(Integer, primary_key=True)
        plec = Column(String)
        psl = Column(String)
        pim = Column(String)
        dim = Column(String)
        nzw = Column(String)
        oim = Column(String)
        mim = Column(String)
        radr = Column(Integer,  ForeignKey('adresy.id'))

        def __init__(self,plec, psl , pim , dim , nzw , oim , mim , radr):
            self.plec = plec
            self.psl  = psl
            self.pim  = pim
            self.dim  = dim
            self.nzw  = nzw
            self.oim  = oim
            self.mim  = mim
            self.radr = radr
        def __repr__(self):
            return "%s %s: pesel: %s"%(self.pim, self.nzw, self.psl)

    class Adresy(Base):
        __tablename__ = 'adresy'
        uid = Column(Integer, primary_key=True)
        kod = Column(String)
        naz = Column(String)
        id = Column(Integer)
        nra = Column(String)

        def _init_(self, kod, naz, id, nra):
            self.kod = kod
            self.naz = naz
            self.id = id
            self.nra = nra
        def __repr__(self):
            return self.naz
print 'a jednak'