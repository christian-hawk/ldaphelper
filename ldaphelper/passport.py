from ldaphelper.ldapconnector import LdapConnector
import json
import ldap.modlist as modlist

class Passport():
    def __init__(self,login,password):
        self.connection = LdapConnector(login, password)
        self.connection.open_connection()
        self.oxpassport = self.getOxPassport()
        self.gluuPassportConfiguration = self.oxpassport['gluuPassportConfiguration']
        self.objectClass = self.oxpassport['objectClass']
        self.ou = 'oxpassport'
        self.gpc_providers = self.get_gpc_providers()
        self.gpc_conf = self.get_gpc_conf()
        self.gpc_idp_init = self.get_gpc_idpInitiated()


    def getOxPassport(self) -> dict:

        oxpassport = self.connection.connect.search_s(
            self.connection.baseDN, self.connection.searchScope, 'ou=oxpassport')[0][1]
        return oxpassport


    def create_provider(self,provider: dict):
        dn = 'ou=oxpassport,ou=configuration,o=gluu'
        attr = {}
        attr['gluuPassportConfiguration'] = []


    def get_dict_gpc(self) -> dict:
        gpc = self.gluuPassportConfiguration[0].decode()
        gpc_dict = json.loads(gpc)
        return gpc_dict


    def set_gluuPassportConfiguration(self, dict_gpc: dict):
        self.gluuPassportConfiguration = dict_gpc.encode()


    def get_gpc_conf(self) -> dict:
        return self.get_dict_gpc()['conf']


    def get_gpc_idpInitiated(self) -> dict:
        return self.get_dict_gpc()['idpInitiated']


    def get_gpc_providers(self) -> list:
        return self.get_dict_gpc()['providers']


    def construct_gpc_dict(self) -> dict:
        gpc_dict = {}
        gpc_dict['conf'] = self.gpc_conf
        gpc_dict['idpInitiated'] = self.gpc_idp_init
        gpc_dict['providers'] = self.gpc_providers
        return gpc_dict

    def add_provider(self, provider_id: str, displayName: str, provider_type: str, mapping: str,
            passportStrategyId: str, enabled: bool, callbackUrl: str,
            requestForEmail: bool, emailLinkingSafe: bool, options: dict):

        provider = {}
        provider['id'] = provider_id
        provider['displayName'] = displayName
        provider['type'] = provider_type
        provider['mapping'] = mapping
        provider['passportStrategyId'] = passportStrategyId
        provider['enabled'] = enabled
        provider['callbackUrl'] = callbackUrl
        provider['requestForEmail'] = requestForEmail
        provider['emailLinkingSafe'] = emailLinkingSafe
        provider['options'] = options
        print("Adding provider")
        self.gpc_providers.append(provider)
        print("gpc_providers = " + str(self.gpc_providers))
        self.update_gluuPassportConfiguration()

    def update_gluuPassportConfiguration(self):
        dn = 'ou=oxpassport,ou=configuration,o=gluu'
        old_gpc = {'gluuPassportConfiguration' : self.gluuPassportConfiguration}

        new_gpc_dict = self.construct_gpc_dict()
        new_gpc_str = json.dumps(new_gpc_dict)

        new_gpc_byte = new_gpc_str.encode()

        new_gpc_list = []
        new_gpc_list.append(new_gpc_byte)

        new_gpc = {'gluuPassportConfiguration' : new_gpc_list}

        ldif = modlist.modifyModlist(old_gpc,new_gpc)

        self.connection.connect.modify_s(dn,ldif)








    # def set_gpc_providers(self, providers: list):
    #     gpc_dict = {}

    #     providers = []
    #     id = str
    #     displayName
    #     type
    #     mapping
    #     passportStrategyId
    #     enabled
    #     callbackUrl
    #     requestForEmail
    #     emailLinkingSafe
    #     options
