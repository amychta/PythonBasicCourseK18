from lessons.treewalker.MyNode import MyNode

def excluded_topics():
    return ["Obolonsky region", "Alaska", "Colorado", "Warsaw"]

def create_tree():
    world = MyNode("World")

    usa = MyNode("USA")
    ukraine = MyNode("Ukraine")
    poland = MyNode("Poland")

    alaska = MyNode("Alaska")
    washington = MyNode("Washington")
    colorado = MyNode("Colorado")

    kyiv = MyNode("Kyiv")
    lviv = MyNode("Lviv")
    poltava = MyNode("Poltava")

    obolonsky = MyNode("Obolonsky region")
    golosiivsky = MyNode("Golosiivsky region")

    katowice = MyNode("Katowice")
    warsaw = MyNode("Warsaw")

    world.children.append(ukraine)
    world.children.append(poland)
    world.children.append(usa)

    ukraine.children.append(kyiv)
    ukraine.children.append(lviv)
    ukraine.children.append(poltava)

    poland.children.append(katowice)
    poland.children.append(warsaw)

    usa.children.append(alaska)
    usa.children.append(washington)
    usa.children.append(colorado)

    kyiv.children.append(obolonsky)
    kyiv.children.append(golosiivsky)

    return world


