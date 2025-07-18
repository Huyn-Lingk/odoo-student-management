# -*- coding: utf-8 -*-
{
    'name': "quanLySinhvien",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
    Ứng dụng quản lý sinh viên tiện lợi và hiệu quả
    """,

    'author': "Huyn",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',   

    'report/student_report_template.xml',
    'report/student_listShow_template.xml',
    'views/sequence_student_code.xml',
    'views/student.xml',                         
    'views/grade.xml',
    'views/subject.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}

