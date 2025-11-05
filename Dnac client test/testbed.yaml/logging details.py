# tests/utils.py
import logging

logger = logging.getLogger(__name__)

def log_result(test_name, result):
    """Log formatted test result"""
    if result == "PASS":
        logger.info(f"✅ {test_name}: PASSED")
    elif result == "FAIL":
        logger.error(f"❌ {test_name}: FAILED")
    else:
        logger.warning(f"⚠️ {test_name}: {result}")

def validate_output(output, keyword):
    """Check if expected keyword exists in command output"""
    return keyword.lower() in output.lower()
