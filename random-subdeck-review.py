from anki.sched import Scheduler
from aqt.utils import showInfo

import random

def randomFillRev(self):
    self._resetRev() # We need to reset the _revDids, so it can pick a random card from all subdecks again.
    random.shuffle(self._revDids) # Shuffle the deck ids array, so it will pick a random one.
    obj = origFillRev(self)
    return obj

origFillRev = Scheduler._fillRev
Scheduler._fillRev = randomFillRev