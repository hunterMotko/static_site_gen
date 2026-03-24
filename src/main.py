import os
import sys
import shutil
from copy_recursive import copy_files_recursive
from page_gen import generate_pages_recursive


def main():
    dir_path_static = "./static"
    dir_path_public = "./docs"
    content_dir = "./content"
    template_file = "./template.html"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_files_recursive(dir_path_static, dir_path_public)
    generate_pages_recursive(content_dir, template_file,
                             dir_path_public, basepath)


if __name__ == "__main__":
    main()
