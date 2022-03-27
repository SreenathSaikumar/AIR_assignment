# AIR Assignment UE19CS332
## The Team
Sreenath Saikumar - PES2UG19CS406<br>
Srivatsan Narendiran - PES2UG19CS408<br>
Sreekanth Maneesh - PES2UG19CS405

## Datasets Used
[Legal Citation Text Classification](https://www.kaggle.com/datasets/shivamb/legal-citation-text-classification)<br>
[Shopee Text Reviews](https://www.kaggle.com/datasets/shymammoth/shopee-reviews)<br>
[Emotion Detection from Text](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text)

## Search Techniques Used
- Phrase querying for 2 words with proximity has been performed and benchmarked for query retrieval time on the Legal Citation and Shopee Text review dataset. A positional index is used for the same.
- Simple 2 word boolean querying has been performed and benchmarked on the Emotion Detection dataset with the use of AND, OR and NOT. An inverted index is constructed for the same.