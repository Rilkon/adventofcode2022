import pathlib
import sys
import anytree

TOTAL = 70000000
REQUIRED = 30000000


def parse(parsedata):
    root = ElvNode("root")
    current_dir = root

    for line in parsedata.strip().splitlines()[1:]:
        # Ignore "$ ls" and "dir", create files when they appear and only create directories when cd'ing into them

        if line[0].isdigit():
            # Create a new file node in current directory
            filesize = int(line.split(" ")[0])
            filename = line.split(" ")[1]
            ElvNode(filename, filesize, "file", parent=current_dir)

            # Aggregate sizes while building the tree to avoid work when solving part1/part2
            temp = current_dir
            while temp:
                temp.size += filesize
                temp = temp.parent

        elif line.startswith("$ cd .."):
            # Change the current working directory to its parent
            current_dir = current_dir.parent

        elif line.startswith("$ cd "):
            # Create a new dir node in current directory and update the current directory
            directory = line.split(" ")[1]
            current_dir = ElvNode(directory, 0, "dir", parent=current_dir)

    return root


def print_tree(treeroot):
    # Just for a nice printout of the tree on the console
    for prefix, _, node in anytree.RenderTree(treeroot):
        treestr = f"{prefix}{node.name}, ({node.node_type}, size={node.size})"
        print(f"{treestr.ljust(8)}")


def part1(root):
    # Filesizes were aggregated on dir level while building the tree, just get back all dirs <= 100.000 here
    results = anytree.findall(root, filter_=lambda node: node.size <= 100000 and node.node_type == "dir")
    return sum(el.size for el in results)


def part2(root):
    # Find the smallest directory to delete that fulfills the space requirement
    result = anytree.findall(root, filter_=lambda node: node.size >= (
            REQUIRED - (TOTAL - root.size)) and node.node_type == "dir")
    return min(result, key=lambda x: x.size).size


# Inheriting from NodeMixin allows my own class to use all anytree features (https://anytree.readthedocs.io/)
class ElvNode(anytree.NodeMixin):
    def __init__(self, name, size=0, node_type="dir", parent=None, children=None):
        super(ElvNode).__init__()
        self.name = name
        self.size = size
        self.node_type = node_type
        self.parent = parent
        if children:
            self.children = children


def solve(puzzle):
    data = parse(puzzle)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
