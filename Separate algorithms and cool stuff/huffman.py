import sys

text = 'never gonna give you up, never gonna let you down'

class Node:
  def __init__(self, _val, _left_child, _right_child):
    self.val = _val
    self.left_child = _left_child
    self.right_child = _right_child

def get_huffman_tree(text):
    """
    Builds Huffman tree for text using the Node class
    text: string
    """
    freq = _get_letter_freq(text)
    while len(freq) >= 3:
        lc = freq.pop()
        rc = freq.pop()
        val = lc[1] + rc[1]
        node = Node(val, lc[0], rc[0])
        _put_node_in_freq_list(node, freq)
    return Node('root', freq[0][0], freq[1][0])

def _get_letter_freq(text):
  """
    Returns a list of tuples where 1st elem is char from text, 
    2nd elem is its frequency in text, sorted by 2nd elem
    text: string
  """
  freq = {}
  for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
  sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
  return sorted_freq

def _put_node_in_freq_list(node, freq):
  """
    Inserts Node in sorted freq list based on node.val 
    node: Node
    freq: list
  """
  i = 0
  while i < len(freq) and freq[i][1] > node.val:
    i += 1
  freq.insert(i, [node, node.val])

def get_codes(node, path = [], codes = {}):
  """
    Returns a dictionary, keys - characters, vals - their (Huffman) code
  """
  if isinstance(node, str):
    codes[node] = list(path)
    return 
  if (node.left_child):
    path.append(0)
    get_codes(node.left_child, path, codes)
    path.pop()
  if (node.right_child):
    path.append(1)
    get_codes(node.right_child, path, codes)
    path.pop()
  return codes

def encode_text(text):
    """
        Uses Huffman Coding to encode given text
        Returns string
    """
    tree = get_huffman_tree(text)
    codes = get_codes(tree)
    encoded = [''.join(str(bit) for bit in codes[ch]) for ch in text]
    return ''.join(encoded)

encoded = encode_text(text)
tree = get_huffman_tree(text)

original_size_bits = len(text) * 8
encoded_size_bits = len(encoded)

print ('Encoded:', encoded)
print ('Encoded size:', encoded_size_bits, 'bits')
print ('Original size:', original_size_bits, 'bits')
print ('Improvement:', round(( encoded_size_bits / original_size_bits) * 100, 2), '% "better" than just using 8 bits per char')

def decode_text(tree, encoded): 
  """
    Decodes encoded text
    Returns string
    tree: Node
    encoded: string
  """
  encodedList = [int(bit) for bit in list(encoded)]
  text = []
  node = tree
  for bit in encodedList:
    if bit:
      node = node.right_child
    else:
      node = node.left_child
    if isinstance(node, str): 
        text.append(node)
        node = tree
  return ''.join(text)

decoded = decode_text(tree, encoded)
print ('Decoded: ', decoded)



