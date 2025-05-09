def read_seqs_from_csv(file) -> list[str]:
    """
    Reads protein sequences from a specific file.
    Should be edited depending on how sequences are stored in your file.
    :param file: The file with your sequences
    :return: List of sequences
    """
    seqs = []

    with open(file) as f:
        lines = f.readlines()
        # print(lines[:10])
        seqs = [line.split(",")[1] for line in lines[1:]]

    return seqs

def edit_seq_list(seq_list: list[str],
                  remove_ncAA: bool = True,
                  keep_within: list[int] = [-1]) -> list[str]:
    """
    Edits list of sequences to remove problematic sequences.
    :param seq_list: List of sequences
    :param keep_within: Keep all sequences of length L within range [x, y] inclusive. ([-1]) includes all.
    :return: Cleaned list of sequences
    """
    seqs = []
    for seq in seq_list:
        L = len(seq)
        if remove_ncAA and not contains_ncAA(seq):
            seqs.append(seq)
        if keep_within != [-1] and (L >= keep_within[0] and L <= keep_within[1]):
            seqs.append(seq)

    return seqs

def contains_ncAA(seq: str) -> bool:
    """
    Checks a sequence (str) to see if it contains any ncAAs.
    :param seq: The sequence to check
    :return: True if contains ncAA, False otherwise.
    """
    amino_acids = {'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I',
                   'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'}
    for aa in seq:
        if aa not in amino_acids:
            return True

    return False


if __name__ == "__main__":
    # testing
    all_seqs = read_seqs_from_csv("pdb_redesigned.csv")
    edited_list = edit_seq_list(all_seqs, remove_ncAA=True)

    # training factor
    train_percent = 0.8
    print(len(all_seqs[:]))

