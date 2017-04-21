#!/usr/bin/python
# -*- coding: utf-8 -*-

# paths
PATH_TO_CHROMIUM = '/home/shitong/Research/Release_old'
PATH_TO_URLFILE  = '../res/scanning_list'
PATH_TO_LOG      = '/tmp/adblock_trace.log'
PATH_TO_FILTERED_LOG = '/home/shitong/Research/JSPROJ/log/'
PATH_TO_STAT_FILE = '/home/shitong/Research/JSPROJ/total_stat'

# signals
SIGSUCCESS = 1
SIGFAIL    = 0

# keywords
NO_KEYWORDS = [
    'extensions::',
    'chrome-extension:',
    'v8',
]
YES_KEYWORDS = [
    'http'
]

# number of runs stuff
#NUM_OF_RUNS_W_AB = 2
#NUM_OF_RUNS_WO_AB = 2
NUM_OF_RUNS = 3
N_TOP_ALEXA = 1000

# flags
FLAG_W_AB = 0
FLAG_WO_AB = 1

# regex pattern to match log record
PATTERN_LOG = r'(\"http\S*\")\s(IF|THEN|ELSE)\s(\d*)(\s-1|)'
PATTERN_DIFF_REC = r'unmatched: pos (\"\S*\")(\d*)'

# position-wise flags
THIS_POS_ONLY_HAS_IF = 0
THIS_POS_HAS_IF_THEN = 1
THIS_POS_HAS_IF_ELSE = 2

# timeout for loading pages (by sec)
TIMEOUT_LOAD_W_AB = 100
TIMEOUT_LOAD_WO_AB = 30

TIMEOUT_WARMING = 5

# command switches for starting Chromium enabled/disabled
OPT_W_AB = ['--no-sandbox']
OPT_WO_AB = ['--no-sandbox', '--disable-extensions']

XVFB_PREF = "xvfb-run --server-args='-screen 0, 1024x768x24' "

# times of executing kill commands
KILL_TIMES = 5

# threshold parameters
DIFF_THRESHD_W_AB = 0
DIFF_THRESHD_WO_AB = 0

# fake header
FAKE_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
