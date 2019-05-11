import rules

# Detail about rule system: https://github.com/dfunckt/django-rules


@rules.predicate
def is_agent(user) -> bool:
    return user.is_agent


@rules.predicate
def is_manager(user) -> bool:
    return user.is_manager


is_logged_agent = rules.is_authenticated & is_agent
is_logged_manager = rules.is_authenticated & is_manager
is_logged_personnel = rules.is_authenticated & (is_agent | is_manager)

# Generic permission, can be used, until detailed are needed


rules.add_perm('client', is_logged_personnel)
rules.add_perm('client.add', is_logged_personnel)
rules.add_perm('client.edit', is_logged_personnel)
rules.add_perm('client.delete', is_logged_personnel)

rules.add_perm('realty', is_logged_personnel)
rules.add_perm('realty.add', is_logged_personnel)
rules.add_perm('realty.edit', is_logged_personnel)
rules.add_perm('realty.delete', is_logged_personnel)

rules.add_perm('profile', is_logged_personnel)

rules.add_perm('service', is_manager)
rules.add_perm('service.add', is_manager)
rules.add_perm('service.edit', is_manager)
rules.add_perm('service.delete', is_manager)

rules.add_perm('realty_type', is_manager)
rules.add_perm('realty_type.add', is_manager)
rules.add_perm('realty_type.edit', is_manager)
rules.add_perm('realty_type.delete', is_manager)

rules.add_perm('request', is_logged_personnel)
rules.add_perm('request.add', is_logged_personnel)
rules.add_perm('request.edit', is_logged_personnel)
rules.add_perm('request.delete', is_logged_personnel)
rules.add_perm('request.closed', is_logged_personnel)
