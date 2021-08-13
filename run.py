#!/usr/bin/env ```python
# -*- coding: utf-8 -*-
import pytest

if __name__=='__main__':
  pytest.main(["--cov=./src/" ,"--cov-report=html","--cov-config=.coveragerc"] )


# pytest --doctest-modules --junitxml=junit/test-results.xml --cov=./code/ --cov-report=xml
