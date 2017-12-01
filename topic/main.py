### Tyler's usage notes: TODO: Remove these and place in main file.
import doc_vectors

import nltk
nltk.download("punkt")
#Add multiple documents as strings.
keywords = doc_vectors.docs_to_keywords(["bananas are neat", "bananas, cabanas, bananas potatoes."])
print(keywords)