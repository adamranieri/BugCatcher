from enum import Enum


class Level(str,Enum):
    LOW = "Low"
    MED = "Medium"
    HIGH = "High"

class TestResult(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    FLAKY = "FLAKY"
    UNEXECUTED = "UNEXECUTED"

class TestType(str, Enum):
    PERFORMANCE = "PERFORMANCE"
    ACCEPTANCE = "ACCEPTANCE"
    FUNCTIONAL = "FUNCTIONAL"
    REGRESSION = "REGRESSION"
    RETESTING = "RETESTING"

class TestLevel(str, Enum):
    UNIT = "UNIT"
    INTEGRATION = "INTEGRATION"
    SYSTEM = "SYSTEM"
    ACCEPTANCE = "ACCEPTANCE"

class DefectStatus(str, Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    FIXED = "Fixed"
    DECLINED = "Declined"
    SHELVED = "Shelved"