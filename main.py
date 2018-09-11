# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 23:36:36 2018

@author: Computer
"""

pinyintothaidict =	{
#การถอดเสียงพยัญชนะแบบพินอิน
"p" : "พ" ,
"t" : "ท" ,
"k"	:	"ค" ,
"b":	"ป",
"d"	:	"ต",
"g"	:	"ก",
"s"	:	"ส",
"c"	: "ฉ",
"z"	:	"จ",
"x"	:	"ส",
"q"	:	"ช",
"j"	:	"จ",
"sh"	:	"ซ",
"ch"	: "ช",
"zh"	:	"จ",
"f"	:	"ฟ",
"h"	:	"ห",
"l"	:	"ล",
"r"	: "ร",
"w"	:	"ว",
"y"	:	"ย",
"m"	:	"ม",
"n"	:	"น",
"ng"	:	"ง",


#การถอดเสียงสระ
"a":		"อา",
"ā":		"อา",
"á":		"อ๋า",
"ǎ":		"อ่า",
"à":		"อ้า",


"ai":	"อาย",
"ài":	"อ้าย",
"an":		"อัน",
"án":		"อั๋น",
"àn":		"อั้น",
"ang":		"อัง",
"áng":		"อ๋าง",
"ar":  "อาร์",
"anr":  "อาร์",
"air":		"อาร์",
"ao":		"เอา",
"ǎo":		"เอ่า",
"áo":		"เอ๋า",

"e":	"เออ",
"ē":	"เออ",
"ê":	"เอ",
"ě":	"เอ่อ",
"é":	"เอ๋อ",
"è":	"เอ้อ",

"ei":	"เอย์",
"èi":	"เอ้ย",
"ěi":	"เอ่ย",
"en":	"เอิน",
"ēn":	"เอิน",
"eng":	"เอิง",  
"éng": "เอิ๋ง",
"er":		"เออร์",

"i":	"อี",
"ī":	"อี",
"í":	"อี๋",
"ì":	"อี้",
"ǐ":	"อี่",

"ia":		"เอีย",
"iān":		"เอียน",
"iàn":		"เอี้ยน",
"iǎn":		"เอี่ยน",
"iào":		"เอี้ยว",
"ie":		"เอีย",
"īn":		"อิน",
"íng":		"อิ๋ง",
"ìng":		"อิ้ง",
"ǐng":		"อิ่ง",
"iu":		"อิว",

"o":		"โอ",
"ō":		"โอ",
"ǒ":		"โอ่",
"Ó":		"โอ๋",
"ó":		"โอ๋",
"ò":		"โอ้",

"ong":		"อง",
"òng":		"อ้ง",
"ǒng":		"อ่ง",
"ou":		"โอว",
"ǒu":		"โอว",
"ǒu":"โอ่ว",
"Òu":"โอ้ว",

"u":	"อู",
"ū":	"อู",
"ú":	"อู๋",
"ǔ":	"อู่",
"ù":	"อู้",

"uǎ":	"อั่ว",
"uàn":	"อ้วน",
"uǎn":	"อ่วน",
"uāng":	"อวง",

"ue":  "เอว",


"uer":		"เอวร์", 
"ui":		"อุย",
"un":	"อุน",
"uo":		"อัว",
"ü":		"อวี", 
"üe":		"เอว", 
"ün":		"อวิน"

}


inputwords = 'Céng yǒu yī shuāng shǒu jiào máng zhě zhòng míng Sheng mìng jiàn guāng huàn rán yī xīn, tā qí miào de shǒu cháng fǔ wèi zhe wǒ lǐng wǒ zǒu xiàng guāng míng. Qí miào de ēn diǎn ràng wǒ yòu dé zháo Měi hǎo de xīn sheng mìng, wǒ yǒng yuǎn gē sòng wǒ yǒng yuǎn zàn měi nǐ nà qí miào de shuāng shǒu. Ó! Zhǔ! Nǐ nà qí miào de shuāng shǒu, ó! Zhǔ! Nǐ nà cí ài de shuāng shǒu, qí miào de ēn diǎn ràng wǒ yòu dé zháo měi hǎo de xīn sheng mìng, wǒ yǒng yuǎn gē sòng wǒ yǒng yuǎn zàn měi nǐ nà qí miào de shuāng shǒu. Zhǔ nǐ de yán yǔ shì wǒ de néng lì Xiāng xìn zhě b ìděi zhe yī zhì, Qí miào de huà yǔ zhǔ yī zhì le wǒ lǐng wǒ zǒu xiàng guāng míng.'
outputlist = []
outputstring = ''
lowercasewords = inputwords.lower()
replaceexcalm=lowercasewords.replace('!',' ')
replacecomma = replaceexcalm.replace('.',' ')
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
            if itr-1 >= 0:
                
                wordcreated=tempwordtomodify.replace('อ',charbefore,1)
            else:
                wordcreated=tempwordtomodify
            print(wordcreated)
        elif itr > 0:
            wordcreated=wordcreated+thaicharlist[itr]
            
    outputlist.append(wordcreated)
    wordcreated='' #reset the word
print(splittedwords)
print(outputlist)


#convert from list to string with spaces 
for word in outputlist:

    outputstring = outputstring + (word)
    outputstring = outputstring +' '
    
print(outputstring)







