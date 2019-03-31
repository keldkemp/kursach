import rules

# Detail about rule system: https://github.com/dfunckt/django-rules


@rules.predicate
def is_agent(user) -> bool:
    return user.is_agent


is_logged_agent = rules.is_authenticated & is_agent
is_logged_personnel = rules.is_authenticated & is_agent

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
