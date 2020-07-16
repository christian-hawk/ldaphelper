from unittest import TestCase
from unittest import mock
from ldaphelper import ldapconnector
import sys
from types import ModuleType


class TestLdapConnector(TestCase):

    def test_ldap_exists(self):
        self.assertTrue(
            hasattr(ldapconnector, 'ldap')
        )

    def test_ldap_is_module(self):
        self.assertIsInstance(
            ldapconnector.ldap,
            ModuleType,
            'ldap is not a module'
        )
    def test_ldap_exists_as_module(self):
        self.assertIn(
            'ldap',
            sys.modules
        )

    def test_ldap_is_imported(self):
        self.assertTrue(
            (ldapconnector.ldap.__path__[0]).endswith('/ldap')
        )

    def test_if_LdapConnector_exists(self):
        self.assertTrue(
            hasattr(ldapconnector,'LdapConnector'),
            'There is no LdapConnector attr in ldapconnector'
        )

    def test_if_LdapConnector_is_class(self):
        self.assertTrue(
            type(ldapconnector.LdapConnector) is type,
            'LdapConnector is not type'
        )
