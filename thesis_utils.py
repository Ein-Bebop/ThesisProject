import spacy


nlp = spacy.load('es_core_news_sm')

def sentencer(comment):
  sentences_raw = list(nlp(comment).sents)

  sens_clean = []
  for sent in sentences_raw:
    if len(sent) > 1:
      # print(sent)
      sens_clean.append([sent])
  return list(sens_clean)

def deepest_sentence(sentences):
    if type(sentences) is not list:
        return sentences.text
    else:
        for i in range(len(sentences)):
            return deepest_sentence(sentences[i])
        # return deepest_sentence(sentences[0])