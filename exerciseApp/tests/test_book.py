import pytest

from library.factories import BookFactory

pytestmark = pytest.mark.django_db

@pytest.fixture
def created_book():
  return BookFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_book_post(created_book):
  assert created_book.title == 'pytest with factory'