from dataclasses import dataclass
from typing import Dict, Generic, List, Mapping, Optional, TypeVar, Any
from collections import defaultdict
import itertools

from talon import actions
from talon import Module
import re

from .extensions import file_extensions
from .numbers import digits_map, teens, scales, tens
from .abbreviate import abbreviations
from .keys import symbol_key_words

import user.knausj_talon.code.create_spoken_forms

mod = Module()
