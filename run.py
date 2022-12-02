import sys
import os
from pathlib import Path
sys.path.insert(0, 'src')

def main(targets):
    if 'report' in targets:
        wd = str(Path(__file__).parent.absolute())
        build_path = wd + '/notebooks'
        notebook_path = wd + '/notebooks/report.ipynb'
        output_path = wd + '/bin/report.pdf'
        template_path = wd + '/notebooks/citations.tplx'
        
        args1 = [
            'nbconvert',
            notebook_path,
            '--to pdf',
            '--output ' + output_path,
            '--no-input',
            '--execute',
            '--Execute.Preprocessor.timeout=999999'
        ]
        
        command = 'cd ' + build_path + ' && jupyter ' + ' '.join(args1) + ' && cd ' + wd
        os.system(command)
        

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)