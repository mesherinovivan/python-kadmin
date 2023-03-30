#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
from distutils.util import execute, newer
from distutils.spawn import spawn

#
# hack to support linking when running
#  python setup.py sdist
#

import os
del os.link

if newer('./src/getdate.y', './src/getdate.c'):
    execute(spawn, (['bison', '-y', '-o', './src/getdate.c', './src/getdate.y'],))

setup(name='python-kadmin',
      version='0.1.2c',
      description='Python module for kerberos admin (kadm5)',
      url='https://github.com/akostyuk/python-kadmin',
      download_url='https://github.com/akostyuk/python-kadmin/tarball/v0.1.2b',
      author='Russell Jancewicz',
      author_email='russell.jancewicz@gmail.com',
      license='MIT',
      zip_safe=False,
      ext_modules=[
          Extension(
              "kadmin",
              library_dirs=["/usr/local/opt/krb5/lib"],
              libraries=["krb5", "kadm5clnt", "kdb5"],
              # include_dirs=["/usr/include/", "/usr/include/et/"],
              sources=[
                  "src/kadmin.c",
                  "src/PyKAdminErrors.c",
                  "src/PyKAdminObject.c",
                  "src/PyKAdminIterator.c",
                  "src/PyKAdminPrincipalObject.c",
                  "src/PyKAdminPolicyObject.c",
                  "src/PyKAdminCommon.c",
                  "src/PyKAdminXDR.c",
                  "src/getdate.c"
                  ],
              extra_compile_args=["-v", "--std=gnu89"]
          ),
          Extension(
              "kadmin_local",
              library_dirs=["/usr/local/opt/krb5/lib"],
              libraries=["krb5", "kadm5srv", "kdb5"],
              sources=[
                  "src/kadmin.c",
                  "src/PyKAdminErrors.c",
                  "src/PyKAdminObject.c",
                  "src/PyKAdminIterator.c",
                  "src/PyKAdminPrincipalObject.c",
                  "src/PyKAdminPolicyObject.c",
                  "src/PyKAdminCommon.c",
                  "src/PyKAdminXDR.c",
                  "src/getdate.c"
                  ],
              define_macros=[('KADMIN_LOCAL', '')],
              extra_compile_args=["-v", "--std=gnu89"],
          )
      ],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: System Administrators",
          "Intended Audience :: Developers",
          "Operating System :: POSIX",
          "Programming Language :: C",
          "Programming Language :: Python",
          "Programming Language :: YACC",
          "License :: OSI Approved :: MIT License",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Systems Administration :: Authentication/Directory",
      ]
)

