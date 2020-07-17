from unittest import TestCase
from unittest.mock import MagicMock, patch
import ldaphelper
from ldaphelper import op
from types import ModuleType
import inspect
import ldap
import helper

ldap.initialize

# helper
def get_Op_instance():
    """ Returns Op instance initialized with a mocked LdapConnection """
    connection = MagicMock(ldaphelper.ldapconnector.LdapConnector)
    connection.__setattr__('connect',ldap.ldapobject.SimpleLDAPObject)
    #connection.connect.__setattr__('search_s','value')
    # connection.connect = MagicMock(ldaphelper.ldapconnector.LdapConnector.connect)
    #connection.searchScope = MagicMock(ldaphelper.ldapconnector.LdapConnector.searchScope)
    op_instance = op.Op(connection)
    # op_instance.connection.connect.search_s = MagicMock(
    #     op.Op.dn,ldaphelper.LdapConnector.searchScope,'displayName=%s' % 'test-client')
    return op_instance


class TestOp(TestCase):

    def test_should_return_if_op_exists(self):
        self.assertTrue(
            hasattr(ldaphelper, 'op'),
            'ldaphelper does not have op attribute'
        )

    def test_if_op_is_module(self):
        self.assertIsInstance(
            op,
            ModuleType,
            'op is not a module'
        )

    def test_if_Op_exists(self):
        self.assertTrue(
            hasattr(op, 'Op'),
            'Op does not exist in op'
        )

    def test_if_Op_is_class(self):
        self.assertTrue(
            type(op.Op) == type,
            'Op is not type (not a Class)'
        )

    def test_if_Op_receives_LdapConnector(self):
        """[Check if Op receives class LdapConnector as arg]
        """
        annotations = inspect.getfullargspec(op.Op).annotations
        annotations_values = []
        for key in annotations:
            annotations_values.append(annotations[key])
        self.assertIn(
            ldaphelper.ldapconnector.LdapConnector,
            annotations_values,
            'Op does not receive LdapConnector class as arg'
        )


    def test_if_Op_has_attr_connection(self):
        self.assertTrue(hasattr(op.Op,'connection'),
        'Op has no attribute named connection')

    def test_if_connection_is_none(self):
        self.assertIsNone(op.Op.connection, 'connection is not none')

    def test_if_init_Op_connection_sets_LdapConnector_instance(self):
        # import ipdb; ipdb.set_trace()
        op_instance = get_Op_instance()

        self.assertIsInstance(
            op_instance.connection,
            ldaphelper.ldapconnector.LdapConnector,
            'connection is not an instance of LdapConnector after __init__'
        )

    def test_if_get_op_by_display_name_exists_in_Op(self):
        self.assertTrue(hasattr(op.Op, 'get_op_by_display_name'))

    def test_if_get_op_by_display_name_is_callable(self):
        self.assertTrue(hasattr(op.Op.get_op_by_display_name, '__call__'),
            'get_op_by_display_name is not callable')

    # @patch.object(ldaphelper.LdapConnector.connect, 'search_s')
    def test_get_op_by_display_name_should_return_a_tuple(self):

        op_instance = get_Op_instance()
        with patch.object(op_instance.connection.connect, 'search_s',
            return_value = (helper.MOCKED_SEARCH_S_VALID_RESPONSE)):
            self.assertIsInstance(
                op.Op.get_op_by_display_name(op_instance,'test-client'),
                tuple,
                'get_op_by_display_name() does not return a list'
            )

    def test_if_Op_has_dn(self):
        self.assertTrue(hasattr(op.Op, 'dn'),
        'Op does not have dn attribute')

    def test_if_dn_is_string(self):
        self.assertTrue( type(op.Op.dn) == str,
        'dn is not a string')

    def test_if_get_op_by_display_name_one_return_dict(self):
        """ get_op_by_display_name[1] """
        # mocked
        op_instance = get_Op_instance()
        with patch.object(op_instance.connection.connect, 'search_s',
            return_value = (helper.MOCKED_SEARCH_S_VALID_RESPONSE)):
            op_client = op_instance.get_op_by_display_name('test-client')
            self.assertTrue(type(op_client[1]) == dict,'get_op_by_display_name[1] is not a dict')

    def test_if_get_op_by_display_name_returns_valid_tuple(self):
        op_instance = get_Op_instance()
        with patch.object(op_instance.connection.connect, 'search_s',
            return_value = (helper.MOCKED_SEARCH_S_VALID_RESPONSE)):

            tp = op_instance.get_op_by_display_name('test-client')

            some_keys = ['objectClass', 'oxAuthScope', 'oxAuthTrustedClient', 'oxAuthResponseType',
                'oxAuthTokenEndpointAuthMethod', 'oxAuthRequireAuthTime', 'oxAccessTokenAsJwt',
                'oxPersistClientAuthorizations', 'oxAuthGrantType', 'inum', 'oxAttributes', 'oxAuthAppType',
                'oxLastLogonTime', 'oxDisabled', 'oxIncludeClaimsInIdToken', 'oxRptAsJwt', 'displayName',
                'oxAuthClientSecret', 'oxAuthSubjectType']

            #import ipdb; ipdb.set_trace()
            self.assertTrue(set(some_keys).issubset(tp[1]),'search response[1] tuple does not have expected keys')




