from __future__ import print_function

from jinjalint.lint import resolve_file_paths, lint
import argparse

def parse_issues(filenames):
    files = resolve_file_paths(filenames, extensions=['.html'])
    lints = lint(files, {})
    return sorted(lints, key=lambda i: (i.location.file_path, i.location.line))


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Filenames pre-commit believes are changed'
    )
    args = parser.parse_args(argv)

    issues = parse_issues(args.filenames)
    for issue in issues:
        print(str(issue))
    return int(len(issues) > 0)


if __name__ == '__main__':
    exit(main())
