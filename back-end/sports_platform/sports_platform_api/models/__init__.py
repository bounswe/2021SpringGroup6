"""
__init__ is created to use multiple model files.
https://docs.djangoproject.com/en/3.2/topics/db/models/#organizing-models-in-a-package
Import other models on this file
"""

from .user_models import User, SportSkillLevel, Follow, Block
from .sport_models import Sport
from .event_models import *
from .activity_stream_models import ActivityStream
from .badge_models import *
from .equipment_models import *
