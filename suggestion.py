import re

def bigram(word, previous_word, word_list):
   expression_count = 0
   previous_count =  0
   for i in range(len(word_list)):
      if(i < len(word_list)):
         if (previous_word == word_list[i]) and (word == word_list[i+1]):
            expression_count +=1

      if (previous_word == word_list[i]):
         previous_count+=1

   if(previous_count == 0):
      previous_count +=1

   return float(expression_count/previous_count)


def trigram(word, previous_word, previous_word2, word_list):
   expression_count = 0
   previous_count =  0
   for i in range(len(word_list)):
      if(i < len(word_list)-1):
         if (previous_word2 == word_list[i]) and (previous_word == word_list[i+1]) and (word == word_list[i+2]):
            expression_count +=1

      if (previous_word2 == word_list[i]) and (previous_word == word_list[i+1]):
         previous_count+=1

   if(previous_count == 0):
      previous_count +=1
      
   return float(expression_count/previous_count)


def suggestion(text, word_list, rawText, regex, typeGram):
   print("\nProcessing...")
   probability = 0
   results = []
   sentence = text.split(' ')

   if(typeGram == "B"):
      bigram_word_list = re.findall(sentence[-1] + " " + regex, rawText)
      for word in bigram_word_list:
         wordAux = word.split(' ')[1]
         results.append([bigram(wordAux, sentence[-1], word_list), wordAux])
   else: 
      trigram_word_list = re.findall(sentence[-1]+" "+sentence[-2]+" "+ regex, rawText)
      for word in trigram_word_list:
         wordAux = word.split(' ')[2]
         results.append([trigram(wordAux, sentence[-1], sentence[-2], word_list), wordAux])

   suggestedAux = []
   for result in results:
      if result not in suggestedAux:
         suggestedAux.append(result)

   suggested = []
   for word in sorted(suggestedAux, reverse=True)[:3]:
      suggested.append(word[1])

   return suggested


def main():
   regex = "[a-zçãõáéíóúâêîôûà']+"
   word_list = open('shakespeare.txt','r').read().lower()

   print("Select one option")
   print("1.Bigram")
   print("2.Trigram")
   option = int(input("\nOption: ")) 
   if(option == 1):
      text = input("\nEnter the sentence: ").lower()
      print("The suggested words are:",suggestion(text,  re.findall(regex, word_list), word_list, regex, 'B'))
   else:
      text = input("\nEnter the sentence: ").lower()
      print("The suggested words are:",suggestion(text,  re.findall(regex, word_list), word_list, regex, 'T'))

main()