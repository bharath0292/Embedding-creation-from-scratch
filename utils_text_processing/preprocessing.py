import re

class Preprocessing:

    def remove_punctuations(self,text, punctuations=r'''!()-[]{};:'"\,<>./?@#$%^&*_“~''') :

        """ A method to remove punctuations """

        for x in text.lower():
            if x in punctuations:
                text = text.replace(x, "")

        return text

    def remove_digits(self, text):

        """ A method to remove numeric digits """

        text = re.sub(r'\w*\d\w*', '', text)

        return text

    def remove_whitespaces(self, text):

        """ A method to remove whitespace """

        text = re.sub(r'\s+', ' ', text).strip()

        return text

    def words_to_lower(self, text):

        """ A method to change words to lower """

        text = text.lower()

        return text


    def remove_stopwords(self, text : list, stop_words=['and', 'a', 'is', 'the', 'in', 'be', 'will', 'was']) -> list:

        """ A method to remove stopwords """

        text=text.split(' ')

        text = [x for x in text if x not in stop_words]

        return text
