from PyTest_example.Manager import Manager


def test_add_task():
    manager = Manager('test')
    manager.add_task('test')
    assert manager.get_task_list() == ['test']


def test_get_task_list():
    manager = Manager('test')
    manager.add_task('test')
    assert manager.get_task_list() == ['test']


def test_del_task():
    manager = Manager('test')
    manager.add_task('test')
    manager.del_task('test')
    assert manager.get_task_list() == []
