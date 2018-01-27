import re

#Note: everything is read from left-to-rigbt, HOWEVER, when using file.readlines(), and printing out the
#dictionary, it goes backwards in the iteration...?


#TODO:
# separate basmallah
# Get root-words
# Get i'rab
# Alif-sagheerah
# Change surah names from numbers to actual names
# Change to specific ayah (or ayat) names from numbers
# Notate makkan/madinan surah



def partitionSurahs(file):
    #Iterate all the way through entire file
    #Set i to 0
    #While read_file[1] is i + 1
        #store the ayat
    #Else, move onto next surah

    regex = r"\d+"
    split_file = file.split('\n')


    surahs = dict()
    end_index = len(split_file)

    for i in range(len(split_file) - 1, -1, -1):
        ayah = split_file[i]
        chapter, verse = re.findall(regex, ayah)


        #if new chapter started or the last chapter is reached
        if int(verse) == 1:
            surahs[int(chapter)] = '\n'.join(split_file[i:end_index])

            end_index = i

    return surahs

def partitionNames(file):
    '''Make a dictionary of list of surah names, for later use in indexing surahs by name'''
    split_file = file.split('\n')
    regex1 = r'\d+'
    regex2 = r'\(\w+[\W*\w+]*\)'

    data = dict()
    for line in split_file:
        number = re.search(regex1, line)
        english = re.search(regex2, line)

        #Take everything from 
        transliteration = line[number.span()[1]+1:english.span()[0]].strip()




def changeName(file1, file2):
    '''Use surah names to be indexed so that one can look up a surah by its name rather than just its number'''

    #Sorted because iterated backwards in partitioning the suraat
    for key in sorted(file1.keys()):
        pass




def separateCopyrightStatement(file, regex):
    split_file = file.split('\n')
    __copyright_statement = str()
    copyright_statement_indices = list()
    for i in range(len(split_file)):
        line = split_file[i]
        if re.search(regex, line) is None or '#' in line:
            __copyright_statement += line
            copyright_statement_indices.append(i)


    #use newline to join just so that it prints with a newline every line...otherwise prints with last ayah
    #first due to reading left-to-right instead of right-to-left

    #Add hash-symbol so that it remains like original
    __copyright_statement = '\n#'.join(__copyright_statement.split('#'))

    #Take everything that's before the copyright-statement
    mushaf_without_copyright = '\n'.join(split_file[:copyright_statement_indices[0]])
    return mushaf_without_copyright, __copyright_statement


def getWithoutCopyrightStatement(file, regex):
    return separateCopyrightStatement(file, regex)[0]

def getCopyrightStatement(file, regex):
    return separateCopyrightStatement(file, regex)[1]



def __main__():
    with open(r'C:/Users/hartm/PycharmProjects/quran/quran-uthmani.txt', 'r', encoding='utf-8') as quran,\
         open(r'C:\Users\hartm\PycharmProjects\quran\surah_names.txt', 'r', encoding='utf-8') as names:

        #Mushaf itself
        mushaf_with_copyright = quran.read()
        mushaf = getWithoutCopyrightStatement(mushaf_with_copyright, r'\d+')
        partitioned_surahs = partitionSurahs(mushaf)

        print(sorted(partitioned_surahs.keys()))

        #Surah names
        surah_names_with_copyright = names.read()
        surah_names = getWithoutCopyrightStatement(surah_names_with_copyright, r'\d+\.')

        # changeName(partitioned_surahs)
        partitionNames(surah_names)











__main__()
