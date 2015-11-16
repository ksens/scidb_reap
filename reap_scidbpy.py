#!python
# This is a script to delete the arrays left over by a badly terminated SciDB-py session 
# when there can be hundreds of arrays like:
# {12} 'py1100961778328_00046',32128,32128,'py1100961778328_00046<No:int64,name:string,uaid:int64,aid:int64,schema:string,availability:bool,temporary:bool> [idx=0:*,1000000,0]',true,false
# {13} 'py1100963282158_00003',32130,32130,'py1100963282158_00003<No:int64,name:string,library:string> [idx=0:*,64,0]',true,false
# {14} 'py1100963282158_00008',32132,32132,'py1100963282158_00008<No:int64,name:string,type:string> [idx=0:*,17,0]',true,false
# {15} 'py1100963282158_00013',32134,32134,'py1100963282158_00013<No:int64,name:string,uaid:int64,aid:int64,schema:string,availability:bool,temporary:bool> [idx=0:*,1000000,0]',true,false

# use with caution: array names matching 'py*_*' will be deleted
# target is to delete arrays like 'py1100961778328_00046'
# but arrays like 'pyous_papa' will also be deleted!!

# hence better to test stuff with a print statement first
import pandas as pd
from scidbpy import connect
sdb = connect()
list = sdb.list_arrays()
df = pd.DataFrame(list.items(), columns=['name', 'schema'])
pydf = df[df.name.str.match('py.*_.*')] # use with caution: array names matching 'py*_*' will be deleted
                                        
                                       
for pyname in pydf['name']:
  print "remove(%s)" % pyname         # better to test stuff with a print statement first
  #sdb.query("remove(%s)" % pyname)
    
sdb.reap()
