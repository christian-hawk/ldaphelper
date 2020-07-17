# mock data

OP_STATIC_ATTRS = {
    "objectClass": ["top", "oxAuthClient"],
    "oxAuthScope": [
        "inum=F0C4,ou=scopes,o=gluu",
        "inum=C4F5,ou=scopes,o=gluu",
    ],
    "inum": "w124asdgggAGs",
}

ADD_OP_TEST_ARGS = {
    "oxAuthLogoutSessionRequired": False,
    "oxAuthTrustedClient": False,
    "oxAuthResponseType": "token",
    "oxAuthTokenEndpointAuthMethod": "client_secret_basic",
    "oxAuthRequireAuthTime": False,
    "oxAccessTokenAsJwt": False,
    "oxPersistClientAuthorizations": True,
    "oxAuthGrantType": "client_credentials",
    "oxAttributes":
    '{"tlsClientAuthSubjectDn":null,"runIntrospectionScriptBeforeAccessTokenAsJwtCreationAndIncludeClaims":false,"keepClientAuthorizationAfterExpiration":false}',
    "oxAuthAppType": "web",
    "oxDisabled": False,
    "oxIncludeClaimsInIdToken": False,
    "oxRptAsJwt": False,
    "displayName": "test-client2",
    "oxAuthClientSecret": "somecoolsecret",
    "oxAuthSubjectType": "pairwise",
}

MOCKED_SEARCH_S_VALID_RESPONSE = [(
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
)]

OP_ADD_OP_EXPECTED_RETURN = expected_created_op = (
    "inum=w124asdgggAGs,ou=clients,o=gluu",
    {
        "objectClass": [b"top", b"oxAuthClient"],
        "oxAuthLogoutSessionRequired": [b"false"],
        "oxAuthTrustedClient": [b"false"],
        "oxAuthScope":
        [b"inum=F0C4,ou=scopes,o=gluu", b"inum=C4F5,ou=scopes,o=gluu"],
        "oxAuthResponseType": [b"token"],
        "oxAuthTokenEndpointAuthMethod": [b"client_secret_basic"],
        "oxAuthRequireAuthTime": [b"false"],
        "oxAccessTokenAsJwt": [b"false"],
        "oxPersistClientAuthorizations": [b"true"],
        "oxAuthGrantType": [b"client_credentials"],
        "inum": [b"w124asdgggAGs"],
        "oxAttributes": [
            b'{"tlsClientAuthSubjectDn":null,"runIntrospectionScriptBeforeAccessTokenAsJwtCreationAndIncludeClaims":false,"keepClientAuthorizationAfterExpiration":false}'
        ],
        "oxAuthAppType": [b"web"],
        "oxIncludeClaimsInIdToken": [b"false"],
        "oxRptAsJwt": [b"false"],
        "oxDisabled": [b"false"],
        "displayName": [b"test-client2"],
        "oxAuthClientSecret": [b"somecoolsecret"],
        "oxAuthSubjectType": [b"pairwise"],
    },
)
