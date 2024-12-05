import argparse


def _gen_argparser():
    cmds = argparse.ArgumentParser(
        prog="cli-lib",
        description="CLI managed library",
    )

    cmds.add_argument(
        "-s",
        "--storage-path",
        default="db.json",
        help="Specify file for library storage, db.json",
    )
    
    action_cmds= cmds.add_subparsers(title="Available actions", dest="cmds")
    action_cmds.required = True
    
    create_cmd = action_cmds.add_parser("add", description="Add book")
    create_cmd.add_argument("--title", required=True)
    create_cmd.add_argument("--author", required=True)
    create_cmd.add_argument("--year", required=True)
    
    delete_cmd=action_cmds.add_parser("del", description="Delete book")
    delete_cmd.add_argument("--id", required=True)
    
    search_cmd = action_cmds.add_parser("search",description="Search book")
    search_cmd.add_argument("--title")
    search_cmd.add_argument("--author")
    search_cmd.add_argument("--year")
    
    show_cmd = action_cmds.add_parser("show", description="Show all books")
    
    change_status_cmd = action_cmds.add_parser("change_status", description="Change status of the book")
    change_status_cmd.add_argument("--id", required=True)
    change_status_cmd.add_argument("--status")
    
    
    
    

    return cmds


def parse_args():
    root_cmd = _gen_argparser()

    args = root_cmd.parse_args()

    return args
