from django.urls import reverse


def test_login_page(client):
    endpoint = reverse('users:login_view')
    response = client.get(endpoint)

    assert response.status_code == 200
    assert '<h1>Login</h1>' in str(response.content)
