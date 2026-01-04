from enum import Enum


class AgentState(Enum):
    IDLE = "IDLE"
    VALIDATE = "VALIDATE"
    EXECUTE = "EXECUTE"
    VERIFY = "VERIFY"
    RECOVER = "RECOVER"
    CONFIRM = "CONFIRM"
    FAIL = "FAIL"
