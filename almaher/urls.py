from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('login', views.user_login, name='login'),
     path('logout', views.user_logout, name='logout'),
    path('blank', views.blank, name='blank'),
    path('404', views.pg_404, name='404'),
    
    # Manage Person
    path('person', views.person, name='person'),
    path('person/edit/<int:pk>', views.edit_person, name='edit_person'),
    path('person/del/<int:pk>', views.del_person, name='del_person'),

    path('person/lock/<int:pk>', views.lock_person, name='lock_person'),
    path('person/unlock/<int:pk>', views.unlock_person, name='unlock_person'),

    path('graduate', views.graduate, name='graduate'),

    # Urls Teachers
    path('teacher', views.teacher, name='teacher'),
    path('teacher/add', views.add_teacher, name='add_teacher'),
    
    # Urls Students
    path('student', views.student, name='student'),
    path('student/add', views.add_student, name='add_student'),

    # Urls Courses
    path('course', views.course, name='course'),
    path('course/add', views.add_course, name='add_course'),
    path('course/del/<int:pk>', views.del_course, name='del_course'),

    # Urls Levels
    path('level', views.level, name='level'),
    path('level/add', views.add_level, name='add_level'),
    path('level/del/<int:pk>', views.del_level, name='del_level'),

    # Urls Positions
    path('position', views.position, name='position'),
    path('position/add', views.add_position, name='add_position'),
    path('position/del/<int:pk>', views.del_position, name='del_position'),

    # Urls Times
    path('time', views.time, name='time'),
    path('time/add', views.add_time, name='add_time'),
    path('time/del/<int:pk>', views.del_time, name='del_time'),

    # Urls Sessions
    path('session', views.session, name='session'),
    path('session/generate', views.generate_session, name='generate_session'),
    path('session/add', views.add_session, name='add_session'),
    path('session/edit/<int:pk>', views.edit_session, name='edit_session'),
    path('session/del/<int:pk>', views.del_session, name='del_session'),

    # Urls Sessions_Students
    path('session/student/<int:pk>', views.session_student, name='session_student'),
    path('session/student/add/<int:pk>/<int:num>', views.add_session_student, name='add_session_student'),
    path('session/student/del/<int:pk>/<int:num>', views.del_session_student, name='del_session_student'),

    # Urls View_Session_Student
    path('view/session/student', views.view_session_student, name='view_session_student'),

    # Urls Attendance
    path('select/attendance', views.select_attendance, name='attendance'),
    path('attendance/teacher', views.attendance_teacher, name='attendance_teacher'),
    path('attendance/student', views.attendance_student, name='attendance_student'),
    path('attendance/generater', views.attendance_generater, name='attendance_generater'),
    
    # JSON
    path('ajax/change_status_true', views.change_status_true, name='change_status_true'),
    path('ajax/change_status_false', views.change_status_false, name='change_status_false'),

    # Urls Exam
    path('select/exam', views.select_exam, name='select_exam'),
    path('exam', views.exam, name='exam'),

    # Urls Export to *
    path('export/excel/student', views.export_excel_student, name='export_excel_student'),
    path('export/excel/teacher', views.export_excel_teacher, name='export_excel_teacher'),
    path('export/excel/attendance/student', views.export_excel_attendance_student, name='export_excel_attendance_student'),
    path('export/excel/attendance/teacher', views.export_excel_attendance_teacher, name='export_excel_attendance_teacher'),
    
    
    
    
    
    
    path('wait', views.wait_list, name='wait_list'),

    # Urls Select Course for session
    path('select/course', views.select_course, name='select_course'),

]