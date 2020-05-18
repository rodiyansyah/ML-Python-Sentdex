import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

data = pd.read_csv('spam.csv',encoding='latin-1')
data.columns = ['v1','v2','v3','v4','v5']
data = data.rename(columns = {'v1': 'label', 'v2': 'text'})


token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(lowercase=True, stop_words='english', ngram_range=(1, 1), tokenizer=token.tokenize)
text_counts = cv.fit_transform(data['text'])
x_train, x_test, y_train, y_test = train_test_split(text_counts, data['label'], test_size=0.1, random_state=1)


clf = MultinomialNB().fit(x_train, y_train)
pred = clf.predict(x_test)
print("accuracy : ", metrics.accuracy_score(y_test, pred))

spam_count = data.groupby('label').count()
plt.bar(spam_count.index.values, spam_count['text'])
plt.xlabel('spam label')
plt.ylabel('Number of text')
plt.show()


