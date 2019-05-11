import argparse
import subprocess
import os
def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    args = parser.parse_args(argv)
    files = "'" + "', '".join(args.filenames) + "'"
    if (len(files) > 0):
        subprocess.call(['Rscript', '--no-init-file', '-e', 'styler::style_file(' + files + ')'] , stdout=open(os.devnull, 'wb'))


if __name__ == '__main__':
    exit(main())