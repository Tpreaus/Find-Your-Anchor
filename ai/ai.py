# Import the necessary libraries
import pandas as pd
import json
import requests
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora
from gensim.models import LdaModel

# Fetch the data from the API
response = requests.get('http://localhost:3005/api/clubs')
data = response.json()

# Convert the data to a pandas DataFrame
data = pd.DataFrame(data)

# Store descriptions
corpus = data['Description']
# Store activity names
activity_names = data['Activity Name'].tolist()

# Clean the data
nltk.download('stopwords')
nltk.download('wordnet')  
nltk.download('omw-1.4')  
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

# remove stopwords, punctuation, and normalize the corpus
# Filter out these words
filter_out = {'club', 'rollins', 'student', 'students', 'organization', 'organizations', 
              'campus', 'college', 'university', 'community', 'group', 'groups', 'association', 
              'associations', 'society', 'societies'}

stop = set(stopwords.words('english')).union(filter_out)
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

# Function to clean the text
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = "".join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

clean_corpus = [clean(doc).split() for doc in corpus]

# Creating document-term matrix 
dictionary = corpora.Dictionary(clean_corpus)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in clean_corpus]

# LDA model
lda = LdaModel(doc_term_matrix, num_topics=100, id2word = dictionary)

# Get dominant topic for each document
dominant_topics = []
for doc_bow in doc_term_matrix:
    topic_distribution = lda.get_document_topics(doc_bow)
    dominant_topic = sorted(topic_distribution, key=lambda x: x[1], reverse=True)[0]
    dominant_topics.append(dominant_topic)

# Print array with activity name and topic num
activity_topic_array = []
for i, topic in enumerate(dominant_topics):
    activity_topic_array.append((activity_names[i], topic[0]))
print(activity_topic_array)

