import ldaphelper

class Op:
    connection = None
    dn = 'ou=clients,o=gluu'
    def __init__(self, connection: ldaphelper.LdapConnector):
        self.connection = connection

    def get_op_by_display_name(self,displayName: str):
        op_client = self.connection.connect.search_s(
            self.dn,self.connection.searchScope,'displayName=%s' % displayName)
        return op_client[0]