print"To know the complement of DNA"
string= raw_input("give DNA strand ")
str2 = ""
i=0
for i in range(len(string)):
   if string[i]=="A" :
     str2+="U"
   elif string[i]=="T" :
     str2+="A"
   elif string[i]=="C" :
     str2+="G"
   elif string[i]=="G" :
     str2+="C"
   else:
       str2 += string[i]

print "Your RNA strand is :",str2 