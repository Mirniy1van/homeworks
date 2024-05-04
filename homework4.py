immutable_var = (1, 2, 3, True, 'a', 'b', [1, 2])
print(immutable_var)
immutable_var[6][0] = False  # Кортежи могут хранить списки, внутри которых можно менять значения.
# Но внутри кортежа значения постоянны
mutable_list = [1, 2, 3, 'string', False]
print(mutable_list)
