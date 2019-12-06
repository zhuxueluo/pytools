#! encoding utf8
import os
import hashlib
import sys
import shutil

def hashfile(fp):
    try:
        f = open(fp,'rb')
    except:
        print('open file='+fp+' except')
    md5tool=hashlib.md5()
    while True:
        buf=f.read(4096)
        if not buf:
            break
        md5tool.update(buf)
    hash_code = md5tool.hexdigest()
    f.close()
    return hash_code

globalset={}
# absolute path
def distinct_copy(fromdir, dstdir, recursive):
    '''
    guide line
    '''
    print(fromdir)
    listitem = os.listdir(fromdir)
    for item in listitem:
        itempath = fromdir+os.path.sep+item
        if os.path.isfile(itempath):
            md5sum = hashfile(itempath)
            if globalset.has_key(md5sum):
                print('omit '+itempath+" for "+globalset.get(md5sum))
            else:
                targetFile = dstdir+os.path.sep+os.path.basename(itempath)
                newTargetFile = targetFile if not os.path.exists(targetFile) else targetFile+"."+md5sum
                shutil.copyfile(itempath, newTargetFile)
                globalset[md5sum]=itempath
        elif recursive=='True':
            distinct_copy(itempath, dstdir, 'True')
        else:
            print('skip dir '+ itempath)

if __name__ == '__main__':
    print('args are:'+ str(sys.argv))
    ''' test hashfile
    if len(sys.argv) < 2:
        print('input file to get md5')
        sys.exit(1)
    print(hashfile(sys.argv[1]))
    '''
    # test distinct_copy
    if len(sys.argv) < 4:
        print('args: srcdir dstdir recursive')
        sys.exit(1)
    distinct_copy(sys.argv[1], sys.argv[2], sys.argv[3])
