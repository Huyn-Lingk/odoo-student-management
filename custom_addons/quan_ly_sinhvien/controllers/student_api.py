from odoo import http
from odoo.http import request

class StudentAPI(http.Controller):
    @http.route('/api/student/<int:student_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_student_info(self, student_id, **kwargs):
        student = request.env['quanlysinhvien.student'].sudo().search([('id', '=', student_id)], limit=1)
        if not student:
            return request.make_json_response({'error': 'Không tìm thấy sinh viên'}, status=404)

        return request.make_json_response({
            'name': student.name,
            'email': student.email,
            'student_code': student.student_code,
            'gender': student.gender,
            'phone': student.phone,
            'class_name': student.class_name,
            'birth_date': student.birth_date
        })
