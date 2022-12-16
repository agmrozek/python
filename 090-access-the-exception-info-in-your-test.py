import pytest

def test_new_score_should_be_higher(yellow_belt):
    assert yellow_belt.score == 50
    with pytest.raises(ValueError) as excinfo:
        yellow_belt.score = 40
    assert str(excinfo.value) == "Cannot lower score"

(Pdb) excinfo.value
ValueError('Cannot lower score')
(Pdb) str(excinfo.value)
'Cannot lower score'