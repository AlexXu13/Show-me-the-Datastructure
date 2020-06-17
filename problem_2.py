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
    if dirpath == None:
        return "Path format is wrong!"
    if len(dirpath) == 0:
        return "Path format is wrong!"
    if not suffix:
        suffix = ""
    for filepath in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filepath)
        if os.path.isdir(filepath):
            files = find_files(suffix,filepath, findfiles)
        elif os.path.isfile(filepath) and filepath.endswith(suffix):
            findfiles.append(filepath)
    return findfiles

print(find_files('.c','./testdir')) #return .c files
print(find_files(None,'./testdir')) #return all files
print(find_files('.c',None)) #return attention
print(find_files('.c','')) #return attention

