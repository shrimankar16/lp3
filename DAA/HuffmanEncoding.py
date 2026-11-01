# Huffman Encoding using Greedy Strategy
#
# Greedy choice: always merge the two nodes with the lowest frequency first.
#
# Time Complexity : O(n log n) - n insertions/deletions on a min-heap
# Space Complexity: O(n)       - heap and code table store n entries

import heapq

# ── Node for the Huffman Tree ─────────────────────────────
class Node:
    def __init__(self, char, freq):
        self.char  = char   # character (None for internal nodes)
        self.freq  = freq   # frequency
        self.left  = None
        self.right = None

    # heapq compares nodes; define < so lower freq = higher priority
    def __lt__(self, other):
        return self.freq < other.freq


# ── Build Huffman Tree ────────────────────────────────────
def build_huffman_tree(freq_map):
    # Push all characters into a min-heap
    heap = [Node(ch, fr) for ch, fr in freq_map.items()]
    heapq.heapify(heap)

    # Greedy: keep merging the two smallest nodes until one tree remains
    while len(heap) > 1:
        left  = heapq.heappop(heap)   # smallest frequency
        right = heapq.heappop(heap)   # second smallest frequency

        # Create an internal node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left  = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]   # root of Huffman tree


# ── Generate Codes by traversing the tree ────────────────
def generate_codes(node, prefix="", codes={}):
    if node is None:
        return
    # Leaf node → assign code
    if node.char is not None:
        codes[node.char] = prefix if prefix else "0"  # single-char edge case
        return
    generate_codes(node.left,  prefix + "0", codes)
    generate_codes(node.right, prefix + "1", codes)
    return codes


# ── Encode the input string ───────────────────────────────
def huffman_encode(text):
    if not text:
        return "", {}

    # Build frequency map
    freq_map = {}
    for ch in text:
        freq_map[ch] = freq_map.get(ch, 0) + 1

    root  = build_huffman_tree(freq_map)
    codes = generate_codes(root, "", {})

    encoded = "".join(codes[ch] for ch in text)
    return encoded, codes


# ── Driver ────────────────────────────────────────────────
if __name__ == "__main__":
    text = input("Enter text to encode: ")

    encoded, codes = huffman_encode(text)

    print("\nCharacter Codes:")
    for ch, code in sorted(codes.items()):
        print(f"  '{ch}' : {code}")

    print(f"\nOriginal text  : {text}")
    print(f"Encoded output : {encoded}")
    print(f"\nOriginal bits  : {len(text) * 8}")
    print(f"Encoded bits   : {len(encoded)}")
