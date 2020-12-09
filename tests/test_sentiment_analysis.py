import my_package


def test_positive() -> None:
    a = my_package.SentimentAnalyzer()
    assert(a.predict('I am feeling so good!') == 'POSITIVE')
