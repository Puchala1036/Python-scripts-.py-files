#Create a Dictionary of Student Marks
'''
dict={"sss":98,"hhh":56,"wew":98 }
ask_studName=input("Enter the student's name:")
for i in dict:
    if ask_studName ==i:
        print("{} marks:{}".format(ask_studName,dict[i]))
        found=True
        break 
    else:
        print("Student not found {}".format(ask_studName))
'''
#Demonstrate List Slicing 

'''
Original_List=[1,2,3,4,5,6,7,8,9,10]
Extracted_List=(Original_List[0:5])
print("Extracted first five elements", Extracted_List)
Reversed_List=Extracted_List.copy()
Reversed_List.reverse()
print("Reversed Extracted elements", Reversed_List)
'''