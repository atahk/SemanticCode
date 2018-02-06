#!/usr/bin/env python
# pylint: disable=I0011,C0103,C0326

import os.path
import shutil
import dill

# Languages are a tuple with a full name and a short name.
# LANGUAGES = [("Haskell", "hs"), ("Javascript", "js"), ("MATLAB", "m")]
LANGUAGES = [("Cpp", "cpp"), ("R", "r"), ("Rcpp", "rcpp")]

# The ligatures dict associated to each language full name a list of substitution tuples.
# A substitution tuple consists of a tuple of glyph names to match, a function from the
# glyph names to the substituted glyph, and a string of additional ignores. Most glyphs are
# named according to the characters they replace, hence we use `"_".join`, but others are
# given by a constant function of the form `lambda xs: "glyph_name"`.
LIGATURES = {
    "Haskell": [
        (("asterisk",   "asterisk", "asterisk"), "_".join,
         "    ignore sub slash asterisk' asterisk asterisk;\n"
         "    ignore sub asterisk' asterisk asterisk slash;\n"),
        (("colon",      "colon",    "colon"),   "_".join, ""),
        (("equal",      "equal",    "equal"),   lambda xs: "equivalence_3", ""),
        (("equal",      "equal",    "greater"), "_".join, ""),
        (("equal",      "less",     "less"),    "_".join, ""),
        (("greater",    "equal",    "greater"), "_".join, ""),
        (("greater",    "greater",  "equal"),   "_".join, ""),
        (("greater",    "greater",  "greater"), "_".join, ""),
        (("greater",    "greater",  "hyphen"),  "_".join, ""),
        (("hyphen",     "greater",  "greater"), "_".join, ""),
        (("hyphen",     "less",     "less"),    "_".join, ""),
        (("less",       "asterisk", "greater"), "_".join, ""),
        (("less",       "bar",      "greater"), "_".join, ""),
        (("less",       "dollar",   "greater"), "_".join, ""),
        (("less",       "equal",    "greater"), "_".join, ""),
        (("less",       "equal",    "less"),    "_".join, ""),
        (("less",       "hyphen",   "greater"), "_".join, ""),
        (("less",       "plus",     "greater"), "_".join, ""),
        (("less",       "less",     "less"),    "_".join, ""),
        (("period",     "period",   "period"),  "_".join, ""),
        (("plus",       "plus",     "plus"),    "_".join, ""),
        (("asterisk",   "greater"),             "_".join, ""),
        (("backslash",  "backslash"),           "_".join, ""),
        (("bar",        "bar"),                 "_".join, ""),
        (("bar",        "greater"),             "_".join, ""),
        (("colon",      "colon"),               "_".join, ""),
        (("equal",      "equal"),               lambda xs: "equal_2", ""),
        (("equal",      "greater"),             "_".join, ""),
        (("exclam",     "exclam"),              "_".join, ""),
        (("greater",    "greater"),             "_".join, ""),
        (("greater",    "hyphen"),              "_".join, ""),
        (("hyphen",     "greater"),             "_".join, ""),
        (("hyphen",     "less"),                "_".join, ""),
        (("less",       "asterisk"),            "_".join, ""),
        (("less",       "greater"),             "_".join, ""),
        (("less",       "bar"),                 "_".join, ""),
        (("less",       "hyphen"),              "_".join, ""),
        (("less",       "less"),                "_".join, ""),
        (("period",     "period"),              "_".join, ""),
        (("plus",       "plus"),                "_".join, ""),
        (("slash",      "equal"),               lambda xs: "not_equal_2", "")],
    "Javascript": [
        (("equal",      "equal",    "equal"),   lambda xs: "equivalence_3", ""),
        (("exclam",     "equal",    "equal"),   lambda xs: "not_equivalence_3", ""),
        (("greater",    "greater",  "greater"), "_".join, ""),
        (("less",       "less",     "less"),    "_".join, ""),
        (("bar",        "bar"),                 "_".join, ""),
        (("equal",      "equal"),               lambda xs: "equal_2", ""),
        (("equal",      "greater"),             "_".join, ""),
        (("exclam",     "equal"),               lambda xs: "not_equal_2", ""),
        (("greater",    "greater"),             "_".join, ""),
        (("less",       "less"),                "_".join, ""),
        (("plus",       "plus"),                "_".join, "")],
    "MATLAB": [
        (("equal",      "equal"),               lambda xs: "equal_2",     ""),
        (("asciitilde", "equal"),               lambda xs: "not_equal_2", "")],
    "Cpp": [
        (("less",       "equal"),               lambda xs: "less_inequality", ""),
        (("greater",    "equal"),               lambda xs: "greater_inequality", ""),
        (("ampersand",  "ampersand"),           "_".join, ""),
        (("hyphen",     "greater"),             "_".join, ""),
        (("less",       "hyphen"),              "_".join, ""),
        (("colon",      "colon"),               "_".join, ""),
        (("bar",        "bar"),                 "_".join, ""),
        (("slash",      "slash"),               "_".join, ""),
        (("slash",      "asterisk"),            "_".join, ""),
        (("asterisk",   "slash"),               "_".join, ""),
        (("equal",      "equal"),               lambda xs: "equivalence_2", ""),
        (("exclam",     "equal"),               lambda xs: "not_equivalence_2", ""),
        (("greater",    "greater"),             "_".join, ""),
        (("less",       "less"),                "_".join, ""),
        (("plus",       "plus"),                "_".join, "")],
    "R": [
        (("period",     "period",   "period"),  "_".join, ""),
        (("colon",      "colon",    "colon"),   "_".join, ""),
        (("less",       "less",     "hyphen"),  "_".join, ""),
        (("less",       "equal"),               lambda xs: "less_inequality", ""),
        (("greater",    "equal"),               lambda xs: "greater_inequality", ""),
        (("ampersand",  "ampersand"),           "_".join, ""),
        (("hyphen",     "greater"),             "_".join, ""),
        (("less",       "hyphen"),              "_".join, ""),
        (("colon",      "colon"),               "_".join, ""),
        (("bar",        "bar"),                 "_".join, ""),
        (("numbersign", "numbersign"),          "_".join, ""),
        (("equal",      "equal"),               lambda xs: "equivalence_2", ""),
        (("exclam",     "equal"),               lambda xs: "not_equivalence_2", "")],
    "Rcpp": [
        (("equal",      "equal",    "equal"),   lambda xs: "equal_3", ""),
        (("exclam",     "equal",    "equal"),   lambda xs: "not_equal_3", ""),
        (("period",     "period",   "period"),  "_".join, ""),
        (("colon",      "colon",    "colon"),   "_".join, ""),
        (("less",       "equal",    "greater"), "_".join, ""),
        (("less",       "less",     "hyphen"),  "_".join, ""),
        (("asciitilde", "equal"),               lambda xs: "approx_2", ""),
        (("less",       "equal"),               lambda xs: "less_inequality", ""),
        (("greater",    "equal"),               lambda xs: "greater_inequality", ""),
        (("ampersand",  "ampersand"),           "_".join, ""),
        (("hyphen",     "greater"),             "_".join, ""),
        (("less",       "hyphen"),              "_".join, ""),
        (("colon",      "colon"),               "_".join, ""),
        (("bar",        "bar"),                 "_".join, ""),
        (("numbersign", "numbersign"),          "_".join, ""),
        (("slash",      "slash"),               "_".join, ""),
        (("slash",      "asterisk"),            "_".join, ""),
        (("asterisk",   "slash"),               "_".join, ""),
        (("equal",      "equal"),               lambda xs: "equivalence_2", ""),
        (("equal",      "greater"),             "_".join, ""),
        (("exclam",     "equal"),               lambda xs: "not_equivalence_2", ""),
        (("greater",    "greater"),             "_".join, ""),
        (("less",       "less"),                "_".join, ""),
        (("plus",       "plus"),                "_".join, "")],
}

