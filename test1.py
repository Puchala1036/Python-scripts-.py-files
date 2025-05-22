#Handle Errors 
with open('samp.txt', 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
print('Error: The file sample.txt does not exist.')


 

#Append Data to a File
file1=open('sam.txt','a')
append_file=file1.write('\n Learning file  Handling in Python')
print(append_file)
file1.close()
file1=open('sam.txt','r')
append_file=file1.read()
print(append_file)
file1.close()
