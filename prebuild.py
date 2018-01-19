#!/usr/bin/env python
# pylint: disable=I0011,C0103,C0326

import subprocess
import io

if __name__ == "__main__":

    processes = []
    files = dict()
    for shape in ["RomanMasters/SourceCodePro.designspace", "ItalicMasters/SourceCodePro-It.designspace"]:
        files[shape] = io.open('build-instance-'+shape.split("/")[0]+'.log', mode='wt')
        p = subprocess.Popen(["makeInstancesUFO", "-d", shape],
                             bufsize=1, stdout=files[shape], stderr=files[shape])
        processes.append(p)

    for p in processes:
        p.wait()
