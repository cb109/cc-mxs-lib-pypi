import os


def init():
    packagedir = os.path.abspath(os.path.dirname(__file__))
    maxscriptfile = os.path.join(packagedir, "{{cookiecutter.name}}")
    importcommand = r'fileIn @"{0}"'.format(maxscriptfile)
    try:
        import MaxPlus
        MaxPlus.Core.EvalMAXScript(importcommand)
    except ImportError:
        try:
            from Py3dsMax import mxs
            mxs.fileIn(maxscriptfile)
        except ImportError:
            raise ImportError("Could not find a suitable "
                              "3ds Max Python backend.")