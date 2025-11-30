import sys
import os
import re
from notebook.app import main

if __name__ == "__main__":
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])

    if "BUILD_WORKING_DIRECTORY" in os.environ:
        os.chdir(os.environ["BUILD_WORKING_DIRECTORY"])

    sys.exit(main())