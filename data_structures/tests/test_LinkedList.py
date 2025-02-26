import pytest
from data_structures.LinkedList import Node, LinkedList


@pytest.fixture()
def node1():
    yield Node('apple')


@pytest.fixture()
def node2():
    yield Node(1234)


@pytest.fixture()
def ll_0_items():
    yield LinkedList()


@pytest.fixture()
def ll_2_items():
    l = LinkedList()
    node1 = Node('Node 1')
    node2 = Node('Node 2')
    node1.next = node2
    node2.previous = node1
    l.head = node1
    l.tail = node2
    l._length = 2
    yield l


def test_repr(ll_0_items):
    assert repr(ll_0_items) == "<LinkedList object: head = None>"


def test_len(ll_0_items, ll_2_items):
    assert len(ll_0_items) == 0
    assert len(ll_2_items) == 2


def test_insert_first(ll_0_items, ll_2_items):
    # empty list
    ll_0_items.insert_first('inserted')
    assert ll_0_items.head.data == 'inserted'
    assert ll_0_items.tail.data == 'inserted'

    # 2 items list
    assert len(ll_2_items) == 2
    ll_2_items.insert_first('inserted')
    assert len(ll_2_items) == 3
    assert ll_2_items.head.data == 'inserted'
    assert ll_2_items.head.next.data == 'Node 1'
    assert ll_2_items.head.next.previous.data == 'inserted'


def test_insert_last(ll_0_items, ll_2_items):
    # empty list
    ll_0_items.insert_first('inserted')
    assert ll_0_items.head.data == 'inserted'
    assert ll_0_items.tail.data == 'inserted'

    # 2 items list
    assert len(ll_2_items) == 2
    ll_2_items.insert_last('inserted')
    assert len(ll_2_items) == 3
    assert ll_2_items.tail.data == 'inserted'
    assert ll_2_items.tail.previous.data == 'Node 2'
    assert ll_2_items.tail.previous.next.data == 'inserted'


def test_delete_first(ll_2_items):
    assert len(ll_2_items) == 2
    item_2 = ll_2_items[1]
    ll_2_items.delete_first()
    assert len(ll_2_items) == 1
    assert ll_2_items[0] == item_2


def test_delete_last(ll_2_items):
    assert len(ll_2_items) == 2
    item_1 = ll_2_items[0]
    ll_2_items.delete_last()
    assert len(ll_2_items) == 1
    assert ll_2_items[0] == item_1


def test_getter_setter(ll_2_items, ll_0_items):
    assert len(ll_2_items) == 2
    assert ll_2_items[0] != '1st'
    assert ll_2_items[1] != '2nd'
    ll_2_items[0] = '1st'
    ll_2_items[1] = '2nd'
    assert ll_2_items[0] == '1st'
    assert ll_2_items[1] == '2nd'


def test_insert_at(ll_2_items):
    assert len(ll_2_items) == 2
    item_1 = ll_2_items[0]
    item_2 = ll_2_items[1]
    ll_2_items.insert_at(1, 'New node')
    assert len(ll_2_items) == 3
    assert ll_2_items[0] == item_1
    assert ll_2_items[1] == 'New node'
    assert ll_2_items[2] == item_2


def test_delete_at(ll_2_items):
    assert len(ll_2_items) == 2
    item_1 = ll_2_items[0]
    ll_2_items.delete_at(1)
    assert len(ll_2_items) == 1
    assert ll_2_items[0] == item_1
    ll_2_items.delete_at(0)
    assert len(ll_2_items) == 0
