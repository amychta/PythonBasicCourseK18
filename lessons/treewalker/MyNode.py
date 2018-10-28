class MyNode(object):
    topic_name = None
    children = []

    def __init__(self, name):
        self.topic_name = name
        self.children = []

    def __str__(self):
        prefix = "{\"" + self.topic_name + "\": ["
        childen_str = ", ".join(str(x) for x in self.children)
        suffix = "]}"
        return prefix + childen_str + suffix
