import os
import re
import setuptools

from setuptools.command.sdist import sdist


projectname = "{{cookiecutter.name}}"
rootdir = os.path.abspath(os.path.dirname(__file__))


def get_version():
    """The actual version is part of the MAXScript backend file."""
    regex = r"version\s*=\s*\"(?P<version>\d{1}\.\d{1}\.\d{1})\"\s*"
    packagedir = os.path.join(rootdir, projectname)
    maxscriptfile = os.path.join(packagedir, projectname + ".ms")
    with open(maxscriptfile) as f:
        lines = f.readlines()
    for line in lines:
        match = re.match(regex, line.strip())
        if match:
            return match.group("version")



class CleanSdist(sdist):
    """Makes sure the source distribution package is *.pyc-free."""

    def remove_pyc_files(self):
        for root, dirs, files in os.walk(rootdir):
            for filename in files:
                name, ext = os.path.split(filename)
                if ext == ".pyc":
                    filepath = os.path.join(root, filename)
                    try:
                        os.remove(filepath)
                    except OSError:
                        pass

    def run(self):
        self.remove_pyc_files()
        sdist.run(self)


setuptools.setup(name=projectname,
                 version=get_version(),
                 description="{{cookiecutter.description}}",
                 long_description=open("README.rst").read(),
                 author="{{cookiecutter.author}}",
                 author_email="{{cookiecutter.author_email}}",
                 license=open("LICENSE.rst").read(),
                 packages=setuptools.find_packages(),
                 # While the MANIFEST.in tells sdist what to package,
                 # this will make sure it also gets installed when
                 # executing bdist_wheel by pip on the sdist package.
                 include_package_data=True,
                 package_data={"" : ["*.ms"]},
                 cmdclass={'sdist': CleanSdist})