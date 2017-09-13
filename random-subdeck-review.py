from anki.sched import Scheduler
from aqt.utils import showInfo

import random

def randomFillRev(self):
#    showInfo(str(len(self._revDids)))
    random.shuffle(self._revDids)
    obj = origFillRev(self)
#    showInfo(str(len(self._revQueue)))
#    random.shuffle(self._revQueue)
#    showInfo(str(len(self._revQueue)))
    return obj

origFillRev = Scheduler._fillRev
Scheduler._fillRev = randomFillRev