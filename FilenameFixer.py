#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

__author__ = "Jonathan N. Winters"
__copyright__ = "Copyright 2020
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.2"
__maintainer__ = "Jonathan N. Winters"
__email__ = "jnw25@cornell.edu"
__status__ = "Work in progress."

import os
import argparse

total_changes = 0
num_dirs = 0


#parse arguments
parser = argparse.ArgumentParser(prog='FilenameFixer')
parser = argparse.ArgumentParser(description='Replaces given chars in all filenames contained within a given directory. NOTE: This program does not yet correct directory names.')
parser.add_argument( 'path',  help='Specify path to directory.')
parser.add_argument( 'current_character', help='Character to convert from.')
parser.add_argument( 'new_character', help='Character to convert to.')

parser.add_argument('--version', action='version', version='%(prog)s 0.2')
parser.add_argument( '-r', '--recursive', action='store_true', help='Applies the specified character substitution recursively to the file hierarcy rooted at the given path')
parser.add_argument( '-v', '--verbose', action='store_true', help='Causes FilenameFixer to be verbose, showing full file path as they are changed.')
parser.add_argument( '-l', '--log', help='Specify path to write log file.')
parser.add_argument( '-c', '--copy', help='FEATURE NOT YET DEVELOPED: Copies the entire directory structure and contained files to specified locations, replacing the specified character in each file path.')
parser.add_argument('--analyze', help='FEATURE NOT YET DEVELOPED: Search for potential problem file and directory names.')
parser.add_argument('--dirs-only', help='FEATURE NOT YET DEVELOPED: Replaces given character in directory paths only.')
parser.add_argument('--files-only', help='FEATURE NOT YET DEVELOPED: Replaces given character in file names only and does not modify directories.')




def char_replace(file_list,char_from,char_to, verbose):
    #create new LIST of files that has pairs of src/dst paths
    #os.rename(src, dst)
    for original_absolute_path in file_list:
       
        filename = original_absolute_path.split("/")[-1]
        folder = original_absolute_path[0:len(original_absolute_path)-len(filename)]

        #perform move
        has_special_char = (filename.find(char_from) > 0)
        new_filename = filename.replace(char_from, char_to) 
        new_absolute_path = folder + new_filename
        os.replace(original_absolute_path,new_absolute_path)
        if verbose and has_special_char:
            print(original_absolute_path)
            print(new_absolute_path)
   
            

def create_file_list(path,recursive):
    file_list = []
    if recursive:
        for path, dirs, files in os.walk(path):
            #print(os.path.join(path,dirs))
            for filename in files:
                full_path = os.path.join(path,filename)
                file_list.append(full_path)
    else: #not recursive
        path, dirs, files = next(os.walk(path))
        for filename in files:
            full_path = os.path.join(path,filename)
            file_list.append(full_path)
            
    return file_list
    
              
def count_num_files_with_special_char(file_list,character):
    count = 0
    for f in file_list:
        filename = f.split("/")[-1]
        if filename.find(character) > 0:
            count += 1
    
    return count
    

def copy_and_rename():
    #http://techs.studyhorror.com/d/python-how-to-copy-and-rename-files
    
    return 0
    
 

def main():    
    args = parser.parse_args()
    print("Search path = " + args.path)
    print("Swapping " + args.current_character + " with " +args.new_character)

    print(str(args.copy) + " is the new path") # do so preserving time stamps?
   
    file_list = create_file_list(args.path,args.recursive)
    special_character_count = count_num_files_with_special_char(file_list,args.current_character)
    print(str(special_character_count) + "\tfiles containing [" + args.current_character + "]" )

    char_replace(file_list, args.current_character, args.new_character, args.verbose)
    print(str(len(file_list)) + "\ttotal files searched")
   
    


main()



