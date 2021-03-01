#!/bin/bash

source ./env
BERNARD_SETTINGS_FILE=tests/settings.py

pytest -c pytest.init

TESTS_RESULTS=$?

if [ $TESTS_RESULTS -eq 0 ]; then
  echo "Test Correctly"
else
  echo "Test Failed"
fi
