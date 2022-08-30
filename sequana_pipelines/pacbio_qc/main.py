# -*- coding: utf-8 -*-
#
#  This file is part of Sequana software
#
#  Copyright (c) 2016 - Sequana Development Team
#
#  File author(s):
#      Thomas Cokelaer <thomas.cokelaer@pasteur.fr>
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/sequana/sequana
#  documentation: http://sequana.readthedocs.io
#
##############################################################################
import sys
import os
import argparse
import shutil
import subprocess

from sequana_pipetools.options import *
from sequana_pipetools.misc import Colors
from sequana_pipetools.info import sequana_epilog, sequana_prolog
from sequana_pipetools import SequanaManager

col = Colors()

NAME = "pacbio_qc"

class MyKrakenOptions():
    def __init__(self, group_name="section_kraken"):
        self.group_name = group_name

    def add_options(self, parser):
        group = parser.add_argument_group(self.group_name)

        group.add_argument("--do-kraken", action="store_true",
            default=False,
             help="""If this options is set and valid DB are provided, runs
                kraken taxonomy.""")

        group.add_argument("--kraken-databases", dest="kraken_databases", type=str,
            nargs="+", default=[],
            help="""Path to a valid set of Kraken database(s).
                If you do not have any, please see https://sequana.readthedocs.io
                or use sequana_taxonomy --download option.
                You may use several, in which case, an iterative taxonomy is
                performed as explained in online sequana documentation""")


class Options(argparse.ArgumentParser):
    def __init__(self, prog=NAME, epilog=None):
        usage = col.purple(sequana_prolog.format(**{"name": NAME}))
        super(Options, self).__init__(
            usage=usage,
            prog=prog,
            description="",
            epilog=epilog,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )
        # add a new group of options to the parser
        so = SlurmOptions()
        so.add_options(self)

        # add a snakemake group of options to the parser
        so = SnakemakeOptions(working_directory=NAME)
        so.add_options(self)

        so = InputOptions(input_pattern="*.bam", add_input_readtag=False)
        so.add_options(self)

        so = GeneralOptions()
        so.add_options(self)

        pipeline_group = self.add_argument_group("pipeline")

        so = MyKrakenOptions()
        so.add_options(self)

        self.add_argument("--run", default=False, action="store_true",
            help="execute the pipeline directly")

    def parse_args(self, *args):
        args_list = list(*args)
        if "--from-project" in args_list:
            if len(args_list)>2:
                msg = "WARNING [sequana]: With --from-project option, " + \
                        "pipeline and data-related options will be ignored."
                print(col.error(msg))
            for action in self._actions:
                if action.required is True:
                    action.required = False
        options = super(Options, self).parse_args(*args)
        return options


def main(args=None):

    if args is None:
        args = sys.argv

    # whatever needs to be called by all pipeline before the options parsing
    from sequana_pipetools.options import before_pipeline

    before_pipeline(NAME)

    # option parsing including common epilog
    options = Options(NAME, epilog=sequana_epilog).parse_args(args[1:])

    # the real stuff is here
    manager = SequanaManager(options, NAME)

    # create the beginning of the command and the working directory
    manager.setup()
    from sequana import logger

    # fill the config file with input parameters

    if options.from_project is None:
        cfg = manager.config.config

        cfg.input_directory = os.path.abspath(options.input_directory)
        cfg.input_pattern = options.input_pattern
        manager.exists(cfg.input_directory)
        # ------------------------------------- kraken
        if options.do_kraken is True:
            cfg.kraken.do = True
        else:
            cfg.kraken.do = False

        if options.kraken_databases:
            cfg.kraken.databases =  [os.path.abspath(x)
                                     for x in options.kraken_databases]
            for this in options.kraken_databases:
                manager.exists(this)
            # if a DB is provided, let us update this field:
            cfg.kraken.do = True

    # finalise the command and save it; copy the snakemake. update the config
    # file and save it.
    manager.teardown() 

    if options.run:
        subprocess.Popen(["sh", '{}.sh'.format(NAME)], cwd=options.workdir)

if __name__ == "__main__":
    main()
