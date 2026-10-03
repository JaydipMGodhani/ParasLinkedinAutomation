"""Project Paras safe-start configuration.

Map these values to the equivalent settings in the upstream
LinkedIn-AI-Job-Applier-Ultimate project after its source is copied here.
"""

JOB_SITE = "linkedin"

# Phase 1: market intelligence only.
COLLECT_INFO_MODE = True

# No application submission during initial validation.
TEST_MODE = False
MONKEY_MODE = False

EASY_APPLY_ONLY_MODE = True
MAX_APPLIES_NUM = 5
JOB_IS_INTERESTING_THRESH = 80
