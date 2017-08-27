# Quick preview URL
# http://www.drivethrurpg.com/demo_xml/{prodcutId}.xml

# Full preview URL
# http://watermark.drivethrurpg.com/pdf_previews/{}-sample.pdf

import argparse
import json
import urllib

parser = argparse.ArgumentParser(description='Validate that DriveThruRPG Quick and Full previews exist.')
parser.add_argument('jsonFile', type=argparse.FileType('r'), help='JSON file listing products and metadata')

args = parser.parse_args()

baseUrl = 'http://www.drivethrurpg.com/product/'

def getProductUrl(productId):
    """Generates and returns the URL to view the product"""
    return baseUrl + productId

def getQuickViewUrl(productId):
    """Generates and returns the URL used to view quick view product"""
    return 'http://www.drivethrurpg.com/demo_xml/' + productId + '.xml'


def getFullViewUrl(productId):
    """Generates and returns the URL used to view full view product"""
    return 'http://watermark.drivethrurpg.com/pdf_previews/' + productId + '-sample.pdf'

productsJson = json.load(args.jsonFile)

for product in productsJson['Products']:
    productId = product['productId']
    print 'Testing product ' + productId

    missingQuick = False
    missinFull = False
    if product['shouldHaveQuickPreview']:
        quickViewUrl = getQuickViewUrl(productId)
        quickResponse = urllib.urlopen(quickViewUrl)
        if quickResponse.getcode() != 200:
            missingQuick = True

    if product['shouldHaveFullPreview']:
        fullViewUrl = getFullViewUrl(productId)
        fullResponse = urllib.urlopen(fullViewUrl)
        if fullResponse.getcode() != 200:
            missinFull = True

    if missingQuick:
        print getProductUrl(productId) + ' is missing quick view'

    if missinFull:
        print getProductUrl(productId) + ' is missing quick view'
