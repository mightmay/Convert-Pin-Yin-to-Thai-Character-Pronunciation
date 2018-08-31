# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 23:36:36 2018

@author: Computer
"""

pinyintothaidict =	{
  "éng": "เอิ๋ง",
  "ǒu":"โอ่ว",
  "c": "ฉ",
  "q": "ช",
  "y":"ย"
}


inputwords = 'Céng yǒu yī shuāng  shǒu jiào máng  zhě zhòng  míng'
outputlist = []
outputstring = ''
lowercasewords = inputwords.lower()

replacecomma = lowercasewords.replace('.',' ')
replacedot = replacecomma.replace(',',' ')

splittedwords = replacedot.split()
print(splittedwords)


for i1 in range(len(splittedwords)):
        
    wordtoloop =splittedwords[i1]
    
    
    
    # we will use this list to build the Thai character pronounciation later
    thaicharlist = []
    
    '''
    Example of segments of the word céng: 
    céng=
    c <-- matched
    cé
    cén
    céng
    é
    én
    éng <--- matched
    '''
    # temp string to append char, to use segments of the word to search our dicts
    tempstr = ""
    whileloopcounter =0 #stop when looping too much
    # while the there are still char left in that word
    while(len(wordtoloop)>0 and whileloopcounter<20):
        whileloopcounter=whileloopcounter+1
        print(whileloopcounter)
        for char in (wordtoloop): #loop through each char in the word
            tempstr+=char
            print(tempstr)
            
            if(tempstr in pinyintothaidict): #if the words segment is in dict, then keep it first, we will use the last segment as the correct match
                chartodelete = tempstr
                
        thaicharlist.append(pinyintothaidict[chartodelete]) # append the last segment to our list for creating Thai char pronouciation
        tempstr = "" # reset the temp
        
        wordtoloop = wordtoloop.replace(chartodelete,'',1) # delete the matched segment from word
    
    print(thaicharlist)
    
    foundoo_flag = 0 #flag to see if there is any อ which we can replace with leading char
    
    for itr in range(len(thaicharlist)):
        
        #check if it is vowel, if it is we will replace อ with leading character
        if 'อ' in thaicharlist[itr]:
            print(thaicharlist[itr])
            foundoo_flag = 1
            tempwordtomodify = thaicharlist[itr]
            charbefore = thaicharlist[itr-1]
            wordcreated=''
            wordcreated=tempwordtomodify.replace('อ',charbefore,1)
            print(wordcreated)
    outputlist.append(wordcreated)
    wordcreated='' #reset the word
print(outputlist)


#convert from list to string with spaces 
for word in outputlist:

    outputstring = outputstring + (word)
    outputstring = outputstring +' '
    
print(outputstring)







