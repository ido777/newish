import pytest
from django.contrib.auth import get_user_model
from unittest.mock import patch
from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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


@pytest.mark.django_db
def test_tag_str():
    """Test the tag string representation"""
    tag = models.Tag.objects.create(
        user=sample_user(),
        name='Vegan'
    )

    assert str(tag) == tag.name


@pytest.mark.django_db
def test_ingredient_str():
    """Test the ingredient string representation"""
    ingredient = models.Ingredient.objects.create(
        user=sample_user(),
        name='Cucumber'
    )

    assert str(ingredient) == ingredient.name


@pytest.mark.django_db
def test_recipe_str():
    """Test the recipe string representation"""
    recipe = models.Recipe.objects.create(
        user=sample_user(),
        title='Steak and mushroom sauce',
        time_minutes=5,
        price=5.00
    )

    assert str(recipe) == recipe.title


@pytest.mark.django_db
@patch('uuid.uuid4')
def test_recipe_file_name_uuid(mock_uuid):
    """Test that image is saved in the correct location"""
    uuid = 'test-uuid'
    mock_uuid.return_value = uuid
    file_path = models.recipe_image_file_path(None, 'myimage.jpg')

    exp_path = f'uploads/recipe/{uuid}.jpg'
    assert file_path == exp_path

