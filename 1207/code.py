import re
from collections import defaultdict 

with open('test_input.txt') as f:
  lines = f.readlines()

class Node:
  def __init__(self, is_dir, path, size = 0, content = []):
    self.is_dir = is_dir
    self.path = path
    self.size = size
    self.content = content
  
  def add_content(self, content):
    self.content.append(content)

current_folder = Node(True, '/')

for i, _ in enumerate(lines):
  mv_up = re.match(r'\$\scd\s\.\.', lines[i])
  if mv_up:
    current_folder.path = re.sub(r'\/[a-zA-Z]+\/$', '/', current_folder.path)
    continue

  cmd = re.match(r'\$\scd\s([a-zA-Z]+|\/)', lines[i])
  if cmd and cmd.group(1) != current_folder.path:
    current_folder = Node(True, current_folder.path + cmd.group(1) + "/")
    continue
  
  # file starts with digits (size)
  file = re.match(r'(\d+)\s(.+)', lines[i])
  if file:
    current_folder.add_content(Node(False, current_folder.path + file.group(2), file.group(1)))
    continue

  sub_folder = re.match(r'dir\s([a-zA-Z]+)', lines[i])
  if sub_folder:
    current_folder.add_content(Node(True, current_folder.path + sub_folder.group(1) + "/"))

total = 0
for node in current_folder.content:
  if not node.is_dir:
    print(node.path)
    total += int(node.size)

print(total)