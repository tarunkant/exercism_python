str1= raw_input("enter alphabets for comparing ")
str2= raw_input("enter alphabets fom which you want to compare ")
count=0
i=0
if len(str1)>=len(str2):
 for i in range(len(str2)):
    if str1[i]==str2[i]:
      count +=1
    else: i=+1
else: 
 for i in range(len(str2)):
    if str1[i]==str2[i]:
      count +=1
    else: i+=1
print"Counting of alphabet which are  same is: ",count