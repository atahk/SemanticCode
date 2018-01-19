#!/usr/bin/env python
# pylint: disable=I0011,C0103,C0326

import subprocess
import io

if __name__ == "__main__":

    processes = []
    for shape in ["Roman", "Italic"]:
        with io.open('build-instance-'+shape+'.log', mode='wb') as out:
            p = subprocess.Popen(["makeInstancesUFO", "-d", shape+"Masters/SourceCodePro.designspace"], stdout=out, stderr=out)
            child_processes.append(p)
    for p in processes:
        p.wait()
