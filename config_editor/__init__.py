#    Copyright 2017 Alexey Stepanov aka penguinolog

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Config file editors."""

from __future__ import absolute_import

from .config_editor import ConfigEditor
from .json_editor import JsonEditor
from .yaml_editor import YamlEditor

__all__ = (
    "ConfigEditor",
    "JsonEditor",
    "YamlEditor"
)

__version__ = '0.9.2'
__author__ = "Alexey Stepanov <penguinolog@gmail.com>"
