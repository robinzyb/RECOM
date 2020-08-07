import argparse
import sys
from reweight.reweight import reweight_run
from reweight.utils.tools import ipi_extra

def main():
    print("Description\n------------")
    parser = argparse.ArgumentParser(description="""
    reweight is a convenient script to reweight the quantity from commitee
    potential, to view the sub-command help,  type "reweight sub-command -h.
    the potentials stored must be eV unit""")

    subparsers = parser.add_subparsers()
    # run
    parser_run = subparsers.add_parser(
            "run", help="main function to reweight the quantity")
    parser_run.add_argument('CONFIG', type=str,
            help="parameter file, json format")
    parser_run.set_defaults(func=reweight_run)

    # tools
    parser_tools = subparsers.add_parser(
            "extract", help="extract the potential from ipi extra file")
    parser_tools.add_argument("ipi_extra_file", type=str,
            help="ipi raw extra file")
    parser_tools.add_argument("pot_num", type=int,
            help="the number of potential in committee")
    parser_tools.add_argument("--factor", nargs="?", const=1.0,
            type=float, help="conversion factor used to change the unit of energy")
    parser_tools.set_defaults(func=ipi_extra)



    args = parser.parse_args()

    try:
        getattr(args, "func")
    except AttributeError:
        parser.print_help()
        sys.exit(0)

    args.func(args)

if __name__ == "__main__":
    main()
