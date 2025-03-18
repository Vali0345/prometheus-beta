import pytest
from src.list_difference import find_list_difference

def test_basic_list_difference():
    """Test basic list difference scenario"""
    unique1, unique2, common = find_list_difference([1, 2, 3], [3, 4, 5])
    assert unique1 == {1, 2}
    assert unique2 == {4, 5}
    assert common == {3}

def test_empty_lists():
    """Test behavior with empty lists"""
    unique1, unique2, common = find_list_difference([], [])
    assert unique1 == set()
    assert unique2 == set()
    assert common == set()

def test_one_empty_list():
    """Test difference with one empty list"""
    unique1, unique2, common = find_list_difference([1, 2, 3], [])
    assert unique1 == {1, 2, 3}
    assert unique2 == set()
    assert common == set()

def test_identical_lists():
    """Test lists with identical elements"""
    unique1, unique2, common = find_list_difference([1, 2, 3], [1, 2, 3])
    assert unique1 == set()
    assert unique2 == set()
    assert common == {1, 2, 3}

def test_duplicate_elements():
    """Test lists with duplicate elements"""
    unique1, unique2, common = find_list_difference([1, 1, 2, 3], [1, 4, 4, 5])
    assert unique1 == {2, 3}
    assert unique2 == {4, 5}
    assert common == {1}

def test_different_types():
    """Test lists with different types of elements"""
    unique1, unique2, common = find_list_difference([1, 'a', 2], ['a', 3, 4])
    assert unique1 == {1, 2}
    assert unique2 == {3, 4}
    assert common == {'a'}

def test_large_lists():
    """Test behavior with larger lists"""
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    unique1, unique2, common = find_list_difference(list1, list2)
    assert len(unique1) == 500
    assert len(unique2) == 500
    assert len(common) == 500