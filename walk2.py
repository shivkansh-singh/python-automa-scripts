import os                                                          
import time                                                        
import humanize                                                    
                                                                      
parent_path = input("Enter parent path to search in: ")            
                                                                      
def walking(parent_path):                                          
       print(f"Starting Directory walk on: {parent_path}")            
       children = os.listdir(parent_path)                             
       for child in children:                                         
          child_path = os.path.join(parent_path,child)               
          if os.path.isfile(child_path):                             
              child_data=os.stat(child_path)                         
              print(f"File: {child_path}")                           
              print(f"\tFile Size: {humanize.naturalsize(child_data.st_size)}")
              print(f"\tFile Creation Time: {time.ctime(child_data.st_ctime)}")
              print(f"\tFile Permissions: {oct(child_data.st_mode)[-3:]}")
              print("--------")                                      
          elif os.path.isdir(child_path):
              walking(child_path)
walking(parent_path)
