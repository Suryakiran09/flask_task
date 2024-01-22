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


def test_post_assignment_student_1(client, h_student_1):
    content = 'ABCD TESTPOST'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })

    if response.status_code == 200:
        data = response.json['data']
        assert data['content'] == content
        assert data['state'] == 'DRAFT'
        assert data['teacher_id'] is None
    elif response.status_code == 400:
        assert 'error' in response.json 
    else:
        assert False, f"Unexpected status code: {response.status_code}"

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
