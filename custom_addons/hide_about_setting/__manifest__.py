{
    'name': 'Hide About in Settings',
    'version': '1.0',
    'summary': 'Ẩn phần About trong trang Cài đặt Odoo',
    'author': 'Huyn & Bo',
    'depends': ['base_setup'],
    'data': [
        'views/hide_about_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
