import shutil

import igittigitt


def copy_eb_files(src, dst, ebignroe_path):
    """ copy files from src to dst based on ebignore file
    """
    parser = igittigitt.IgnoreParser()
    parser.parse_rule_files("", ebignroe_path)
    shutil.copytree(src, dst, ignore=parser.shutil_ignore)
