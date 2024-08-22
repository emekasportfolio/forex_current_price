from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
from lxml import html

def get_xrt_data(request):
    xrt_ticker_list_1 = [
        'eurusd', 'usdjpy', 'gbpusd', 'audusd', 'eurjpy', 'gbpjpy', 'euraud', 'audjpy', 'usdcad', 'eurgbp',
        'gbpaud', 'eurcad', 'eurchf', 'gbpcad', 'usdchf', 'cadjpy', 'nzdusd', 'audcad', 'gbpchf', 'cadchf',
        'audchf', 'chfjpy', 'cnhjpy', 'nzdcad', 'nzdjpy', 'eurhuf', 'mxnjpy', 'gbpnzd', 'gbppln', 'gbpsek',
        'eurrub', 'nzdchf', 'usdzar', 'zarjpy', 'usdpln', 'usdrub'
    ]
    xrt_last_1 = []

    for ticker in xrt_ticker_list_1:
        url = f"https://www.investing.com/currencies/{ticker[:3].lower()}-{ticker[3:].lower()}-technical"
        turl = requests.get(url)
        tree = html.fromstring(turl.content)
        
        valu1 = tree.xpath('//div[contains(@class, "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]")]/text()')
        valu1 = valu1[0].strip() if valu1 else None
        
        valu2 = tree.xpath('//span[@data-test="instrument-price-change-percent"]/text()')
        valu2 = ''.join(valu2).strip() if valu2 else None

        finitum = [ticker, valu1, valu2]
        xrt_last_1.append(finitum)
    
    return JsonResponse(xrt_last_1, safe=False)
