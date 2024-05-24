from razdel import sentenize
from model import classifier


def get_model_result(text, sep=True):
    '''
    text: str - Text to sentiment analysis
    sep: bool - True if you need to analyze each sentence individually,
    otherwise False.

    A function for analyzing the mood of the text.
    It can analyze both the whole text and sentences individually.

    Returns list of dictionaries such as
        [{
            'text': text or sentence,
            'label': negative/positive,
            'score': score of model
        }]
    '''
    if sep:
        text = [list(sent)[2] for sent in list(sentenize(text))]
    else:
        text = [text]

    evals = classifier(text)
    result = [
            {
                'Text': text[i],
                'label': eval['label'],
                'Score': round(eval['score'], 5)
            }
            for i, eval in enumerate(evals)
        ]
    return result
