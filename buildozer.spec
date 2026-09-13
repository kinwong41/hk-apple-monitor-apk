[app]
title = HK Apple Monitor
package.name = hkapplemonitor
package.domain = com.kingsley.hkapple
source.dir =.
source.include_exts = py
version = 1.0
requirements = python3,kivy,aiohttp
orientation = portrait

[buildozer]
log_level = 2#data/images/original/*
#


#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#[app@demo]
#title = My Application (demo)
#
#[app:source.exclude_patterns@demo]
#images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#buildozer --profile demo android debug


[app:source.exclude_patterns]
venv
.buildozer
bin
*.log

# (str) Application versioning (method 1)
#version.regex = __version__ = ['"]([^'"]*)['"]
#version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
# version = 1.2.0

# (list) Application requirements
#   comma separated e.g. "requirements = sqlite3,kivy"
#requirements = python3,kivy

# (str) Custom source folders - default ["apps"] - includes only that, so an empty list should be the default if this is used ?
#source.dir = .

# (list) Source files to include (let empty to include all the files)
#source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg


# (str) If you want to embed a versioned copy of python, you can use this variable.
#    The build will embed a python binary as python<version> (ie: python3.8)
#    This variable only works with sdl2 bootstrap (i.e. not with webview or service_only)
#    The value can be e.g. 3.8, 3.9, 3.10, 3.11 etc.
#    For python3.11, you might need to use python3.12 as the recipe does not exist for 3.11 yet.
#    So if you want python 3.11, use python3.12 and buildozer will use 3.11 (yeah weird, but that's how it is)
#    Leave blank to use default version (3.10)
#    Note: you can also use python3.12.0 for example if you want to use a specific patch version
#    Note: if you leave it blank, it will use the default python version from python-for-android
#    Note: if you specify a version, make sure to have a recipe for it in python-for-android
#    e.g. python3.12
#    If you leave blank, it will default to 3.10
#    See https://github.com/kivy/python-for-android/tree/develop/pythonforandroid/recipes
#    for available recipes
#    For example python3.12 will use python3.11 recipe if 3.12 doesn't exist
#    So you can just use python3.12 for 3.11
#    For python3.12, you might need to use python3.12 as well (obviously)
#    Leave blank to use default
#    Example: python_version = 3.10
#python_version = 3.10

# (str) Application versioning (method 1)
#version.regex = __version__ = ['"]([^'"]*)['"]
#version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
# version = 1.2.0

# (list) Application requirements
#   comma separated e.g. "requirements = sqlite3,kivy"
#requirements = python3,kivy

# (str) Custom source folders - default ["apps"] - includes only that, so an empty list should be the default if this is used ?
#source.dir = .

# (list) Source files to include (let empty to include all the files)
#source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg


# (str) Application versioning (method 1)
#version.regex = __version__ = ['"]([^'"]*)['"]
#version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
# version = 1.2.0

# (list) Application requirements
#   comma separated e.g. "requirements = sqlite3,kivy"
#requirements = python3,kivy

# (str) Custom source folders - default ["apps"] - includes only that, so an empty list should be the default if this is used ?
#source.dir = .

# (list) Source files to include (let empty to include all the files)
#source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

[buildozer]
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin
