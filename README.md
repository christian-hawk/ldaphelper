# ldaphelper
[![Build Status](https://travis-ci.org/christian-hawk/ldaphelper.svg?branch=master)](https://travis-ci.org/christian-hawk/ldaphelper) [![codecov](https://codecov.io/gh/christian-hawk/ldaphelper/branch/master/graph/badge.svg)](https://codecov.io/gh/christian-hawk/ldaphelper)


Wanna try to make it a little easier

```python
from ldaphelper import LdapConnection(), User

user = 'cn=directory manager'
password = 'amazingpassword'

con = LdapConnection(user,password)
ldp_user = User(con)

user = {
    "uuid" : "johndoe",
    "password" : "strongpassword,
    "mail" : "john.doe@ldaphelper.org",
    "givenName" : "John",
    "sn" : "Doe"
}

added_user = ldp_user.add_user(user)

```
