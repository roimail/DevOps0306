#open file only for read
file = open("requirements.txt", "r")
#print(file.read())
for line in file.readlines():
    print(line, end='')

#open file only for append (notice the newline pattern)
file_a = open("requirements.txt", "a")
#file_a.writelines(["datadog\n"])
#file_a.writelines(["socketio\n"])


# check that the line was added to the text file
print(file.read(), end='')


file.close()
file_a.close()



# another way, using "with"
# try:
#     with open("requirements.txt",r) as f:
#         f.read()
# except:
#     print('nope')



