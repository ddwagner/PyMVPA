# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the PyMVPA package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
""""""

import mvpa2

__docformat__ = 'restructuredtext'

parser_args = {
    'description':
"""Query various information about this PyMVPA installation. If no option is
given useful subset of the available information is printed."""
}

def setup_parser(parser):
    excl = parser.add_mutually_exclusive_group()
    excl.add_argument('--externals', action='store_true',
                        help='list status of external dependencies')
    if __debug__:
        excl.add_argument('--debug', action='store_true',
                          help='list available debug channels')
    excl.add_argument(
            '--learner-warehouse', action='store_true',
            help='list available algorithms in the learner warehouse')
    return parser

def run(args):
    if args.externals:
        print mvpa2.wtf(include=['externals'])
    elif args.debug:
        mvpa2.debug.print_registered()
    elif args.learner_warehouse:
        from mvpa2.clfs.warehouse import clfswh
        clfswh.print_registered()
    else:
        print mvpa2.wtf()
