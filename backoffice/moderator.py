from moderation import moderation
from moderation.moderator import GenericModerator
from backoffice.models import Work


class WorkModerator(GenericModerator):
    auto_approve_for_staff = False

moderation.register(Work, WorkModerator)
