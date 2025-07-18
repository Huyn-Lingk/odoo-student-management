from odoo import models, fields

class Subject(models.Model):
    _name = 'quanlysinhvien.subject'
    _description = 'Subject Information'
    
    name = fields.Char(string='Tên môn học', required=True)
    code = fields.Char(string='Mã môn học', required=True)
    credits = fields.Integer(string='Số tín chỉ', required=True)
    semester = fields.Char(string='Học kỳ', required=True)