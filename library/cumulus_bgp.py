#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import yaml

def configure_bgp(module):
    # Module custom pour configurer BGP de manière déclarative
    pass

def main():
    module = AnsibleModule(
        argument_spec=dict(
            asn=dict(type='str', required=True),
            router_id=dict(type='str', required=True),
            neighbors=dict(type='list', required=True)
        )
    )
    configure_bgp(module)

if __name__ == '__main__':
    main()