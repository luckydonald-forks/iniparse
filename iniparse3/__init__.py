# Copyright (c) 2001, 2002, 2003 Python Software Foundation
# Copyright (c) 2004-2008 Paramjit Oberoi <param.cs.wisc.edu>
# Copyright (c) 2007 Tim Lauridsen <tla@rasmil.dk>
# Copyright (c) 2018 luckydonald <https://github.com/luckydonald>
# All Rights Reserved.  See LICENSE-PSF & LICENSE for details.

from ini import INIConfig, change_comment_syntax
from config import BasicConfig, ConfigNamespace
from compat import RawConfigParser, ConfigParser, SafeConfigParser
from utils import tidy

try:
    # python 3
    from configparser import DuplicateSectionError, NoSectionError, NoOptionError, InterpolationMissingOptionError, InterpolationDepthError, InterpolationSyntaxError, DEFAULTSECT, MAX_INTERPOLATION_DEPTH
except ImportError:
    # python 2
    from ConfigParser import DuplicateSectionError, NoSectionError, NoOptionError, InterpolationMissingOptionError, InterpolationDepthError, InterpolationSyntaxError, DEFAULTSECT, MAX_INTERPOLATION_DEPTH
# end try

__all__ = [
    'BasicConfig', 'ConfigNamespace',
    'INIConfig', 'tidy', 'change_comment_syntax',
    'RawConfigParser', 'ConfigParser', 'SafeConfigParser',
    'DuplicateSectionError', 'NoSectionError', 'NoOptionError',
    'InterpolationMissingOptionError', 'InterpolationDepthError',
    'InterpolationSyntaxError', 'DEFAULTSECT', 'MAX_INTERPOLATION_DEPTH',
]


