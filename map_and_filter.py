values = [x for x in range(0, 10)]
print(values)

mapped_values = list(map(lambda x: x ** 2, values))
print(mapped_values)


colors = {'red': 'FF0000', 'green': '00FF00', 'blue': '0000FF'}
color_values = list(map(lambda color: int(color, 16), colors.values()))
print(color_values)

# MAPPING: new iterable = function + old iterable

filtered_values = list(filter(lambda x: x % 3 == 0, values))
print(filtered_values)

logins = ['User1', 'User2', 'User3', 'User4', 'Admin', 'User5', 'User6']
filtered_logins = list(filter(lambda login: str(login).lower() == 'admin', logins))
admin = filtered_logins[0] if len(filtered_logins) > 0 else None    # conditional expression
print(admin)

# FILTERING: new iterable = function + old iterable



