sentence= raw_input("give a sentence ")
sentence= sentence.replace(' ','')
if set(sentence.lower()) >= set('abcdefghijklmnopqrstuvwxyz'):
    print"It is pangram"
else: print"It is not pangram"




