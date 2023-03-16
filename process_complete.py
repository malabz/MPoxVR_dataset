import sys

if __name__ == '__main__':
    seq = 0
    complete = 0
    partial = 0
    this_seq_complete = False
    g = open("MPoxBR(complete).fasta", "w")
    h = open("MPoxBR(incomplete).fasta", "w")
    c = open("complete.tsv", "w")
    o = open("incomplete.tsv", "w")
    c.writelines("Accession\tVirus strain name\tLocation\tHost\tVirus type\tNuc. completeness\n")
    o.writelines("Accession\tVirus strain name\tLocation\tHost\tVirus type\tNuc. completeness\n")
    with open('all_nucleotide.fasta') as f: # This file is downloaded from https://download.cncb.ac.cn/Genome/Viruses/Poxviridae/Monkeypox_virus/all_nucleotide.fasta
        for line in f:
            if(line[0] == '>'):
                seq += 1
                if(line.find("complete") != -1 and line[-8:-1] != ("partial") and line.find("ON669283.1") == -1):
                    print("Vaild Sequence, id = ", line[1:-1].replace("|", "\t"))
                    complete += 1
                    print(line[1:].replace("|", "\t"), file = c, end = '')
                    print(line, file = g, end = '')
                    this_seq_complete = True
                else:
                    partial += 1
                    print(line[1:].replace("|", "\t"), file = o, end = '')
                    print(line, file = h, end = '')
                    this_seq_complete = False
            else:
                if this_seq_complete:
                    print(line, file = g, end = '')
                else:
                    print(line, file = h, end = '')
    print("This file has {} sequences, (complete {}, partial {}).".format(seq, complete, partial), file = sys.stderr)
    # Then, please compress two fasta files using xz program