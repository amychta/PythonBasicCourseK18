from unittest import TestCase

from lessons.treewalker.TreeBuilder import create_tree, excluded_topics
from lessons.treewalker.TreeWalker import only_included_leafs


class TestMyNode(TestCase):
    def test_world_tree(self):
        tree = create_tree()
        topics = excluded_topics()
        list_included_topics = only_included_leafs(tree, topics)
        expected_topics = ['Golosiivsky region', 'Lviv', 'Poltava', 'Katowice', 'Washington'];
        self.assertEqual(list_included_topics, expected_topics)
