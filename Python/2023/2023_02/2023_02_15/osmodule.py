import os

# 1. os.name
# print(os.name)

# 2. get current directory
# print(os.getcwd())

# 3. listdir()
# print(os.listdir())

# 4. os.getlogin()
# print(os.getlogin())

# 5. os.getpid()
# print(os.getpid())

# 6. os.getuid()
# print(os.getuid())

# 7. mkdir()
# print(os.mkdir('test'))

# 8. rename()
# os.rename("OLD_NAME", "NEW_NAME" )

# 9. rmdir() Delete a directory
# os.rmdir("/home/sulaksh/Desktop/newqwerty")









path_cwd = os.getcwd()
print(path_cwd)

# # prints parent directory
print(os.path.abspath(os.path.join(path_cwd, os.pardir)))

print('Parent' , os.path.dirname(path_cwd))




