# Import the necessary libraries
import pandas as pd

# Load the data
data = pd.read_csv('clubData/rollins_activities_and_descriptions.csv')

# Store descriptions
corpus = data['Description']
# Store activity names
activity_names = data['Activity Name'].tolist()

# Print the first 5 descriptions
import string
import nltk
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

from gensim import corpora

# Creating document-term matrix 
dictionary = corpora.Dictionary(clean_corpus)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in clean_corpus]

from gensim.models import LdaModel

# LDA model
lda = LdaModel(doc_term_matrix, num_topics=100, id2word = dictionary)

# Get dominant topic for each document
dominant_topics = []
for doc_bow in doc_term_matrix:
    topic_distribution = lda.get_document_topics(doc_bow)
    dominant_topic = sorted(topic_distribution, key=lambda x: x[1], reverse=True)[0]
    dominant_topics.append(dominant_topic)

# Print dominant topic and associated words for each document
for i, topic in enumerate(dominant_topics):
    topic_num = topic[0]
    topic_words = lda.show_topic(topic_num)
    top_words = ", ".join([word[0] for word in topic_words])
    print(f"Activity '{activity_names[i]}' with associated words: {top_words}")