def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra={'city':'shanghai','job':'qa'}

person('wixshq',23,**extra)

