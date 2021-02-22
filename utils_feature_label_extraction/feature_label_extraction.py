from scipy import sparse
import numpy as np

from utils_unique_word_dict import unique_word_dict

class OneHot_Encoding:

    def onehot(self,word_lists:list,all_words:list):

        """This method to get one one hot vector for all the words"""

        dict_class = unique_word_dict.Unique_Word()
        words=dict_class.create_unique_word_dict(all_words)

        n_words=len(words)

        feature = []
        label = []

        for num, word_list in enumerate(word_lists):

            # Getting the indices
            main_word_index = words.get(word_list[0])
            context_word_index = words.get(word_list[1])

            # Creating the placeholders
            feature_row = np.zeros(n_words)
            label_row = np.zeros(n_words)

            # One hot encoding the main word
            feature_row[main_word_index] = 1

            # One hot encoding the Y matrix words
            label_row[context_word_index] = 1

            feature.append(feature_row)
            label.append(label_row)
        return feature,label

    def convert_to_csrMatrix(self,feature:list,label:list):

        """This method to convert to csr matrix"""
        features = sparse.csr_matrix(feature)
        labels = sparse.csr_matrix(label)

        return features,labels