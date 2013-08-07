from moderation import moderation
from moderation.moderator import GenericModerator
from backoffice.models import Work


class WorkModerator(GenericModerator):
    auto_approve_for_staff = False
    visibility_column = 'visible'

moderation.register(Work, WorkModerator)
