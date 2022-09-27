import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/n1', '1', True, True, 10, '/')
        self.assertEqual(tree.getData('/n1'), '1')
    def test_crear_znode_2(self):
        tree = Ztree()
        tree.create('/n2', '2', True, True, 10, '/')
        self.assertEqual(tree.getData('/n2'), '2')
    def test_crear_znode_3(self):
        tree = Ztree()
        tree.create('/n2/n3', '2', True, True, 10, '/')
        self.assertEqual(tree.getData('/n2/n3'), '2')
    def test_borrar(self):
        tree = Ztree()
        tree.delete('/n2/n3',1)
        self.assertFalse(tree.getData('/n2/n3'),0)
    def test_show(self):
        tree = Ztree()
        tree.showTree()
        

if __name__ == '__main__':
    unittest.main()

