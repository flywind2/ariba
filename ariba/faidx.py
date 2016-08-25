import sys
import os
import pysam
import pyfastaq
from ariba import common


def write_fa_subset(seq_names, infile, outfile, samtools_exe='samtools', verbose=False, verbose_filehandle=sys.stdout):
    if not os.path.exists(infile + '.fai'):
        pysam.faidx(infile)

    f = pyfastaq.utils.open_file_write(outfile)
    for name in seq_names:
        print(pysam.faidx(infile, name), end='', file=f)
    pyfastaq.utils.close(f)

