from enum import Enum

def make_status_enum():
    class Status(Enum):
        PENDING = 'PENDING'
        ACTIVE = 'ACTIVE'
        DONE = 'DONE'
    return Status
