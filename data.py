
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
            'Prodtest.Comcast.Myplan.Web-Qa2'],

            #ContentServiceEndpoint
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa2.xfinity.com',	
            'prodtest.comcast.ebiz.customer.api.QA2.xfinity.com',	
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa2',	
            'Prodtest.Comcast.Ebiz.Order.Api.QA-2',	
            'prodtest.comcast.learn.api.qa2',	

            #Localization Service
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa2.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA2.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa2',
            'Prodtest.Comcast.Ebiz.Order.Api.QA-2',
            'prodtest.comcast.learn.api.qa2',

            #PaymentService
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa2.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA2.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa2',
            'Prodtest.Comcast.Ebiz.Order.Api.QA-2',
            'prodtest.comcast.learn.api.qa2',

            #SalesChannelManagementService
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa2.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA2.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa2',
            'Prodtest.Comcast.Ebiz.Order.Api.QA-2',
            'prodtest.comcast.learn.api.qa2',

            #BaseUrl    
            'Prodtest.Comcast.Mercury.Buyflow.Web-QA2',
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa2',
            'Prodtest.Comcast.Myplan.Web-Qa2',
            'ProdTest.Comcast.Myplan.Web.Omni-Qa2',

            #Mercury RedirectUrl
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa2',
            'Prodtest.Comcast.Mercury.Buyflow.Web-QA2',

            #MyPlan RedirectUrl    
            'Prodtest.Comcast.Myplan.Web-Qa2',
            'ProdTest.Comcast.Myplan.Web.Omni-Qa2'

        },
        'qa4' : [
             #AffiliateId
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa4.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA4.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa4',
            'prodtest.Comcast.Ebiz.Order.Api.Qa-4',
            'prodtest.comcast.learn.api.qa-4',
            'prodtest.comcast.learn.web.qa-4',
            'prodtest.delivery.qa4.xfinity.com',
            'prodtest.www.qa4.comcast.com',
            'www.qa4.comcast.com',     

            #ChannelName
            'comcast.learn.api.qa-4',
            'comcast.learn.web.qa-4',		
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa4.xfinity.com',		
            'prodtest.comcast.ebiz.customer.api.QA4.xfinity.com',		
            'prodtest.comcast.learn.api.qa-4',		
            'prodtest.comcast.learn.web.qa-4',		
            'prodtest.Comcast.Mercury.Buyflow.Web-Qa4',		
            'www.qa4.comcast.com',		
            'prodtest.www.qa4.comcast.com',		
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa4',	

            #ContentServiceEndpoint
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa4.xfinity.com',	
            'prodtest.comcast.ebiz.customer.api.QA4.xfinity.com',	
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa4',	
            'prodtest.Comcast.Ebiz.Order.Api.Qa-4',	
            'prodtest.comcast.learn.api.qa-4',	
            'prodtest.www.qa4.comcast.com',	

            #Localization Service
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa4.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA4.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa4',
            'prodtest.Comcast.Ebiz.Order.Api.Qa-4',
            'prodtest.comcast.learn.api.qa-4',

            #PaymentService
	        'ProdTest.Comcast.ebiz.customer.api.omni.Qa4.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA4.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa4',
            'prodtest.Comcast.Ebiz.Order.Api.Qa-4',
            'prodtest.comcast.learn.api.qa-4',

            #SalesChannelManagementService
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa4.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA4.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa4',
            'prodtest.Comcast.Ebiz.Order.Api.Qa-4',
            'prodtest.comcast.learn.api.qa-4',

            #BaseUrl    
            'prodtest.Comcast.Mercury.Buyflow.Web-Qa4',
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa4',
            'Prodtest.Comcast.Myplan.Web-Qa4',
            'ProdTest.Comcast.Myplan.Web.Omni-Qa4',
            'prodtest.www.qa4.comcast.com',

            #Mercury RedirectUrl
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa4',
            'prodtest.Comcast.Mercury.Buyflow.Web-Qa4',

            #MyPlan RedirectUrl    
            'Prodtest.Comcast.Myplan.Web-Qa4',
            'ProdTest.Comcast.Myplan.Web.Omni-Qa4'
      
        ],
        'qa12': [
             #AffiliateId
            'Prodtest.learn.xfinity.com - QA12',
            'prodtest.learn.api.qa12.xfinity.com', 
            'prodtest.delivery.qa12.xfinity.com',
            'Prodtest.Comcast.Ebiz.Order.Api.Qa-12',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa12',
            'Prodtest.Comcast.Ebiz.Offers.Api.Qa-12',
            'Prodtest.Comcast.Ebiz.Localization.Api.Qa-12',
            'prodtest.comcast.ebiz.customer.api.QA12.xfinity.com',
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa12.xfinity.com',
            
            #ChannelName
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa12.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA12.xfinity.com',		
            'Prodtest.Comcast.Ebiz.Offers.Api.Qa-12',		
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa12',		
            'Prodtest.Comcast.Ebiz.Order.Api.Qa-12',		
            'Prodtest.Comcast.Mercury.Buyflow.Web-Qa12',		
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa12',		
            'prodtest.learn.api.qa12.xfinity.com',		

            #ContentServiceEndpoint
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa12.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA12.xfinity.com',	
            'prodtest.learn.api.qa12.xfinity.com',	
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa12',	
            'Prodtest.Comcast.Ebiz.Order.Api.Qa-12',	

            #Localization Service
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa12.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA12.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa12',
            'Prodtest.Comcast.Ebiz.Order.Api.Qa-12',
            'prodtest.learn.api.qa12.xfinity.com',

             #PaymentService
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa12.xfinity.com',  
            'prodtest.comcast.ebiz.customer.api.QA12.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa12',
            'Prodtest.Comcast.Ebiz.Order.Api.Qa-12',
            'prodtest.learn.api.qa12.xfinity.com',

            #SalesChannelManagementService
            'ProdTest.Comcast.ebiz.customer.api.omni.Qa12.xfinity.com',
            'prodtest.comcast.ebiz.customer.api.QA12.xfinity.com',
            'ProdTest.Comcast.Ebiz.Order.Api.Omni.Qa12',
            'Prodtest.Comcast.Ebiz.Order.Api.Qa-12',
            'prodtest.delivery.qa12.xfinity.com',
            'prodtest.learn.api.qa12.xfinity.com',

            #BaseUrl    
            'Prodtest.Comcast.Mercury.Buyflow.Web-Qa12',
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa12',
            'Prodtest.Comcast.Myplan.Web-Qa12', 
            'ProdTest.Comcast.Myplan.Web.Omni-Qa12',

            #Mercury RedirectUrl
            'Comcast.Mercury.Buyflow.Web-Qa12',
            'Comcast.Mercury.Buyflow.Web.Omni-Qa12',
            'Prodtest.Comcast.Mercury.Buyflow.Web-Qa12',
            'ProdTest.Comcast.Mercury.Buyflow.Web.Omni-Qa12',

            #MyPlan RedirectUrl 
            'Prodtest.Comcast.Myplan.Web-Qa12',  
            'ProdTest.Comcast.Myplan.Web.Omni-Qa12'

        ],
        'int' : [
            '',
            ''
        ],
        'stg' : [
            '',
            ''
        ]
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