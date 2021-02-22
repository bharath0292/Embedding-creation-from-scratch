import pandas as pd

class File_Processing:

    def read_data(self,file_path) -> list:

        """ The method to read file and convert to list """

        #read a file
        data=pd.read_csv(file_path)

        #convert to list
        texts = [x for x in data['text']]

        return texts

    def write_data(self,dataframe):

        """ The method to read file and convert to list """

        dataframe.to_csv('embed.txt', index=False, header=False)
        print('Embedding saved successfully')
