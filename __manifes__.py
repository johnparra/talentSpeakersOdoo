{
    'name': 'UniAcme',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Gestión de votaciones para UniAcme',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sede_views.xml',
        'views/candidato_views.xml',
        'views/estudiante_views.xml',
        'views/votacion_views.xml',
        'views/voto_views.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
