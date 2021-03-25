# Copyright 2020 Planet Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test example scripts in this directory

This is not an example script. This is a pytest module that provides automated
testing of the example scripts in this directory to ensure they are always
up-to-date and run successfully.

YAY automated testing and up-to-date examples!
"""
import logging
from pathlib import Path
import runpy

import pytest

LOGGER = logging.getLogger(__name__)


# All python files in the current directory except this one
# ref: https://stackoverflow.com/a/56813896
SCRIPTS = [s for s in Path(__file__).parent.resolve().glob('*.py')
           if s.name != Path(__file__).name]


# use the script name in the test name
def idfn(script_path):
    return script_path.name


# run the script as __main__ and also provide a global
# that points to the test temporary download directory,
# to be used by the script for all downloads
@pytest.mark.parametrize('script', SCRIPTS, ids=idfn)
def test_example_script_execution(script, tmpdir):
    runpy.run_path(script,
                   run_name='__main__',
                   init_globals={'TEST_DOWNLOAD_DIR': str(tmpdir)})
