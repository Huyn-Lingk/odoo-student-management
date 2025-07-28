from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Subject(models.Model):
    _name = 'qlsv.subject'
    _description = 'Môn học'

    name = fields.Char(string='Tên môn học', required=True)
    code = fields.Char(string='Mã môn học', required=True)
    
    # Quan hệ
    grade_ids = fields.One2many('qlsv.grade', 'subject_id', string='Danh sách điểm')

    # @api.constrain('code', 'name')
    # def check_unique_subject(self):
    #     for rec in self:
    #         if self.search_count([('code', '=', rec.code), ('id', '!=', rec.id)]):
    #             raise ValidationError('Mã môn học này đã tồn tại! Vui lòng nhập mã môn học khác.')