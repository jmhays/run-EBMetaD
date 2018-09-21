#!/bin/bash
set -ev

pushd $HOME
 [ -d run_ebmetad ] || git clone --depth=1 --no-single-branch https://github.com/jmhays/run_ebmetad.git
 pushd run_ebmetad
  git branch -a
  git checkout master
  $PYTHON setup.py install
  $PYTHON -m pytest
 popd
popd
