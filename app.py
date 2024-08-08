from pathlib import Path

path = Path("email")
path1 = Path()
print(path.exists())  # check existence of file/directory
# print(path.mkdir())  make new directory
# print(path.rmdir())  delete directory
for file in path1.glob('*.py'):
    print(file)
