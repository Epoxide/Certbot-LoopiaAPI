#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xmlrpc.client
import os
import time
import dns.resolver

def main():
    # Environment variables passed from Certbot
    domain = os.environ['CERTBOT_DOMAIN']
    validation = os.environ['CERTBOT_VALIDATION']

    # Connect to the LoopiaAPI
    global_username = 'username@loopiaapi'
    global_password = 'password'
    global_domain_server_url = 'https://api.loopia.se/RPCSERV'
    api = xmlrpc.client.ServerProxy(uri = global_domain_server_url, encoding = 'utf-8')
    
    # Retrieve all zone records to an array
    top_level_domain = domain.split('.')[-2] + '.' + domain.split('.')[-1]
    subdomain = '_acme-challenge'
    zone_record = api.getZoneRecords(global_username, global_password, top_level_domain, subdomain)

    # Update the zone record
    zone_record[0]['rdata'] = validation
    api.updateZoneRecord(global_username, global_password, top_level_domain, subdomain, zone_record[0])

    # Check if the TXT record has been deployed
    sleep = 25
    dns.resolver.nameservers = ['8.8.8.8']
    dns_txt = ''
    while dns_txt != validation:
        time.sleep(sleep)
        dns_txt = str(dns.resolver.query(subdomain + '.' + top_level_domain,'TXT').response.answer[0][-1]).split('"')[1]


if __name__ == '__main__':
    main()
