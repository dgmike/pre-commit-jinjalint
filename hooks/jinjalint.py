 import jinjalint
 
 def parse_issues():
    sorted(jinjalint.lint.lint(jinjalint.lint.resolve_file_paths('.', extensions=['.html']), {}), key=lambda i: (i.location.file_path, i.location.line))

 def main():
    issues = [
        str(issue)
        for issue in
        parse_issues()
    ]
 
