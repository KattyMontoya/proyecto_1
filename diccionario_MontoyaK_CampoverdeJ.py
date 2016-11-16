Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> diccionario={'Katty':123456,'Jorge':789456,'Jordy':456789,'Toaza':159753,'Camilo':741369}
>>> diccionario['Guido']=456852
>>> diccionario
{'Guido': 456852, 'Katty': 123456, 'Toaza': 159753, 'Jordy': 456789, 'Camilo': 741369, 'Jorge': 789456}
>>> diccionario['Toaza']
159753
>>> list(diccionario.keys())
['Guido', 'Katty', 'Toaza', 'Jordy', 'Camilo', 'Jorge']
>>> sorted(diccionario.keys())
['Camilo', 'Guido', 'Jordy', 'Jorge', 'Katty', 'Toaza']
>>> 'Guido' in diccionario
True
>>> 'Katty' not in diccionario
False
>>> 
