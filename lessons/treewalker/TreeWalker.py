from lessons.treewalker.MyNode import MyNode
from lessons.treewalker.TreeBuilder import create_tree, excluded_topics
import json


def pretty_print_tree(tree):
    ugly_json = tree.__str__()
    parsed_json = json.loads(ugly_json)
    formatted_json = json.dumps(parsed_json, indent=4)
    return formatted_json


def is_not_excluded_topic(topic_name):
    return topic_name not in excluded_topics()


def build_tree_without_excluded(node=MyNode, excluded_list_here=[]):
    new_parent_node = MyNode(node.topic_name)

    for original_child in node.children:
        if is_not_excluded_topic(original_child.topic_name):
            new_child = build_tree_without_excluded(original_child, excluded_list_here)
            new_parent_node.children.append(new_child)
    return new_parent_node


def collect_leaf_names(node=MyNode, all_included_leafs=[]):
    if len(node.children) == 0:
        all_included_leafs.append(node.topic_name)
    else:
        for child in node.children:
            collect_leaf_names(child, all_included_leafs)


def only_included_leafs(tree, excluded_list_here):
    tree_1 = build_tree_without_excluded(tree, excluded_list_here)
    result = []
    collect_leaf_names(tree_1, result)
    return result


