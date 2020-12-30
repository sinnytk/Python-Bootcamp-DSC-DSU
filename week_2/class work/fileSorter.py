import os
import shutil
curentDir = input('Enter the Path:')
extensions = ['pdf','deb','jpg','txt','tar','mp4','png','mp3','sh']

for folder, subfolders, filenames in os.walk(curentDir):

    # Avoid these Folders
    subfolders[:] = [subfolder for subfolder in subfolders for i in extensions if subfolder!= i]
    
    #rint(f'the current working folder is: {folder}')
    
    # Itrate over all the files in the curent folder
    for filename in filenames:        
        
        # Extract the file extension from filename
        fileExt = (filename.split('.'))[1:2]
        print(fileExt)

        for i in range(len(extensions)):

            # # Move file to directory
            # def moveF(dirt):
            #     shutil.move((curentDir+'/'+filename),(curentDir+"/"+extensions[i]+'/'+filename))
            

            # Check the file with every possible extension
            if fileExt[0] == extensions[i]:
                
                #Creates the Directory path based on the Extension
                dirt = os.path.join(curentDir, extensions[i])
                
                # Check if the directory is already created
                if os.path.isdir(dirt):
                    #Just Moved the file to the directory
                    print(f'this {filename} file is moved')
                    shutil.move((curentDir+'/'+filename),(curentDir+"/"+extensions[i]+'/'+filename))
                else:
                    # First Create the Directory
                    os.mkdir(dirt)
                    # then move the file
                    print(f'this {filename} file is move')
                    shutil.move((curentDir+'/'+filename),(curentDir+"/"+extensions[i]+'/'+filename))
            
            else:
                #Make Directory for other files
                dirt = os.path.join(curentDir, 'Others')
                os.mkdir(dirt)
                # then move the file
                print(f'this {filename} file is moved')
                shutil.move((curentDir+'/'+filename),(curentDir+"/"+extensions[i]+'/'+filename))