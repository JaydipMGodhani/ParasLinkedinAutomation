"""
Project Paras application settings.
Safe Phase 1: collect market intelligence only. No job submissions.
"""

JOB_SITE = "linkedin"
MAX_APPLIES_NUM = 5
HEADLESS_MODE = False
DEBUG_MODE = False

# Never mass-apply indiscriminately.
MONKEY_MODE = False

# Phase 1: collect suitable jobs + skill statistics only.
TEST_MODE = False
COLLECT_INFO_MODE = True

UPLOAD_RESUME = True
EASY_APPLY_ONLY_MODE = True
LINKEDIN_RECOMMENDED_JOBS_MODE = False
LINKEDIN_TOP_APPLICANT_JOBS_MODE = False
RESTART_EVERY_DAY = False

# Leave empty during collect-only phase.
READY_MADE_RESUME_PATH = ""
READY_MADE_PHOTO_PATH = ""
RESUME_STYLE = "FAANGPath"

# High-quality matching over volume.
JOB_IS_INTERESTING_THRESH = 80
MINIMUM_WAIT_TIME_SEC = 10

FREE_TIER = False
FREE_TIER_RPM_LIMIT = 15
DASHBOARD_OUTPUT_APP_LOGS = True
MINIMUM_LOG_LEVEL = "INFO"

# Keep upstream defaults initially. API key/provider configuration stays local in .env.
LLM_MODEL_TYPE = "openrouter"
EASY_APPLY_MODEL = "google/gemini-3.1-flash-lite-preview"
APPLY_AGENT_MODEL = "google/gemini-3.1-flash-lite-preview"
TEMPERATURE = 0.2
