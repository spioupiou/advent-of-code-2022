import re

with open("input.txt") as f:
    lines = f.readlines()

class Node:
    def __init__(self, is_file, path, parent, size=None, content=[]):
        self.is_file = is_file
        self.path = path
        self.parent = parent
        self.size = size
        self.content = content

    def add_content(self, folder):
        self.content.append(folder)

    def get_size(self):
        if self.size != None:
            return self.size
        size = 0
        for sub in self.content:
            size += sub.get_size()
        if size < 100_000:
          print(size)
        # if size >= 4_274_331:
        #   print(size)
        self.size = size
        return size
    
    def print_content(self):
        if self.is_file:
            return self.path + "\n"
        result = self.path + "\n"
        for sub in self.content:
            result = result + sub.print_content()
        return result

root = Node(is_file=False, path="/", parent=None)
current_folder = root

for i, _ in enumerate(lines):
    # move_up
    move_up_cmd = re.match(r"\$\scd\s\.\.", lines[i])
    if move_up_cmd:
        current_folder = current_folder.parent

    # move_down
    move_down_cmd = re.match(r"\$\scd\s([a-zA-Z]+)", lines[i])
    if move_down_cmd:
        current_path = current_folder.path + move_down_cmd.group(1) + "/"
        for item in current_folder.content:
            if item.path == current_path:
                current_folder = item
                break

    # add file to current_folder (file starts with their size)
    file = re.match(r"(\d+)\s(.+)", lines[i])
    if file:
        file_size, file_name = int(file.group(1)), file.group(2)
        current_folder.add_content(
            Node(
                is_file=True,
                path=current_folder.path + file_name,
                size=file_size,
                parent=current_folder,
            )
        )
        continue

    # add sub_folder to current_folder
    sub_folder = re.match(r"dir\s([a-zA-Z]+)", lines[i])
    if sub_folder:
        current_folder.add_content(
            Node(
                is_file=False,
                path=current_folder.path + sub_folder.group(1) + "/",
                content=[],
                parent=current_folder,
            )
        )

total = 0
# print(root.get_size())
30_000_000 - (70_000_000 - root.get_size())
# print(root.print_content())

## Part 1: 1915606
## Part 2: 5025657