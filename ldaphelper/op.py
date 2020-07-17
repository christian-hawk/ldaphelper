import ldaphelper
from ldaphelper.ldapconnector import modlist


class Op:
    connection = None
    dn = "ou=clients,o=gluu"

    def __init__(self, connection: ldaphelper.LdapConnector):
        self.connection = connection

    def get_op_by_display_name(self, displayName: str):
        """[Gets Open Id by display name]

        Args:
            displayName (str): [OP display name ]

        Returns:
            [tuple]: [returns tupple containing dn and attrs]
        """
        op_client = self.connection.connect.search_s(
            self.dn, self.connection.searchScope,
            "displayName=%s" % displayName)
        return op_client[0]

    def add_op(
        self,
        displayName: str,
        oxAuthLogoutSessionRequired: bool,
        oxAuthTrustedClient: bool,
        oxAuthResponseType: str,
        oxAuthTokenEndpointAuthMethod: str,
        oxAuthRequireAuthTime: bool,
        oxAccessTokenAsJwt: bool,
        oxPersistClientAuthorizations: bool,
        oxAuthGrantType: str,
        oxAttributes: str,
        oxAuthAppType: str,
        oxIncludeClaimsInIdToken: bool,
        oxRptAsJwt: bool,
        oxAuthClientSecret: str,
        oxAuthSubjectType: str,
        oxDisabled: bool = False,
    ):

        # set all attributes, boolean ones lowercase
        attrs = {}
        attrs["displayName"] = str(displayName).encode()
        attrs["oxAuthLogoutSessionRequired"] = (
            str(oxAuthLogoutSessionRequired).encode().lower())
        attrs["oxAuthTrustedClient"] = str(
            oxAuthTrustedClient).encode().lower()
        attrs["oxAuthResponseType"] = str(oxAuthResponseType).encode()
        attrs["oxAuthTokenEndpointAuthMethod"] = str(
            oxAuthTokenEndpointAuthMethod).encode()
        attrs["oxAuthRequireAuthTime"] = str(
            oxAuthRequireAuthTime).encode().lower()
        attrs["oxAccessTokenAsJwt"] = str(oxAccessTokenAsJwt).encode().lower()
        attrs["oxPersistClientAuthorizations"] = (
            str(oxPersistClientAuthorizations).encode().lower())
        attrs["oxAuthGrantType"] = str(oxAuthGrantType).encode()
        attrs["oxAttributes"] = str(oxAttributes).encode()
        attrs["oxAuthAppType"] = str(oxAuthAppType).encode()
        attrs["oxIncludeClaimsInIdToken"] = (
            str(oxIncludeClaimsInIdToken).encode().lower())
        attrs["oxRptAsJwt"] = str(oxRptAsJwt).encode().lower()
        attrs["oxAuthClientSecret"] = str(oxAuthClientSecret).encode()
        attrs["oxAuthSubjectType"] = str(oxAuthSubjectType).encode()
        attrs["oxDisabled"] = str(oxDisabled).encode().lower()

        static_attrs = {
            "objectClass": ["top".encode(), "oxAuthClient".encode()],
            "oxAuthScope": [
                "inum=F0C4,ou=scopes,o=gluu".encode(),
                "inum=C4F5,ou=scopes,o=gluu".encode(),
            ],
            "inum":
            "w124asdgggAGs".encode(),
        }

        attrs.update(static_attrs)
        all_attrs = attrs

        new_dn = "inum=%s,%s" % (static_attrs["inum"].decode(), self.dn)
        # create modification list
        ldif = modlist.addModlist(all_attrs)

        self.connection.connect.add_s(new_dn, ldif)
        created_op = self.get_op_by_display_name(attrs["displayName"].decode())
        return created_op
