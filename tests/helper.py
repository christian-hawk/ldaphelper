# mock data

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
