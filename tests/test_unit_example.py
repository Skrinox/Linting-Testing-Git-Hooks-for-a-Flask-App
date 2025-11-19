from app import add_item_to_list, remove_item_from_list


def test_add_item_to_list():
    test_list = []
    add_item_to_list(test_list, 'item1')
    assert (test_list == ['item1'])
    add_item_to_list(test_list, 'item2')
    assert test_list == ['item1', 'item2']

def test_remove_item_from_list():
    test_list = ['item1', 'item2', 'item3']
    remove_item_from_list(test_list, 1)
    assert test_list == ['item1', 'item3']
    remove_item_from_list(test_list, 0)
    assert test_list == ['item3']
    remove_item_from_list(test_list, 5)
    assert test_list == ['item3'] 