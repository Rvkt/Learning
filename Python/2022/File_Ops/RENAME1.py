import os

path = input('Enter Path:\n')

str0 = input('Enter Year:\n')  

str1 = input('Enter Department:\n') 

str2 = input('Enter Post:\n') 

# str3 = from file name  CamelCase sep_


# r('str0_str1_str2_str3.ext')


# C:\Users\Dabba\Desktop\Cloud\Form\2022\2022_IBPS\Clerk

os.chdir(path)

files = os.listdir(path)


for file in files:

    name, ext = (os.path.splitext(file))
    # print(len(name))
    # print(name)
    splitted = name.split(' ')
    splitted = [s.strip() for s in splitted]
    # print(splitted)

    
    try:
        new_name = f'{str0}_{str1.upper()}_{str2.capitalize()}_{splitted[0].capitalize()}_{splitted[1].capitalize()}{ext}'
        # print(new_name)
        os.rename(file, new_name)
    except:
        pass









    # file_name = os.rename(name.sep('_'))
    # print(file_name)



