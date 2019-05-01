from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "reverse_roman"
    FUNCTION_NAMES = {
        "python_3": "reverse_roman",
        "js_node": "reverseRoman"
    }
    ENV_COVERCODE = {
        
    }