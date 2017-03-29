import string


if __name__ == "__main__":
    with open('words.txt') as f:
        words = [l.strip().strip(string.punctuation) for l in f if l.strip()]

    words = filter(lambda s: len(s) > 1, words)
    words = list(set(words))
    with open('cleaned-words.txt', 'w') as f:
        f.write('\n'.join(words))
