
def check_application_name(app_name: str, env_name: str, key_name: str) -> bool:
    dataset = {
        'qa2' : {
            "AffiliateId" : [
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa2.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA2.xfinity.com',
            'Prodtest.Comcast.Ebiz.Order.Api.QA-2',
            'prodtest.comcast.learn.web.qa2',
            'Prodtest.Comcast.Mercury.Buyflow.Web-QA2',
            'prodtest.comcast.learn.api.qa2',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa2'],

            "ChannelName" : [
            'comcast.learn.api.qa2',
            'comcast.learn.web.qa2',		
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa2.xfinity.com',		
            'prodtest.comcast.ebiz.customer.api.QA2.xfinity.com',		
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa2',		
            'Prodtest.Comcast.Ebiz.Order.Api.QA-2',		
            'prodtest.comcast.learn.api.qa2',
            'Prodtest.Comcast.Mercury.Buyflow.Web-QA2',	
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa2',
            'Prodtest.Comcast.Myplan.Web-Qa2']
        }
    }

    return app_name in dataset[env_name][key_name]


def get_value_field(key_name: str, prod_or_pesudo: str) -> list:
    
    value_set = {
        'AffiliateId': {'prod': 'DOT_COM', 'pesudo' : 'DOT_COM-TEST'},
        'ChannelName': {'prod': 'WEB', 'pesudo' : 'TEST'},
        'ContentServiceEndpoint': {'prod': 'https://ctp-gateway-prod.ctp.comcast.net/', 'pesudo' : 'https://content-service-pseudo.r3.app.cloud.comcast.net/'},
        'LocalizationService': {'prod': 'https://ctp-api-gateway.ctp.comcast.net/sales/', 'pesudo' : 'https://ctp-api-gateway-pseudo.r3.app.cloud.comcast.net/sales/'},
        'PaymentService': {'prod': 'https://ctp-pci-gateway.ctp.comcast.net/sales/', 'pesudo' : 'https://ctp-api-gateway-pseudo.r3.app.cloud.comcast.net/sales/'},
        'SalesChannelManagementService': {'prod': 'https://ctp-api-gateway.ctp.comcast.net/sales/', 'pesudo' : 'https://ctp-api-gateway-pseudo.r3.app.cloud.comcast.net/sales/'},
        'BaseUrl': {'prod': 'https://crs.identity.xfinity.com', 'pesudo' : 'https://crs-st.identity.xfinity.com'},
        'Mercury-RedirectUrl': {'prod': 'https://approval.xfinity.com?crsid={0}&ref={2}&failoverUrl={1}', 'pesudo' : 'https://pseudo-approval.cws.xfinity.com/?crsid={0}&failoverUrl={1}&ref={2}'},
        'MyPlan-RedirectUrl': {'prod': 'approval.xfinity.com?crsid={0}&ref=buyflow&failoverUrl={1}', 'pesudo' : 'pseudo-approval.cws.xfinity.com/?crsid={0}&ref=buyflow&failoverUrl={1}'}
    }

    return value_set[key_name][prod_or_pesudo.lower()]