# Unused ignores from Hasklig:
# ("slash", "asterisk") :
#    "    ignore sub slash' asterisk slash;\n"
#    "    ignore sub asterisk slash' asterisk;\n"
# ("asterisk", "slash") :
#    "    ignore sub slash asterisk' slash;\n"
#    "    ignore sub asterisk' slash asterisk;\n"
# ("asterisk", "asterisk") :
#    "    ignore sub slash asterisk' asterisk;\n"
#    "    ignore sub asterisk' asterisk slash;\n")

ROMAN_WEIGHTS = ["Black", "Bold", "ExtraLight", "Light", "Medium", "Regular", "Semibold"]
ITALIC_WEIGHTS = ["BlackIt", "BoldIt", "ExtraLightIt", "LightIt", "MediumIt", "It", "SemiboldIt"]


def to_rule(substitution_tuple):
    glyphs, replace_function, ignores = substitution_tuple
    length = len(glyphs)
    rule = ""
        
    # the rule starts out as a template with 0 standing for the combined glyph
    # and 1.. standing for the individual glyphs that are replaced
    if length == 2:
        rule = ("  lookup 1_2 {\n"
                "    ignore sub 1 1' 2;\n"
                "    ignore sub 1' 2 2;\n"
                + ignores +
                "    sub LIG 2' by 0;\n"
                "    sub 1'  2  by LIG;\n"
                "  } 1_2;\n\n")
    elif length == 3:
        rule = ("  lookup 1_2_3 {\n"
                "    ignore sub 1 1' 2 3;\n"
                "    ignore sub 1' 2 3 3;\n"
                + ignores +
                "    sub LIG LIG 3' by 0;\n"
                "    sub LIG  2' 3  by LIG;\n"
                "    sub 1'   2  3  by LIG;\n"
                "  } 1_2_3;\n\n")
    elif length == 4:
        rule = ("  lookup 1_2_3_4 {\n"
                "    ignore sub 1 1' 2 3 4;\n"
                "    ignore sub 1' 2 3 4 4;\n"
                + ignores +
                "    sub LIG LIG LIG 4' by 0;\n"
                "    sub LIG LIG  3' 4  by LIG;\n"
                "    sub LIG  2'  3  4  by LIG;\n"
                "    sub 1'   2   3  4  by LIG;\n"
                "  } 1_2_3_4;\n\n")

    # since replacement glyph names can contain digits, perform the individual
    # substitutions first
    for i in range(0, length):
        rule = rule.replace(str(i+1), glyphs[i])

    rule = rule.replace(str(0), replace_function(glyphs))
    return rule


