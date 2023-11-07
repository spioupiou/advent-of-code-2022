import re

with open("test_input.txt") as f:
    lines = f.readlines()


class Node:
    def __init__(self, is_file, path, parent, size=0, content=[]):
        self.is_file = is_file
        self.path = path
        self.parent = parent
        self.size = size
        self.content = content

    def add_content(self, folder):
        self.content.append(folder)

    def get_size(self):
        if self.is_file:
            return self.size
        size = self.size
        for sub in self.content:
            size += sub.get_size()
        self.size = size
        return self.size


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
for item in root.content:
    total += item.get_size()
print(total)
