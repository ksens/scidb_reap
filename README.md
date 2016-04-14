# scidbpy_reap

## Shell command

First test with:
```
for name in $(iqlist_names | grep -e "py.*_.*" | awk '{print $2}' | cut -d "'" -f2) ; 
  do 
  echo $name; 
done
```

Then execute the removal by:
```
for name in $(iqlist_names | grep -e "py.*_.*" | awk '{print $2}' | cut -d "'" -f2) ; 
  do 
  echo $name; 
  iquery -aq "remove($name)" ; 
done
```

## Python script
This is a script to delete the arrays left over by a badly terminated SciDB-py session when there can be hundreds of arrays like:
```
{12} 'py1100961778328_00046',32128,32128,'py1100961778328_00046<No:int64,name:string,uaid:int64,aid:int64,schema:string,availability:bool,temporary:bool> [idx=0:*,1000000,0]',true,false
{13} 'py1100963282158_00003',32130,32130,'py1100963282158_00003<No:int64,name:string,library:string> [idx=0:*,64,0]',true,false
{14} 'py1100963282158_00008',32132,32132,'py1100963282158_00008<No:int64,name:string,type:string> [idx=0:*,17,0]',true,false
{15} 'py1100963282158_00013',32134,32134,'py1100963282158_00013<No:int64,name:string,uaid:int64,aid:int64,schema:string,availability:bool,temporary:bool> [idx=0:*,1000000,0]',true,false
```

## Use with caution

- array names matching `'py*_*'` will be deleted 
- target is to delete arrays like `'py1100961778328_00046'`
- but arrays like `'pyous_papa'` will also be deleted!!

Hence better to test stuff with a print statement first
