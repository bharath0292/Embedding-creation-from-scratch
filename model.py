from utils_file_processing import file_processing
from utils_word_extraction import word_extraction
from utils_feature_label_extraction import feature_label_extraction
from utils_unique_word_dict import unique_word_dict

from keras.models import Input, Model
from keras.layers import Dense
import pandas as pd

#path to the file
path=r'Data\sample.csv'

#initialize file class
file=file_processing.File_Processing()
sentence_list=file.read_data(path)

#initialize Word_Extracting to get context
word_extract=word_extraction.Word_Extracting()
word_lists,all_words=word_extract.create_context_and_unique_word(sentence_list)

#to get unique words
unique_word_class=unique_word_dict.Unique_Word()
words=unique_word_class.create_unique_word_dict(all_words)
words=list(words.keys())

#it will change all words to csr matrix
feature_label=feature_label_extraction.OneHot_Encoding()
feature,label=feature_label.onehot(word_lists,all_words)
feature,label=feature_label.convert_to_csrMatrix(feature,label)


embed_size = 2

# Defining the neural network
input = Input(shape=(21,))

output = Dense(units=embed_size, activation='relu')(input)
output = Dense(units=21,   activation='softmax')(output)

model = Model(inputs=input, outputs=output)
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Optimizing the network weights
model.fit(x=feature,y=label,batch_size=256,epochs=1000)

embedding=model.get_weights()[0]

word=[]
vectors=[]

for w in words:
    word.append(w)
for v in embedding:
    vectors.append(v)

word_vector=pd.DataFrame(pd.concat([pd.Series(word),pd.Series(vectors)],axis=1))

#write to embed.txt
file.write_data(word_vector)
