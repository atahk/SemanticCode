#!/usr/bin/env python
# pylint: disable=I0011,C0103,C0326


import errno
import os
import shutil
import subprocess
import argparse

import dill

ADD_SVG_SCRIPT = os.path.abspath("addSVGtable.py")
UVS = os.path.abspath("uvs.txt")

with open("config.dill", 'r') as f:
    CONFIG = dill.load(f)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def rm_f(path):
    try:
        os.remove(path)
    except OSError as e:
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred


def rm_rf(path):
    shutil.rmtree(path, ignore_errors=True)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Build font files')
    parser.add_argument('-t', '--target', metavar='dir', type=str,
                        default='target', required=False,
                        help='target directory for font files')
    args = parser.parse_args()
    target = os.path.expanduser(args.target).rstrip("/")

    rm_rf(target+"/")

    for full_name, short_name in CONFIG["LANGUAGES"]:
        otf_dir = "%s/%s/" % (target, short_name)
        mkdir_p(otf_dir)

        family_name = "Semantic%s" % full_name

        rm_f("ligatures.fea")
        shutil.copy("ligatures.%s.fea" % short_name, "ligatures.fea")

        for weight in CONFIG["ROMAN_WEIGHTS"]:
            rm_f("Roman/%s/font.ufo/fontinfo.plist" % weight)
            shutil.copy("Roman/%s/font.ufo/fontinfo.%s.plist" % (weight, short_name),
                        "Roman/%s/font.ufo/fontinfo.plist" % weight)

            output_file = os.path.join(
                otf_dir, "%s-%s.otf" % (family_name, weight))
            subprocess.call(["makeotf",
                             "-f", "Roman/%s/font.ufo" % weight,
                             "-r",
                             "-ci", UVS,
                             "-mf", "FontMenuNameDB.%s" % short_name,
                             "-o", output_file])
            rm_f("Roman/%s/current.fpr" % weight)
            subprocess.call([ADD_SVG_SCRIPT,
                             output_file,
                             "svg"])

        for weight in CONFIG["ITALIC_WEIGHTS"]:
            rm_f("Italic/%s/font.ufo/fontinfo.plist" % weight)
            shutil.copy("Italic/%s/font.ufo/fontinfo.%s.plist" % (weight, short_name),
                        "Italic/%s/font.ufo/fontinfo.plist" % weight)

            output_file = os.path.join(
                otf_dir, "%s-%s.otf" % (family_name, weight))
            subprocess.call(["makeotf",
                             "-f", "Italic/%s/font.ufo" % weight,
                             "-r",
                             "-ci", UVS,
                             "-mf", "FontMenuNameDB.%s" % short_name,
                             "-o", output_file])
            rm_f("Roman/%s/current.fpr" % weight)
            subprocess.call([ADD_SVG_SCRIPT,
                             output_file,
                             "svg"])
