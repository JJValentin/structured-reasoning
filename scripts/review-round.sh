#!/usr/bin/env bash
# Run one fresh review. Dependencies: Python 3 and the selected reviewer CLI.
# Usage: review-round.sh <brief.md> <run-dir> <round:1-5> [codex|claude|opencode|cmd]
# REVIEW_MODEL: required exact model ID; no floating aliases.
# REVIEW_CMD: trusted shell command reading stdin/writing stdout; overrides the CLI.
# REVIEW_EFFORT: codex reasoning effort (default high).
# REVIEW_TIMEOUT: seconds (default 300). REVIEW_SCOPE: full or delta (default by round).
# Custom text commands must write their provider-reported model ID to the supplied
# REVIEW_IDENTITY_FILE, or emit Claude/OpenCode JSON containing model telemetry.
# REVIEW_MODEL is also exported to custom commands. No model is selected implicitly.
# Exit 0: verified review; 1: ERROR sentinel + receipt; 2: usage/allowance error.
set -uo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 2
exec python3 "$SCRIPT_DIR/review-support.py" run "$@"
