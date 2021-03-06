#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mbplot import *

def main(csv, ext="pdf", cmap="jet"):
    """Plot membench output as line plot and colormap

    Args:
        csv: Base name of CSV file generated by membench
        cmap: Name of color map
    """
    df = pd.read_csv(csv+'.csv')

    plt.figure()
    heat_plot(df, cmap)
    add_critical_size(16)   # 64K L1
    add_critical_size(18)   # 256K L2
    add_critical_size(21)   # 3M L3
    add_critical_stride(5)  # 64B cache line
    add_critical_stride(12) # 4K page size
    add_critical_assoc(3)   # L1 and L3 assoc
    add_critical_assoc(9)   # TLB size
    plt.savefig(csv+'-heat.' + ext, bbox_inches='tight')


if __name__ == "__main__":
    main(*sys.argv[1:])