def generate_config_file(languages):
    with open('config.dill', 'w') as f:
        dill.dump({"LANGUAGES": languages,
                   "LIGATURES": LIGATURES,
                   "ITALIC_WEIGHTS": ITALIC_WEIGHTS,
                   "ROMAN_WEIGHTS": ROMAN_WEIGHTS,
                  }, f)


def generate_ligature_files(languages):
    for full_name, short_name in languages:
        with open("ligatures.%s.fea" % short_name, 'w') as f:
            f.write("feature calt {\n")
            f.writelines([to_rule(ligature) for ligature in LIGATURES[full_name]])
            f.write("} calt;\n")


def generate_fontinfo_files(languages):
    fontinfo_file = "fontinfo.plist"
    generic_file = "fontinfo.generic.plist"
    for weight in ROMAN_WEIGHTS:
        generic_info_file = "Roman/%s/font.ufo/%s" % (weight, generic_file)
        if not os.path.exists(generic_info_file):
            basic_info_file = "Roman/%s/font.ufo/%s" % (weight, fontinfo_file)
            shutil.copy(basic_info_file, generic_info_file)
        with open(generic_info_file, 'r') as f:
            generic_info = f.read()

        for full_name, short_name in languages:
            language_info_file = "Roman/%s/font.ufo/fontinfo.%s.plist" % (weight, short_name)
            with open(language_info_file, 'w') as f:
                f.write(generic_info.replace("SemanticCode", "Semantic%s" % full_name))

    for weight in ITALIC_WEIGHTS:
        generic_info_file = "Italic/%s/font.ufo/%s" % (weight, generic_file)
        if not os.path.exists(generic_info_file):
            basic_info_file = "Italic/%s/font.ufo/%s" % (weight, fontinfo_file)
            shutil.copy(basic_info_file, generic_info_file)
        with open(generic_info_file, 'r') as f:
            generic_info = f.read()

        for full_name, short_name in languages:
            language_info_file = "Italic/%s/font.ufo/fontinfo.%s.plist" % (weight, short_name)
            with open(language_info_file, 'w') as f:
                f.write(generic_info.replace("SemanticCode", "Semantic%s" % full_name))


def generate_fontmenunamedbs(languages):
    with open('FontMenuNameDB.generic', 'r') as f:
        fontmenunamedb = f.read()

    for full_name, short_name in languages:
        with open('FontMenuNameDB.%s' % short_name, 'w') as f:
            f.write(fontmenunamedb.replace("SemanticCode", "Semantic%s" % full_name))


if __name__ == "__main__":

    enabled = LANGUAGES

    print "Configuring Semantic Fonts..."
    print "    Languages enabled: %s" % ", ".join([fn for fn, sn in enabled])

    generate_config_file(enabled)
    generate_fontinfo_files(enabled)
    generate_fontmenunamedbs(enabled)
    generate_ligature_files(enabled)

    print "Done"
