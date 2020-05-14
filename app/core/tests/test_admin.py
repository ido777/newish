import pytest
from django.urls import reverse


@pytest.mark.skip(reason="WIP moving to pytest tests")
def test_with_authenticated_client(client, django_user_model):
    email = 'admin@somewhere.com'
    password = 'password123'
    admin_user = django_user_model.objects.create_superuser(
        email, password)
    client.force_login(user=admin_user)
    user = django_user_model.objects.create_user('user@somewhere.com', password='password123',
                                                 name='Test user full name')

    url = reverse('admin:core_user_changelist')
    res = client.get(url)

    assert user.name in res
    assert user.email in res


def test_user_page_change(client, django_user_model):
    """Test that the user edit page works"""
    email = 'admin@somewhere.com'
    password = 'password123'
    admin_user = django_user_model.objects.create_superuser(
        email, password)
    client.force_login(user=admin_user)
    user = django_user_model.objects.create_user('user@somewhere.com', password='password123',
                                                 name='Test user full name')

    url = reverse('admin:core_user_change', args=[user.id])
    res = client.get(url)

    assert res.status_code == 200


def test_create_user_page(client, django_user_model):
    """Test that the create user page works"""
    email = 'admin@somewhere.com'
    password = 'password123'
    admin_user = django_user_model.objects.create_superuser(
        email, password)
    client.force_login(user=admin_user)
    url = reverse('admin:core_user_add')
    res = client.get(url)

    assert res.status_code == 200


'''
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('user@somewhere.com', password='password123', name='Test user full name')
    assert User.objects.count() == 1



@pytest.mark.parametrize(
    'admin, user, client',
        get_user_model().objects.create_superuser(
                'admin@somewhere.com', password='password123'),
        get_user_model().objects.create_user(
        'user@somewhere.com', password='password123', name='Test user full name'),
        Client()
    )
@pytest.mark.db
def test_users_listed(admin, user, client):
    """Test that users are listed on the user page """
    url = reverse('admin:core_user_changelist')
    res = client.get(url)

    assert user.name in res
    assert user.email in res

'''
