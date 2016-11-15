# -*- coding: utf-8 -*-
"""Summary

Attributes:
    f (TYPE): Description
    news (TYPE): Description
    page_text (TYPE): Description
    page_unicode (TYPE): Description
    tree (TYPE): Description
"""
from lxml import html
from urllib2 import urlopen

def get_url_cont_lst(url_in, lambda_para, decode_para, encode_para):
    """Summary

    Args:
        url_in (TYPE): Description
        lambda_para (TYPE): Description

    Returns:
        TYPE: Description
    """
    page_uinc = urlopen(url_in)
    page_txt = page_uinc.read().decode(decode_para)
    page_tree = html.fromstring(page_txt)
    cont_lst = page_tree.xpath(lambda_para)
    cont_lst_enco = []
    for cont in cont_lst:
        cont_lst_enco.append(cont.encode(encode_para))
    return cont_lst

if __name__ == '__main__':
    news = get_url_cont_lst('http://fenlei.baike.com',
        '//dl[@class ="w-160"]/dt/a/text()', 'utf-8', 'utf-8')
    for i in news:
        print i