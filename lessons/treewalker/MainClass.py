from lessons.treewalker.TreeBuilder import create_tree
from lessons.treewalker.TreeBuilder import excluded_topics
from lessons.treewalker.TreeWalker import pretty_print_tree, only_included_leafs

print "------------  Original tree ----------"
tree = create_tree()
print pretty_print_tree(tree)
print "------------  Exclude list ----------"
excluded_list = excluded_topics()
print excluded_list

print "------------  Result list ----------"
result_list = only_included_leafs(tree, excluded_list)
print result_list

