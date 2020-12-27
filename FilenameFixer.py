#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

__author__ = "Jonathan N. Winters"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.6"
__maintainer__ = "Jonathan N. Winters"
__email__ = "jnw25@cornell.edu"
__status__ = "Work in progress."

import os
import argparse
from datetime import datetime

total_changes = 0
num_dirs = 0


#parse arguments
parser = argparse.ArgumentParser(prog='FilenameFixer')
parser = argparse.ArgumentParser(description='Replaces given chars in all filenames contained within a given directory. NOTE: This program does not yet correct directory names.')
parser.add_argument( 'path',  help='Specify path to directory.')
parser.add_argument( 'current_character', help='Character to convert from.')
parser.add_argument( 'new_character', help='Character to convert to.')

parser.add_argument('--version', action='version', version='%(prog)s 0.6')
parser.add_argument( '-r', '--recursive', action='store_true', help='Applies the specified character substitution recursively to the file hierarcy rooted at the given path')
parser.add_argument( '-n', '--dry-run', action='store_true', help='show what would have been renamed')
parser.add_argument( '-v', '--verbose', action='store_true', help='Causes FilenameFixer to be verbose, showing full file path as they are changed.')
parser.add_argument( '-l', '--log', help='Specify path to write log file.')
parser.add_argument( '-c', '--copy', help='FEATURE NOT YET DEVELOPED: Copies the entire directory structure and contained files to specified locations, replacing the specified character in each file path.')
parser.add_argument('--analyze', help='FEATURE NOT YET DEVELOPED: Search for potential problem file and directory names.')
parser.add_argument('--dirs-only', help='FEATURE NOT YET DEVELOPED: Replaces given character in directory paths only.')
parser.add_argument('--files-only', help='FEATURE NOT YET DEVELOPED: Replaces given character in file names only and does not modify directories.')




def char_replace(file_list,char_from,char_to, verbose, dry_run):
    '''iterates through list of absolute file paths and renames any files found matching the specified from/to pair'''
    
    #create new log of files that has pairs of src/dst paths
    log_list = []

    # for each path in the file_list, change the filename from char to char
    for original_absolute_path in file_list:
   
        filename = original_absolute_path.split("/")[-1]
        folder = original_absolute_path[0:len(original_absolute_path)-len(filename)]

        #perform move
        has_special_char = (filename.find(char_from) > 0)
        new_filename = filename.replace(char_from, char_to) 
        new_absolute_path = folder + new_filename
        if has_special_char:
            if not dry_run:
                # CHECK PERMISSIONS
                # IF PERMISSIONS PERFORM MOVE Otherwise break?
                os.replace(original_absolute_path,new_absolute_path)
                #CONFIRM MOVE
   
            log_line_original = "Original: " + original_absolute_path
            log_list.append(log_line_original)
            log_line_new= "     New: " + new_absolute_path
            log_list.append(log_line_new)
            log_line_blank = ""
            log_list.append(log_line_blank)

            if verbose:
                print(log_line_original)
                print(log_line_new)
                print(log_line_blank)
                
    return log_list
            

def create_file_list(path,recursive):
    file_list = []
    if recursive:
        for path, dirs, files in os.walk(path):
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
    '''FUNCTION NOT YET PROGRAMMED: Duplicate files made with the character replaced. Original Files untouched.'''
    #http://techs.studyhorror.com/d/python-how-to-copy-and-rename-files
    
    return 0
    
 

def main():    
    args = parser.parse_args()

    print("")
    print("")
    
    file_list = create_file_list(args.path,args.recursive)
    special_character_count = count_num_files_with_special_char(file_list,args.current_character)
    log_list = []

    log_from_char_replace = char_replace(file_list, args.current_character, args.new_character, args.verbose, args.dry_run) 
    
    # get current date and time
    now = datetime.now()
    date_string = now.strftime("%B %d, %Y %H:%M:%S")

    # first line of log will be the executable name + run + date
    log_line = '{}'.format(parser.prog)+ " run  " + date_string
    print(log_line)
    log_list.append(log_line)
    
    # show what the from/to characters will be
    log_line = "Replace [ " + args.current_character + " ] with [ " +args.new_character +" ]" + " in directory [" + args.path + "]"
    print(log_line)
    log_list.append(log_line)

    # displays count of filenames that contain the specified from char
    log_line = str(special_character_count) + "\tfiles containing [ " + args.current_character + " ]" 
    print(log_line)
    log_list.append(log_line)

    # displays count of all files searched
    log_line = str(len(file_list)) + "\ttotal files searched"
    print(log_line)
    log_list.append(log_line)


    # notify if dry run
    if args.dry_run:
        log_line = "This is a dry-run only. No changes have actually been made."
        log_list.append(log_line)
        print(log_line)

    # add two blank lines
    log_list.append("")
    log_list.append("")

    log_list = log_list + log_from_char_replace

    
    log_file_name = now.strftime("%Y%m%d%H%M%S-" + '{}'.format(parser.prog) )

    #if logs are enabled then write the log list to file at specified path
    if(args.log):
        # if directory path does not exist, create directory
        if not os.path.exists(args.log + "/FileFixerLogs"):
            os.makedirs(args.log + "/FileFixerLogs")    
        #create the log file by writing each line of the log_list        
        f = open(str(args.log) + "/FileFixerLogs/" + log_file_name + ".log" , "w" )
        for log_line in log_list:
            f.write(log_line + "\r\n")
        f.close
        # Test to see if file has been created, if so print confirmation
        print("Log file created: " + str(args.log) + "/" + log_file_name + ".log")

        ########## IMPORTANT HOW TO HNDLE DETECION OF TRAILING / in path and also conver on WINDOWS

main()



