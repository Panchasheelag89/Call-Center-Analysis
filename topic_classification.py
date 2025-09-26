from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def classify_topics(texts, n_topics=3):
    vectorizer=CountVectorizer(stop_words='english')
    X=vectorizer.fit_transform(texts)
    lda=LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)
    topics=[]
    for idx,topic in enumerate(lda.components_):
        top_words=[vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-5:]]
        topics.append(f"Topic {idx+1}: {', '.join(top_words)}")
    return topics
