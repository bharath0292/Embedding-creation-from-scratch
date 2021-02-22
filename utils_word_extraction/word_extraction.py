from utils_text_processing import preprocessing

class Word_Extracting:

    def create_context_and_unique_word(self,sentences:list):

        """The method to find contexts and unique words"""

        #list to get contexts
        word_lists=[]

        #list to get unique words
        all_words=[]

        for sentence in sentences:
            #initialize Preprocessing class
            pre=preprocessing.Preprocessing()

            #remove puntuations
            sentence=pre.remove_punctuations(sentence)

            #remove numerics
            sentence=pre.remove_digits(sentence)

            #remove whitespaces
            sentence=pre.remove_whitespaces(sentence)

            #convert words to lower
            sentence=pre.words_to_lower(sentence)

            #remove stopwords
            sentence=pre.remove_stopwords(sentence)

            all_words+=sentence

            #length of sentence
            length=len(sentence)

            for first_word in range(length):
                for second_word in range(length):
                    if first_word != second_word:
                        word_lists.append([sentence[first_word]] + [sentence[second_word]])

        return word_lists,all_words