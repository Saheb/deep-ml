from collections import defaultdict

def byte_pair_encoding(corpus: dict, num_merges: int) -> list:
    """
    Train a BPE tokenizer on the given corpus.
    
    Args:
        corpus: Dictionary mapping space-separated token sequences to their frequencies.
                Example: {"l o w </w>": 5, "n e w </w>": 6}
        num_merges: Number of merge operations to perform.
    
    Returns:
        List of tuples, where each tuple contains the two tokens that were merged.
        Example: [('l', 'o'), ('lo', 'w')]
    """
    res = []
    curr = corpus
    for _ in range(num_merges):
        c = defaultdict(int)
        for k, v in curr.items():
            tokens = k.split(" ")
            for i in range(len(tokens)-1):
                c[(tokens[i], tokens[i+1])] += v

        items = sorted(c.items(), key=lambda t: t[1], reverse=True)

        # print(items)
        res.append(items[0][0])
        
        new_curr = {}

        for k, v in curr.items():
            newk = ''
            tokens = k.split(" ")
            i = 0
            while i < len(tokens)-1:
                # print(i)
                if (tokens[i], tokens[i+1]) == items[0][0]:
                    newk += tokens[i] + tokens[i+1]
                    i = i + 2
                else:
                    newk += tokens[i]
                    i = i + 1
                newk += ' '

            if i == len(tokens)-1:
                new_curr[newk + tokens[i]] = v
            else:
                new_curr[newk[:-1]] = v

        # print(new_curr) 
        curr = new_curr
       
    return res

