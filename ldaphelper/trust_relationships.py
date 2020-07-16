from .ldapconnector import LdapConnector
from .helper import get_random_inum
import subprocess
# @TODO test relationship creation.

class TrustRelationships():

    def __init__(self, connection: LdapConnector):
        self.connector = connection

    def get_tr_by_display_name(self,displayName):
        search_result = self.connector.connect.search_s(
            self.connector.baseDN,
            self.connector.searchScope,
            "displayName=%s" % displayName
        )
        return search_result[0]

    def create_tr(self,displayName: str,gluuEntityId: str, description: str,
            gluuReleasedAttribute: list, gluuProfileConfiguration: list, gluuSAMLspMetaDataFN: str,
            metadata: str, gluuSAMLspMetaDataSourceType: str = 'file',
            gluuSpecificRelyingPartyConfig: bool = True, gluuStatus: str = 'active',
            gluuSAMLmaxRefreshDelay='PT8H', gluuIsFederation: bool = False):


        attrs = {}
        attrs['objectClass'] = ['top', 'gluuSAMLconfig']
        attrs['gluuEntityType'] = 'Single SP'
        attrs['o'] = 'o=gluu'
        attrs['inum'] = get_random_inum()
        attrs['displayName'] = displayName
        attrs['gluuSAMLmaxRefreshDelay'] = gluuSAMLmaxRefreshDelay
        attrs['gluuStatus'] = gluuStatus
        attrs['gluuSpecificRelyingPartyConfig'] = gluuSpecificRelyingPartyConfig
        attrs['gluuEntityId'] = gluuEntityId
        attrs['gluuIsFederation'] = gluuIsFederation
        attrs['description'] = description
        attrs['gluuReleasedAttribute'] = gluuReleasedAttribute
        attrs['gluuProfileConfiguration'] = gluuProfileConfiguration
        attrs['gluuSAMLspMetaDataSourceType'] = gluuSAMLspMetaDataSourceType
        attrs['gluuSAMLspMetaDataFN'] = gluuSAMLspMetaDataFN

        self.__upload_metadata(gluuSAMLspMetaDataFN,metadata)



    # def test_upload(self):
    #     import ipdb; ipdb.set_trace()
    #     print("test")

    def __upload_metadata(self,file_name: str,metadata: str):
        f = open(file_name,"w+")
        f.write(metadata)
        f.close()

        subprocess.run(
            ["scp",file_name,"eland.christian@chris.gluutwo.org:/opt/gluu-server/opt/shibboleth-idp/metadata"],
            check=True
            )






    def createTr(self):
        import ipdb; ipdb.set_trace()
        pass

