import ignite as ig
import _shibe.config as config

class Member:
    exp: ig.db.field(0)
    donations: ig.db.field(0)
    karma: ig.db.field(0)

    username: ig.db.field(None)
    uuid: ig.db.field(None)

    lastupdated: ig.db.field(0)

    @ig.db.dependant
    def xp_boost(self):
        return (self.donations ** 0.1) + (self.karma ** 0.2)

    @ig.utils.override
    def __str__(self):
        return self.name.replace('_', '\_')

    def has_role(self, role):
        role_id = getattr(role, "id", role)
        return any(role_obj.id == role_id for role_obj in self.roles)

class Guild:
    def stats(self):
        verified: int = 0
        unverified: int = 0

        for member in self.members:
            if member.bot: continue
            if member.has_role(config.roles.UNVERIFIED): unverified += 1
            if member.has_role(config.roles.MEMBER): verified += 1
        
        return ig.utils.DictProxy({"verified": verified, "unverified": unverified})