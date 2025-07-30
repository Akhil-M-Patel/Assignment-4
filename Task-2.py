with open("output.txt",'w') as f1:
    line1=input("Enter text to write to the file:")
    f1.write(line1+'\n')
    print("Data succesfuly written to output.txt.\n")
    
with open("output.txt",'a') as f1:
    line2=input("Enter additional text to append:")
    f1.write(line2+'\n')
    print("Data succesfullly appended.\n")

with open("output.txt",'r') as f1:
    print("Final content of output.txt:")
    for i in f1.readlines():
        print(i.strip())