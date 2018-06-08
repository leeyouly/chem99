from scrapy.dupefilters import RFPDupeFilter
import random

class ChemDupeFilter(RFPDupeFilter):
    def request_fingerprint(self, request):
        if request.url.startswith('http://plas.chem99.com/include/head.aspx'):
            dummy_request = request.copy()
            dummy_request = dummy_request.replace(url = dummy_request.url + '&rdm=' + str(random.random()))
            return super(ChemDupeFilter, self).request_fingerprint(dummy_request)
        if request.url.startswith('http://oil.chem99.com/include/loginframetop.aspx'):
            dummy_request = request.copy()
            dummy_request = dummy_request.replace(url = dummy_request.url + '&rdm=' + str(random.random()))
            return super(ChemDupeFilter, self).request_fingerprint(dummy_request)
        if request.url.startswith('http://rubb.chem99.com/include/loginhead.aspx'):
            dummy_request = request.copy()
            dummy_request = dummy_request.replace(url = dummy_request.url + '&rdm=' + str(random.random()))
            return super(ChemDupeFilter, self).request_fingerprint(dummy_request)
        if request.url.startswith('http://ca.chem99.com/include/login.aspx'):
            dummy_request = request.copy()
            dummy_request = dummy_request.replace(url = dummy_request.url + '&rdm=' + str(random.random()))
            return super(ChemDupeFilter, self).request_fingerprint(dummy_request)
        return super(ChemDupeFilter, self).request_fingerprint(request)
