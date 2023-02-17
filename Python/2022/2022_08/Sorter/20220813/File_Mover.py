import os
import shutil
import pathlib

print('Process may take awhile, please stand by...')

############################################################
#Place full destination of folder/destination you'd like sorted
#Paste it in between the quotes in the exact format of the example below
sourcepath= input('---->  Enter Path:\n')

############################################################
sourcefiles = os.listdir(sourcepath)
destinationpath = sourcepath

for file in sourcefiles:
    try:

# Image Files    
        if file.endswith('.png'):
            pathlib.Path(destinationpath +'/Images/Png').mkdir(parents=True, exist_ok=True) 
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Images/Png',file))

        if file.endswith('.jpeg'):
            pathlib.Path(destinationpath +'/Images/jpeg').mkdir(parents=True, exist_ok=True) 
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Images/jpeg',file))
        
        if file.endswith('.gif'):
            pathlib.Path(destinationpath +'/Images/gif').mkdir(parents=True, exist_ok=True) 
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Images/gif',file))
        
        if file.endswith('.jpg'):
            pathlib.Path(destinationpath +'/Images/jpg').mkdir(parents=True, exist_ok=True) 
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Images/jpg',file))
        
        if file.endswith('.webp'):
            pathlib.Path(destinationpath +'/Images/webp').mkdir(parents=True, exist_ok=True) 
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Images/webp',file))

        if file.endswith('.jfif'):
            pathlib.Path(destinationpath +'/Images/jfif').mkdir(parents=True, exist_ok=True) 
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Images/jfif',file))

        if file.endswith('.JPG'):
            pathlib.Path(destinationpath +'/Images/jpg').mkdir(parents=True, exist_ok=True) 
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Images/jpg',file))

# Video Files    
        elif file.endswith('.mp4'):
            pathlib.Path(destinationpath +'/Videos/mp4').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Videos/mp4',file))

        elif file.endswith('.avi'):
            pathlib.Path(destinationpath +'/Videos/avi').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Videos/avi',file))

        elif file.endswith('.mov'):
            pathlib.Path(destinationpath +'/Videos/mov').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Videos/mov',file))

# Design/Photoshop Files    
        elif file.endswith('.ai'):
            pathlib.Path(destinationpath +'/Adobe Projects').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Adobe Projects',file))
        
# Design/Photoshop Files    
        elif file.endswith('.psd'):
            pathlib.Path(destinationpath +'/Adobe Projects').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Adobe Projects',file))
        
        elif file.endswith('.aep'):
            pathlib.Path(destinationpath +'/Adobe Projects').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Adobe Projects',file))

# Archive Files    
        elif file.endswith('.zip'):
            pathlib.Path(destinationpath +'/Archive/zip').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Archive/zip',file))
        
        elif file.endswith('.rar'):
            pathlib.Path(destinationpath +'/Archive/rar').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Archive/rar',file))
        
        elif file.endswith('.7z'):
            pathlib.Path(destinationpath +'/Archive/7z').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Archive/7z',file))

# Software
        elif file.endswith('.exe'):
            pathlib.Path(destinationpath +'/SoftWare/Exe').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/SoftWare/Exe',file))

# Documents Files    
        elif file.endswith('.xlsx'):
            pathlib.Path(destinationpath +'/Documents/Excel').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Documents/Excel',file))

        elif file.endswith('.pptx')or file.endswith('.PPTM'):
            pathlib.Path(destinationpath +'/Documents/Presentation').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Documents/Presentation',file))

        elif file.endswith('.docx'):
            pathlib.Path(destinationpath +'/Documents/Docs').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Documents/Docs',file))

        elif file.endswith('.txt'):
            pathlib.Path(destinationpath +'/Documents/Txt').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Documents/Txt',file))

        elif file.endswith('.pdf')or file.endswith('.PDF'):  
            pathlib.Path(destinationpath +'/Documents/Pdf').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Documents/Pdf',file))

# Dev Files 
        elif file.endswith('.py'):
            pathlib.Path(destinationpath +'/Python').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Python',file))

# Audio Files    
        elif file.endswith('.mp3'):
            pathlib.Path(destinationpath +'/Music').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Music',file))

        elif os.path.isdir(sourcepath + file):
            if not file=='Folders'and not file=="Other" and not file=='Pictures'and not file=='Videos'and not file=='Adobe Projects'and not file=='MP3 FIles'and not file=='IPAs'and not file=='PDFs'and not file=='Text Files'and not file=='Microsoft Word'and not file=='Powerpoint'and not file=='Excel Files'and not file=='Executables':
                pathlib.Path(destinationpath +'Folders').mkdir(parents=True, exist_ok=True)
                shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Folders',file))
            else:
                print("No need to move " + file + " folder, ignore moved message")
        else:
            pathlib.Path(destinationpath +'/Other').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'/Other',file))

        print(file + " moved")
    except:
        print(file+" movement failed")