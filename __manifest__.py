# -*- coding: utf-8 -*-

{
    'name': 'document_format_ch',
    'summary': """Formatos de documentos CH""",
    'version': '12.0.1.0.0',
    'description': """Formatos de documentos CH""",
    'author': 'DDL',
    'company': 'Xtendoo',
    'website': 'http://www.xtendoo.com',
    'category': 'Extra Tools',
    'depends': [
        'base',
        'account',
        'sale',
        'web'
    ],
    'license': 'AGPL-3',
    'data': [
        'views/report_saleorder_document.xml',
        'views/external_layout_clean.xml',
        'views/report_invoice_document.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,

}
