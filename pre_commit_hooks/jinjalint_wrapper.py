from __future__ import print_function

from jinjalint.lint import resolve_file_paths, lint


def parse_issues():
    files = resolve_file_paths('.', extensions=['.html'])
    lint = lint(files, {})
    return sorted(lint, key=lambda i: (i.location.file_path, i.location.line))


def main():
    issues = parse_issues()
    for issue in issues:
        print(str(issue))
    return len(issues) == 0
    

if __name__ == '__main__':
    sys.exit(check_json())
