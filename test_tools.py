from tools import get_model_result

def test_model_result():
    result = get_model_result("I went for a walk in the woods. "
                              "The weather was good. Suddenly it started to rain and I got wet and sick.", sep=False)
    assert result[0]['label'] == 'NEGATIVE'


def test_model_result_separate():
    result = get_model_result("I went for a walk in the woods. "
                              "The weather was good. Suddenly it started to rain and I got wet and sick.", sep=True)
    assert result[0]['label'] == 'POSITIVE'
    assert result[1]['label'] == 'POSITIVE'
    assert result[2]['label'] == 'NEGATIVE'