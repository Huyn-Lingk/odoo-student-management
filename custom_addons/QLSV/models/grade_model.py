from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Grade(models.Model):
    _name = 'qlsv.grade'
    _description = 'Bảng điểm'

    # Quan hệ
    student_id = fields.Many2one('qlsv.student', string='Sinh viên', required=True)
    subject_id = fields.Many2one('qlsv.subject', string='Môn học', required=True)

    # Điểm số
    mid_term = fields.Float(string='Điểm giữa kỳ')
    final = fields.Float(string='Điểm cuối kỳ')
    average = fields.Float(string='Điểm trung bình', compute='_compute_average', store=True)

    @api.depends('mid_term', 'final')
    def _compute_average(self):
        for record in self:
            if record.final is not None and record.mid_term is not None:
                record.average = (record.mid_term + record.final) / 2
            else:
                record.average = 0.0
                
    @api.constrains('student_id', 'subject_id')
    def _check_unique_student_subject(self):
        for rec in self:
            domain = [
                ('student_id', '=', rec.student_id.id),
                ('subject_id', '=', rec.subject_id.id),
                ('id', '!=', rec.id)  # bỏ qua chính bản ghi đang sửa
            ]
            if self.search_count(domain):
                raise ValidationError('Sinh viên này đã có điểm cho môn học này rồi!')