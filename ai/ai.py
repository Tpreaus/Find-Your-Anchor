

import pandas as pd

data = pd.read_csv('clubData/rollins_activities_and_descriptions.csv')

corpus = data['Description']

import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')  
nltk.download('omw-1.4')  
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

# remove stopwords, punctuation, and normalize the corpus
# Filter
filter_out = {'club', 'rollins', 'student', 'students', 'organization', 'organizations', 
              'campus', 'college', 'university', 'community', 'group', 'groups', 'association', 
              'associations', 'society', 'societies'}

stop = set(stopwords.words('english')).union(filter_out)
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

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

from gensim.models import LsiModel

# LSA model
lsa = LsiModel(doc_term_matrix, num_topics=3, id2word = dictionary)

# LSA model
print(lsa.print_topics(num_topics=100, num_words=3))


from gensim.models import LdaModel

# LDA model
lda = LdaModel(doc_term_matrix, num_topics=100, id2word = dictionary)

# Get dominant topic for each document
dominant_topics = []
for doc_bow in doc_term_matrix:
    topic_distribution = lda.get_document_topics(doc_bow)
    dominant_topic = sorted(topic_distribution, key=lambda x: x[1], reverse=True)[0]
    dominant_topics.append(dominant_topic)

# Print dominant topic for each document
for i, topic in enumerate(dominant_topics):
    print(f"Document {i+1} has dominant topic {topic[0]} with probability {topic[1]}")
