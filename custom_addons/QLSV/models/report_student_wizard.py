from odoo import models, fields
# from odoo.exceptions import UserError

class ReportStudentWizard(models.TransientModel):
    _name = 'qlsv.report_student_wizard'
    _description = 'Báo cáo sinh viên'

    student_code = fields.Many2many('qlsv.student', string="Danh sách sinh viên")


    # def action_print_pdf(self):
    #     try:
    #         return self.env.ref('qlsv.student_report_pdf').report_action(self)
    #     except ValueError:
    #         raise UserError("Không tìm thấy báo cáo 'qlsv.student_report_pdf'"
    def action_print_pdf(self):
        self.ensure_one()
        students = self.student_code
        return self.env.ref('qlsv.student_report_pdf').report_action(students)

       
    
    def action_select_all_students(self):
        all_students = self.env['qlsv.student'].search([])
        self.student_code = [(6, 0, all_students.ids)]
        return {
        'type': 'ir.actions.act_window',
        'res_model': 'qlsv.report_student_wizard',
        'view_mode': 'form',
        'res_id': self.id,
        'target': 'new',  # giữ lại popup
    }

    def action_deselect_all_students(self):
        self.student_code = [(5, 0, 0)]
        return {
        'type': 'ir.actions.act_window',
        'res_model': 'qlsv.report_student_wizard',
        'view_mode': 'form',
        'res_id': self.id,
        'target': 'new',  # Giữ lại popup
    }

