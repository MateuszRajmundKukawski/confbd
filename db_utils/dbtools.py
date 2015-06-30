#from sqlalchemy.dialects.firebird.base import dialect
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, BLOB, MetaData, ForeignKey, update
# import codecs, os, re
# from sqlalchemy import func
# from sqlalchemy.dialects import firebird
# import tbclass



class DbTools(object):
    def __init__(self,db_file_path, password='masterkey', usr='SYSDBA' ):
            self.connection_string = ('firebird+fdb://{user}:{admin_pass}@localhost/{file_path}').format(user=usr,admin_pass=password,file_path=db_file_path)

            
    def db_connect(self):
        
        self.engine = create_engine(self.connection_string, echo=False)
        self.connection = self.engine.connect()          
            
            
if __name__ == '__main__':
    fpath = 'e:/mrk/05_TEMP/PESEL/1815012.fdb'
    x = DbTools(fpath,password='masterkey')
    x.db_connect()
    print x.connection_string