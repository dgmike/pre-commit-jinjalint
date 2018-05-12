from jinjalint.lint import resolve_file_paths, lint
import jinjalint
 
def parse_issues():
    files = resolve_file_paths('.', extensions=['.html'])
    lint = lint(files, {})
    return sorted(lint, key=lambda i: (i.location.file_path, i.location.line))

def main():
    issues = [
        str(issue)
        for issue in
        parse_issues()
    ]
