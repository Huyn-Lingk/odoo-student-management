from odoo import models, fields

class Student(models.Model):
    _name = 'qlsv.student'
    _description = 'Sinh viên'

    name = fields.Char(string='Họ và tên', required=True)
    birth_date = fields.Date(string='Ngày sinh')
    email = fields.Char(string='Email')
    student_code = fields.Char(string='Mã sinh viên', required=True)
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')], string='Giới tính')
    phone = fields.Char(string='Số điện thoại')
    
    # Quan hệ
    class_id = fields.Many2one('qlsv.class', string='Lớp')
    grade_ids = fields.One2many('qlsv.grade', 'student_id', string='Bảng điểm')
