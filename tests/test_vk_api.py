import pytest
from vk_api import getUserNameFromId, postMessageToWall,deleteMessageFromWall

def test_getUserNameFromId():
    with pytest.raises(ValueError) as exec_info:
        getUserNameFromId(-3)
    assert str(exec_info) == 'user_id can not be smaller than "1"'

def test_postMessageToWall():
    res = postMessageToWall()
    assert res.get('response')[0] > 0

def test_deleteMessageFromWall():
    res = deleteMessageFromWall()
    assert res.get('response')[0] == 1

if __name__ == '__main__':
    test_getUserNameFromId()
