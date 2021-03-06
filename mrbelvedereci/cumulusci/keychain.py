import json
from cumulusci.core.keychain import BaseProjectKeychain
from cumulusci.core.config import ConnectedAppOAuthConfig
from cumulusci.core.config import OrgConfig
from cumulusci.core.config import ScratchOrgConfig
from django.conf import settings
from mrbelvedereci.salesforce.models import Org

class MrbelvedereProjectKeychain(BaseProjectKeychain):

    def __init__(self, project_config, key, build_flow):
        self.build_flow = build_flow
        super(MrbelvedereProjectKeychain, self).__init__(project_config, key)

    def _load_keychain_services(self):
        for key, value in settings.__dict__['_wrapped'].__dict__.items():
            if key.startswith('CUMULUSCI_SERVICE_'):
                self.services[key[len('CUMULUSCI_SERVICE_'):]] = ServiceConfig(json.loads(value))

    def change_key(self):
        raise NotImplementedError('change_key is not supported in this keychain')

    def set_connected_app(self):
        raise NotImplementedError('set_connected_app is not supported in this keychain')

    def get_connected_app(self):
        return ConnectedAppOAuthConfig({
            'callback_url': settings.CONNECTED_APP_CALLBACK_URL,
            'client_id': settings.CONNECTED_APP_CLIENT_ID,
            'client_secret': settings.CONNECTED_APP_CLIENT_SECRET,
        })

    def list_orgs(self):
        raise NotImplementedError('list_orgs is not supported in this keychain')

    def get_default_org(self):
        raise NotImplementedError('get_default_org is not supported in this keychain')

    def set_default_org(self):
        raise NotImplementedError('set_default_org is not supported in this keychain')

    def get_org(self, org_name):
        org = Org.objects.get(repo=self.build_flow.build.repo, name=org_name)
        org_config = json.loads(org.json)
    
        if org.scratch:
            return ScratchOrgConfig(org_config)
        else:
            return OrgConfig(org_config)

    def set_org(self, org_name, org_config):
        try:
            org = Org.objects.get(repo = self.build_flow.build.repo, name = org_name)
            org.json = json.dumps(org_config.config)
        except Org.DoesNotExist:
            org = Org(
                name = org_name,
                json = json.dumps(org_config.config),
                repo = self.build_flow.build.repo,
            )
            
        org.scratch = isinstance(org_config, ScratchOrgConfig)
        org.save()
        
