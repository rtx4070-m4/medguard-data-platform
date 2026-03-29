
from pipeline.pipeline import Pipeline

def test_pipeline():
    p=Pipeline()
    result=p.run()
    assert 'rows' in result
