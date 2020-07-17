from unittest import TestCase
from unittest.mock import MagicMock, patch
import ldaphelper
from ldaphelper import op
from types import ModuleType
import inspect
import ldap
import helper


# helper
def get_Op_instance():
    """ Returns Op instance initialized with a mocked LdapConnection """
    connection = MagicMock(ldaphelper.ldapconnector.LdapConnector)
    connection.__setattr__("connect", ldap.ldapobject.SimpleLDAPObject)
    op_instance = op.Op(connection)

    return op_instance


class TestOp(TestCase):
    def setUp(self):
        # mocks
        self.op_instance = get_Op_instance()
        self.search_s = patch.object(
            self.op_instance.connection.connect,
            "search_s",
            return_value=helper.MOCKED_SEARCH_S_VALID_RESPONSE,
        )
        self.add_s = patch.object(
            self.op_instance.connection.connect,
            "add_s",
            return_value=helper.OP_ADD_OP_EXPECTED_RETURN,
        )

        self.search_s.start()
        self.add_s.start()

    def tearDown(self):
        self.search_s.stop()
        self.add_s.stop()

    def test_should_return_if_op_exists(self):
        self.assertTrue(hasattr(ldaphelper, "op"),
                        "ldaphelper does not have op attribute")

    def test_if_op_is_module(self):
        self.assertIsInstance(op, ModuleType, "op is not a module")

    def test_if_Op_exists(self):
        self.assertTrue(hasattr(op, "Op"), "Op does not exist in op")

    def test_if_Op_is_class(self):
        self.assertTrue(type(op.Op) is type, "Op is not type (not a Class)")

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
            "Op does not receive LdapConnector class as arg",
        )

    def test_if_Op_has_attr_connection(self):
        self.assertTrue(hasattr(op.Op, "connection"),
                        "Op has no attribute named connection")

    def test_if_connection_is_none(self):
        self.assertIsNone(op.Op.connection, "connection is not none")

    def test_if_init_Op_connection_sets_LdapConnector_instance(self):
        self.assertIsInstance(
            self.op_instance.connection,
            ldaphelper.ldapconnector.LdapConnector,
            "connection is not an instance of LdapConnector after __init__",
        )

    def test_if_get_op_by_display_name_exists_in_Op(self):
        self.assertTrue(hasattr(op.Op, "get_op_by_display_name"))

    def test_if_get_op_by_display_name_is_callable(self):
        self.assertTrue(
            callable(op.Op.get_op_by_display_name),
            "get_op_by_display_name is not callable",
        )

    def test_get_op_by_display_name_should_return_a_tuple(self):
        self.assertIsInstance(
            self.op_instance.get_op_by_display_name("test-client"),
            tuple,
            "get_op_by_display_name() does not return a list",
        )

    def test_if_Op_has_dn(self):
        self.assertTrue(hasattr(op.Op, "dn"), "Op does not have dn attribute")

    def test_if_dn_is_string(self):
        self.assertTrue(type(op.Op.dn) is str, "dn is not a string")

    def test_if_get_op_by_display_name_one_return_dict(self):
        """ get_op_by_display_name[1] """
        with patch.object(
                self.op_instance.connection.connect,
                "search_s",
                return_value=helper.MOCKED_SEARCH_S_VALID_RESPONSE,
        ):
            op_client = self.op_instance.get_op_by_display_name("test-client")
            self.assertTrue(
                type(op_client[1]) is dict,
                "get_op_by_display_name[1] is not a dict")

    def test_if_get_op_by_display_name_returns_valid_tuple(self):

        tp = self.op_instance.get_op_by_display_name("test-client")

        some_keys = [
            "objectClass",
            "oxAuthScope",
            "oxAuthTrustedClient",
            "oxAuthResponseType",
            "oxAuthTokenEndpointAuthMethod",
            "oxAuthRequireAuthTime",
            "oxAccessTokenAsJwt",
            "oxPersistClientAuthorizations",
            "oxAuthGrantType",
            "inum",
            "oxAttributes",
            "oxAuthAppType",
            "oxLastLogonTime",
            "oxDisabled",
            "oxIncludeClaimsInIdToken",
            "oxRptAsJwt",
            "displayName",
            "oxAuthClientSecret",
            "oxAuthSubjectType",
        ]

        self.assertTrue(
            set(some_keys).issubset(tp[1]),
            "search response[1] tuple does not have expected keys",
        )

    def test_if_add_op_exists(self):
        self.assertTrue(hasattr(op.Op, "add_op"))

    def test_if_add_op_is_callable(self):
        self.assertTrue(callable(op.Op.add_op), "add_op is not callable")

    def test_if_add_op_receives_needed_args(self):
        needed_args = [
            "self",
            "displayName",
            "oxAuthLogoutSessionRequired",
            "oxAuthTrustedClient",
            "oxAuthResponseType",
            "oxAuthTokenEndpointAuthMethod",
            "oxAuthRequireAuthTime",
            "oxAccessTokenAsJwt",
            "oxPersistClientAuthorizations",
            "oxAuthGrantType",
            "oxAttributes",
            "oxAuthAppType",
            "oxIncludeClaimsInIdToken",
            "oxRptAsJwt",
            "oxAuthClientSecret",
            "oxAuthSubjectType",
            "oxDisabled",
        ]
        method_args = inspect.getfullargspec(op.Op.add_op).args
        self.assertListEqual(needed_args, method_args)

    def test_if_add_op_returns_tuple(self):
        self.assertTrue(
            type(self.op_instance.add_op(**helper.ADD_OP_TEST_ARGS)) is tuple,
            "add_op does not return a tuple",
        )

    def test_if_add_op_returns_valid_op_attrs(self):
        valid_keys = []
        for key in helper.MOCKED_SEARCH_S_VALID_RESPONSE[0][1]:
            valid_keys.append(key)

        attrs = self.op_instance.add_op(**helper.ADD_OP_TEST_ARGS)[1]
        self.assertTrue(
            set(valid_keys).issubset(attrs),
            "add_op returning attrs do not have expected keys",
        )

    def test_if_add_op_calls_add_modlist_with_args(self):

        with patch.object(ldaphelper.ldapconnector.modlist,
                          "addModlist") as addModlist:

            self.op_instance.add_op(**helper.ADD_OP_TEST_ARGS)
            all_attrs = {
                "displayName":
                b"test-client2",
                "oxAuthLogoutSessionRequired":
                b"false",
                "oxAuthTrustedClient":
                b"false",
                "oxAuthResponseType":
                b"token",
                "oxAuthTokenEndpointAuthMethod":
                b"client_secret_basic",
                "oxAuthRequireAuthTime":
                b"false",
                "oxAccessTokenAsJwt":
                b"false",
                "oxPersistClientAuthorizations":
                b"true",
                "oxAuthGrantType":
                b"client_credentials",
                "oxAttributes":
                b'{"tlsClientAuthSubjectDn":null,"runIntrospectionScriptBeforeAccessTokenAsJwtCreationAndIncludeClaims":false,"keepClientAuthorizationAfterExpiration":false}',
                "oxAuthAppType":
                b"web",
                "oxIncludeClaimsInIdToken":
                b"false",
                "oxRptAsJwt":
                b"false",
                "oxAuthClientSecret":
                b"somecoolsecret",
                "oxAuthSubjectType":
                b"pairwise",
                "oxDisabled":
                b"false",
                "objectClass": [b"top", b"oxAuthClient"],
                "oxAuthScope": [
                    b"inum=F0C4,ou=scopes,o=gluu",
                    b"inum=C4F5,ou=scopes,o=gluu",
                ],
                "inum":
                b"w124asdgggAGs",
            }

            addModlist.assert_called_once_with(all_attrs)

    def test_if_add_op_calls_ldap_add_s(self):

        with self.add_s as add_s:

            self.op_instance.add_op(**helper.ADD_OP_TEST_ARGS)

            add_s.assert_called_once_with(
                "inum=w124asdgggAGs,ou=clients,o=gluu",
                [
                    ("displayName", b"test-client2"),
                    ("oxAuthLogoutSessionRequired", b"false"),
                    ("oxAuthTrustedClient", b"false"),
                    ("oxAuthResponseType", b"token"),
                    ("oxAuthTokenEndpointAuthMethod", b"client_secret_basic"),
                    ("oxAuthRequireAuthTime", b"false"),
                    ("oxAccessTokenAsJwt", b"false"),
                    ("oxPersistClientAuthorizations", b"true"),
                    ("oxAuthGrantType", b"client_credentials"),
                    (
                        "oxAttributes",
                        b'{"tlsClientAuthSubjectDn":null,"runIntrospectionScriptBeforeAccessTokenAsJwtCreationAndIncludeClaims":false,"keepClientAuthorizationAfterExpiration":false}',
                    ),
                    ("oxAuthAppType", b"web"),
                    ("oxIncludeClaimsInIdToken", b"false"),
                    ("oxRptAsJwt", b"false"),
                    ("oxAuthClientSecret", b"somecoolsecret"),
                    ("oxAuthSubjectType", b"pairwise"),
                    ("oxDisabled", b"false"),
                    ("objectClass", [b"top", b"oxAuthClient"]),
                    (
                        "oxAuthScope",
                        [
                            b"inum=F0C4,ou=scopes,o=gluu",
                            b"inum=C4F5,ou=scopes,o=gluu"
                        ],
                    ),
                    ("inum", b"w124asdgggAGs"),
                ],
            )
        # restarting
        self.add_s.start()

    def test_add_op_should_return_created_op(self):
        expected_created_op = (
            "inum=59376804-e84b-411a-9492-653d14e52c24,ou=clients,o=gluu",
            {
                "objectClass": [b"top", b"oxAuthClient"],
                "oxAuthLogoutSessionRequired": [b"false"],
                "oxAuthScope": [
                    b"inum=F0C4,ou=scopes,o=gluu",
                    b"inum=C4F5,ou=scopes,o=gluu",
                ],
                "oxAuthTrustedClient": [b"false"],
                "oxAuthResponseType": [b"token"],
                "oxAuthTokenEndpointAuthMethod": [b"client_secret_basic"],
                "oxAuthRequireAuthTime": [b"false"],
                "oxAccessTokenAsJwt": [b"false"],
                "oxPersistClientAuthorizations": [b"true"],
                "oxAuthGrantType": [b"client_credentials"],
                "inum": [b"59376804-e84b-411a-9492-653d14e52c24"],
                "oxAttributes": [
                    b'{"tlsClientAuthSubjectDn":null,"runIntrospectionScriptBeforeAccessTokenAsJwtCreationAndIncludeClaims":false,"keepClientAuthorizationAfterExpiration":false}'
                ],
                "oxAuthAppType": [b"web"],
                "oxLastLogonTime": [b"20200714072830.011Z"],
                "oxAuthClientSecretExpiresAt": [b"21200623000000.000Z"],
                "oxDisabled": [b"false"],
                "oxIncludeClaimsInIdToken": [b"false"],
                "oxRptAsJwt": [b"false"],
                "displayName": [b"test-client"],
                "oxAuthClientSecret": [b"gWxnjnUdCm8Rpc0WPmm9lQ=="],
                "oxAuthSubjectType": [b"pairwise"],
                "oxLastAccessTime": [b"20200714072830.011Z"],
            },
        )
        self.assertEqual(
            self.op_instance.add_op(**helper.ADD_OP_TEST_ARGS),
            expected_created_op,
            "add_op() is not returning created_op",
        )
