from distutils.core import setup
import glob


import os


def find_data_files(source,target,patterns):
      """Locates the specified data-files and returns the matches
      in a data_files compatible format.
      source is the root of the source data tree.
      Use '' or '.' for current directory.
      target is the root of the target data tree.
      Use '' or '.' for the distribution directory.
      patterns is a sequence of glob-patterns for the
      files you want to copy.
      """
      if glob.has_magic(source) or glob.has_magic(target):
            raise ValueError("Magic not allowed in src, target")
      ret = {}
      for pattern in patterns:
            pattern = os.path.join(source,pattern)
            for filename in glob.glob(pattern):
                  if os.path.isfile(filename):
                        targetpath = os.path.join(target,os.path.relpath(filename,source))
                        path = os.path.dirname(targetpath)
                        ret.setdefault(path,[]).append(filename)
      return sorted(ret.items())
#Example:
setup(
      name="DDS Calculator",
      version="0.0.3",
      description="A cool little program to caluclate exact bag amounts in DDS",
      author="Dp",
      console=['main.py'],
      include=[]
      #data_files=find_data_files('images','',[
      #'bg.png',
      #'images/*',
      #]),
      )
      # Will copy data/README to dist/README, and all files in data/images/ to dist/images/
      # (not checking any subdirectories of data/images/)

"""data_files = [('Images', glob('Images/*.*')),
                            ]

#includes = ['win32com.decimal_23', 'datetime']
includes = []

excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses',  'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter', 'unittest']
packages = []

dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll','MSVCP90.dll']

setup(
    data_files = data_files,
    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 1,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },
    zipfile = None,
    windows = [filename]
    )"""

"""from distutils.core import setup
import py2exe
setup(console=['main.py'],
      version='0.0.2',
      description='A cool little program to caluclate exact bag amounts in DDS',
      author='Dp')"""
      #packages=['distutils', 'distutils.command', 'tkinter', 'PIL'])
      #package_dir='images')
