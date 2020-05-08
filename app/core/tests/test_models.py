import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user_with_email_successful():
    """Test creating a new user with an email successful"""
    email = 'test@myplace.com'
    password = 'Testpass123'
    user = get_user_model().objects.create_user(
        email=email,
        password=password
    )

    assert user.email == email
    assert user.check_password(password)


@pytest.mark.django_db
def test_new_user_email_normalized():
    """Test """
    email = 'test@UPPERNAME.com'
    user = get_user_model().objects.create_user(email, 'test123')

    assert user.email == email.lower()


@pytest.mark.django_db
def test_new_user_invalid_email():
    """Test """
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(None, 'test123')


@pytest.mark.django_db
def test_create_new_superuser():
    """Test """
    user = get_user_model().objects.create_superuser('test@somewhere.com', 'test123')

    assert user.is_superuser
    assert user.is_staff
