import spacy
from spacy import displacy
from spacy.lang.en import English
from spacy.tokens import DocBin
from spacy.util import filter_spans
import json
from tqdm import tqdm #for test
# from data import train, dev
from data2 import train, dev



## Load in roBERTa Model
nlp = spacy.blank("en")

training_data = train
dev_data = dev

db = DocBin()
i = 0
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations['entities']:
        span = doc.char_span(start, end, label=label)
        if span is None:
            print(f'Skipping Entity -- {i}')
        else:
            ents.append(span)
        i += 1
    doc.ents = ents
    db.add(doc)

db.to_disk("./train.spacy")


# db = DocBin()
# i = 0
# for text, annotations in dev_data:
#     doc = nlp(text)
#     ents = []
#     for start, end, label in annotations['entities']:
#         span = doc.char_span(start, end, label=label)
#         if span is None:
#             print(f'Skipping Entity -- {i}')
#         else:
#             ents.append(span)
#         i += 1
#     doc.ents = ents
#     db.add(doc)

# db.to_disk("./dev.spacy")