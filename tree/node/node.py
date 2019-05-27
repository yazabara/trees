from __future__ import annotations

import uuid
from typing import List


class Node:

    def __init__(self, value: Node, parent=None, depth=0) -> None:
        self.id = uuid.uuid4()
        self.value = value
        self.parent = parent
        self.depth = depth
        self.children: List[Node] = []

    def __str__(self) -> str:
        return "Node(id: {}, value: {}, depth: {})".format(self.id, self.value, self.depth)
