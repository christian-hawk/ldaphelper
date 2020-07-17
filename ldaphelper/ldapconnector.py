import ldap
import ldap.modlist as modlist


class LdapConnector:
    searchScope = None
    connect = None

    def __init__(self, login, password):
        self.ldap_login = login
        self.password = password
        self.baseDN = "o=gluu"
        self.searchScope = ldap.SCOPE_SUBTREE
        self.open_connection()

    def open_connection(self):
        """Open connection with ldap server as self.connect"""
        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        self.connect = ldap.initialize("ldaps://localhost:1636")
        self.connect.set_option(ldap.OPT_DEBUG_LEVEL, 255)
        self.connect.protocol_version = ldap.VERSION2
        self.connect.simple_bind_s(self.ldap_login, self.password)

    def close_connection(self):
        """closes connection with ldap server"""
        self.connect.unbind_s()

    def get_user_by_uid(self, uid):
        """[Return complete user from server]

        Args:
            uid ([str]): [username]

        Returns:
            [class 'tuple']: [(dn, attrs)]
        """
        user = self.connect.search_s(
            self.baseDN,
            self.searchScope,
            "uid=%s" % uid,
            ["objectClass", "mail", "givenName", "sn", "uid", "inum"],
        )
        # user = self.connect.search_s(self.baseDN,self.searchScope,'uid=%s' % uid)
        return user[0]

    def create_user(self, uid, password, mail, givenName, sn):
        """creates user on server and returns created user

        Args:
            uid ([str]): [username]
            password ([str]): [password]
            mail ([str]): [primary email address]
            givenName ([str]): [first name]
            sn ([str]): [last name]

        Returns:
            [type]: [description]
        """
        attrs = {}
        attrs["objectClass"] = [
            "top".encode("utf-8"),
            "gluuCustomPerson".encode("utf-8"),
            "gluuPerson".encode("utf-8"),
        ]
        attrs["mail"] = mail.encode()
        attrs["givenName"] = givenName.encode()
        attrs["sn"] = sn.encode()
        attrs["uid"] = uid.encode()
        attrs["userPassword"] = password.encode()
        attrs["inum"] = self.get_random_inum().encode()
        attrs["displayName"] = ("%s %s" % (givenName, sn)).encode()
        attrs["gluuStatus"] = "active".encode()

        ldif = modlist.addModlist(attrs)
        modlist.addModlist()
        dn = "inum=%s,ou=people,o=gluu" % attrs["inum"].decode()

        self.connect.add_s(dn, ldif)
        generated_user = self.get_user_by_uid(uid)

        return generated_user

    # def get_random_inum(self):
    #     """[Generates a fake random inum, aplhanumeric 30 digits]

    #     Returns:
    #         [str]: [30 digit alphanumeric string to be used as inum]
    #     """
    #     letters_and_digits = string.ascii_letters + string.digits
    #     fake_inum = ''.join((random.choice(letters_and_digits) for i in range(30)))
    #     return fake_inum

    def delete_user(self, inum: str):
        dn = "inum=%s,ou=people,o=gluu" % inum
        self.connect.delete_s(dn)


# zero = 'inum=76bc7475-1bbe-4677-9496-3bee197a9ccd,ou=people,o=gluu'
# one = {'objectClass': [b'top', b'gluuCustomPerson', b'gluuPerson'],
# 'mail': [b'admin@chris.gluuthree.org'],
# 'givenName': [b'Admin'],
# 'telephoneNumber': [b'555-1212'],
# 'middleName': [b'Admin'],
# 'phoneNumberVerified': [b'true'],
# 'inum': [b'76bc7475-1bbe-4677-9496-3bee197a9ccd'],
# 'preferredUsername': [b'admin'],
# 'nickname': [b'Admin'],
# 'gender': [b'male'],
# 'memberOf': [b'inum=60B7,ou=groups,o=gluu'],
# 'emailVerified': [b'true'],
# 'zoneinfo': [b'America/Los_Angeles'],
# 'displayName': [b'Default Admin User'],
# 'birthdate': [b'20170907123010.485Z'],
# 'c': [b'US'], 'gluuStatus': [b'active'], 'sn': [b'User'], 'picture': [b'https://www.gluu.org/wp-content/themes/gluu/images/gl.png'], 'profile': [b'https://www.facebook.com/gluufederation/'], 'website': [b'https://www.gluu.org/'], 'userPassword': [b'{SSHA}nf/wzapuLV2i6RgW+f3+wRUw0uY/jfpQ'], 'uid': [b'admin']})
# connector.close_connection()
# naming = connect.get_naming_contexts()
# print(naming)
# print('-------------------------------')
# print()
# print(connect.search_s(baseDN,searchScope,'displayName=josephdoe2'))
# connect.search(baseDN,searchScope,)
# connect.unbind_s()
# except ldap.LDAPError e:
#     print("LDAP ERROR!! " + e)
