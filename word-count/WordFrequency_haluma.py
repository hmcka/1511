import re

#globals
frequency = {}
text_string = None

def wordFreq():
    """Finds the frequency of words within a file"""
    

file_name = input("What file do you want to process? (Don't forget to add the doc type, .txt at the name of your file (text-doc.txt and word-count.txt will work).")

while text_string == None:
    try:
        document_text = open(file_name, 'r')
        text_string = document_text.read().lower()
    except (FileNotFoundError):
        print("That is not the name of a file!")
        file_name = input("What file do you want to process? (Don't forget to add the doc type, .txt at the name of your file.")

find_words = re.findall(r'\b[a-z]{2,15}\b', text_string)
 
for word in find_words:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, " :: ", frequency[words])

#main
#main()
input("\nPress Enter to Exit.")
