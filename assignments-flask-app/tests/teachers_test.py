
def test_get_assignments_student_1(client, h_student_1):
    response = client.get(
        '/student/assignments',
        headers=h_student_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1

def test_get_assignments_student_2(client, h_student_2):
    response = client.get(
        '/student/assignments',
        headers=h_student_2
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 2

def test_post_assignment_student_1(client, h_teacher_1):
    content = 'ABCD TESTPOST'

    response = client.post(
        '/teacher/assignments',
        headers=h_teacher_1,
        json={
            'content': content
        })

    
    assert response.status_code == 405

    data = response.json
    assert data['error'] == 'MethodNotAllowed'

def test_edit_assignment_student_2(client, h_student_2):
    content = 'NEW CONTENT'

    response = client.post(
        '/student/assignments',
        headers=h_student_2,
        json={
            'id': 5,
            'content': content
        })

    assert response.status_code == 404

    data = response.json
    assert data['error'] == 'FyleError'

def test_edit_submitted_assignment_student_1(client, h_student_1):
    content = 'NEW CONTENT'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'id': 1,
            'content': content
        })

    assert response.status_code == 404

    data = response.json
    assert data['error'] == 'FyleError'

def test_submit_assignment_student_1(client, h_student_1):
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })

    assert response.status_code == 404

    data = response.json
    assert data['error'] == 'FyleError'

def test_grade_assignment_teacher(client, h_teacher_1):
    assignment_id = 1
    grade_value = 'A'

    response = client.post(
        f'/teacher/assignments/grade/{assignment_id}',
        headers=h_teacher_1,
        json={
            'grade': grade_value
        })
    
    assert response.status_code == 404
    
    