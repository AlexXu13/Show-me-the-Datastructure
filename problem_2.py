import os

def find_files(suffix, dirpath, findfiles=[]):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    assert dirpath!=None, "You should enter the path!"
    assert len(dirpath) != 0, "You should enter the path!"
    if not suffix:
        suffix = ""
    for filepath in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filepath)
        if os.path.isdir(filepath):
            files = find_files(suffix,filepath, findfiles)
        elif os.path.isfile(filepath) and filepath.endswith(suffix):
            findfiles.append(filepath)
    return findfiles

#print(find_files('.c','./testdir'))
#print(find_files(None,'./testdir'))
#print(find_files('.c',None))
print(find_files('.c',''))

