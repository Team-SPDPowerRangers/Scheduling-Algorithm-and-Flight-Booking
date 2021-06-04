def encoding(text):
    n = len(text)
    # create list to store the frequency of each symbol
    freqs = {}

    # cycle to count frequencies
    for i in text:
        # every time when we need the symbol it increments
        if i in freqs:
            freqs[i] += 1
        # if no more such symbol meets frequency remains 1
        else:
            freqs[i] = 1


    probs = {}
    for i in freqs:
        probs[i] = round((freqs[i] / n), 3)

    # Creating class for tree node
    class Tree_Node(object):

        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right

        def children(self):
            return (self.left, self.right)

        def nodes(self):
            return (self.left, self.right)

        def __str__(self):
            return '%s_%s' % (self.left, self.right)

    # function of huffman codeng algorithm
    def Huffman_encode(node, left=True, binString=''):
        if type(node) is str:
            return {node: binString}
        (l, r) = node.children()
        tree = dict()
        tree.update(Huffman_encode(l, True, binString + '0'))
        tree.update(Huffman_encode(r, False, binString + '1'))
        return tree

    # sorting probabilities in descending order
    prob = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    nodes = prob
    # print(' ')

    # creating variables to count nodes and steps
    i = 1
    step = 1

    # loop for creating nodes
    while len(nodes) > 1:
        # (symbol, probability)
        (s1, p1) = nodes[-1]
        (s2, p2) = nodes[-2]
        nodes = nodes[:-2]
        node = Tree_Node(s1, s2)
        # print(f'Step {step}')
        # print(f'{Huffman_encode(node)} ')

        # print(f' Node {i}:  {s1} - sum({p1}) ')
        i = i + 1
        # print(f' Node {i}:  {s2} - sum({p2}) ')
        i = i + 1
        nodes.append((node, p1 + p2))

        # sorting nodes in desending order
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        step = step + 1
        # print(' ')

    huffman = Huffman_encode(nodes[0][0])
    a = ''
    codes = {}
    for (i, frequency) in prob:
        codes[i] = huffman[i]

    # loop that compares each symbol in the textwith the symbols in codes list
    for i in text:
        for j in codes:
            if i == j:
                # write to the file
                a = a + codes[j]
    return a,codes

