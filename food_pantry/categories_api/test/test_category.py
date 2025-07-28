import pytest
from rest_framework import status
from rest_framework.test import APIClient # Importamos APIClient directamente
from django.urls import reverse # Necesario para resolver URLs por nombre

# Importamos el modelo Category desde la ruta relativa correcta
from categories_api.models import Category
# Importamos el serializador CategorySerializer desde la ruta relativa correcta
from categories_api.serializers import CategoriesRequestSerializer, CategoriesResponseSerializer


# --- Fixtures para Category (definidos directamente en este archivo de test) ---
@pytest.fixture()  
def api_client() -> APIClient:   # type: ignore
    """  
    Fixture to provide an API client  
    """  
    yield APIClient()

@pytest.fixture
def categories():
    """
    Fixture para crear algunas instancias de Category en la base de datos de prueba.
    El fixture 'db' es proporcionado por pytest-django para asegurar que la DB esté limpia.
    """
    category1 = Category.objects.create(id= 1, name='Frutas', description='Frutas frescas y enlatadas')
    category2 = Category.objects.create(id= 2, name='Verduras', description='Vegetales de hoja y tubérculos')
    return [category1, category2]

@pytest.fixture
def category_post_payload():
    """
    Fixture que devuelve un payload válido para crear una nueva categoría (POST).
    """
    return {
        'name': 'Bebidas',
        'description': 'Agua, zumos, refrescos'
    }

@pytest.fixture
def category_payload_missing_name():
    """
    Fixture que devuelve un payload inválido para crear una categoría (nombre vacío).
    """
    return {
        'name': '', # Esto debería fallar la validación del serializador
        'description': 'Categoría sin nombre'
    }

@pytest.fixture
def category_payload_update_name():
    """
    Fixture que devuelve un payload válido para actualizar una categoría (PUT).
    """
    return {
        'name': 'Panadería',
        'description': 'Pan, bollos, pasteles'
    }

@pytest.fixture
def category_payload_partial_update():
    """
    Fixture que devuelve un payload para actualizar parcialmente una categoría (PATCH).
    """
    return {
        'description': 'Descripción actualizada parcialmente'
    }


class TestCategories:
    # No necesitamos 'end_point' fijo si usamos 'reverse()' con nombres de URL
    # ya que 'reverse' construye la URL completa por nosotros.

    # --- GET all categories ---
    @pytest.mark.django_db
    def test_get_categories_returns_ok(self, api_client, categories):
        """
        Verifica que la API para obtener todas las categorías devuelve 200 OK
        y el número correcto de categorías.
        """
        # Usamos reverse para obtener la URL por su nombre
        url = "/food_pantry/api/v1/categories/"
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == len(categories) # Asume que el fixture 'categories' crea 2 categorías


    # --- CREATE category ---
    @pytest.mark.django_db
    def test_post_category_returns_created(self, api_client, category_post_payload):
        """
        Verifica que se puede crear una nueva categoría con datos válidos.
        """
        url = "/food_pantry/api/v1/categories/"
        initial_category_count = Category.objects.count()
        response = api_client.post(url, category_post_payload, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Category.objects.count() == initial_category_count + 1 # Verifica que se añadió una
        assert response.data.get('name') == category_post_payload.get('name')
        assert response.data.get('description') == category_post_payload.get('description')


    # --- CREATE category with bad data ---
    @pytest.mark.django_db
    def test_post_category_with_missing_name_returns_bad_request(self, api_client, category_payload_missing_name):
        """
        Verifica que no se puede crear una categoría con un nombre faltante/vacío.
        """
        url = "/food_pantry/api/v1/categories/"
        response = api_client.post(url, category_payload_missing_name, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'name' in response.data # Verifica que el error es sobre el campo 'name'


    # --- GET single category ---
    @pytest.mark.django_db
    def test_get_single_category_returns_ok(self, api_client, categories):
        """
        Verifica que se puede obtener una categoría específica por su ID.
        """
        url = "/food_pantry/api/v1/categories/" # Usamos el nombre de URL 'category-detail'
        response = api_client.get(url + "1")

        assert response.status_code == status.HTTP_200_OK
        assert response.data.get('id') == categories[0].id
        assert response.data.get('name') == categories[0].name
        assert response.data.get('description') == categories[0].description


    # --- GET non-existent category ---
    @pytest.mark.django_db
    def test_get_non_existent_category_returns_not_found(self, api_client):
        """
        Verifica que la solicitud de una categoría que no existe devuelve 404 Not Found.
        """
        url = "/food_pantry/api/v1/categories/"
        response = api_client.get(url + "999")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        # assert "not found" in response.data.get('detail', '').lower() # Mensaje de detalle de DRF


    # --- UPDATE category (PUT) ---
    @pytest.mark.django_db
    def test_put_category_returns_ok(self, api_client, categories, category_payload_update_name):
        """
        Verifica que se puede actualizar completamente una categoría existente con PUT.
        """
        category_to_update = categories[0]
        url = "/food_pantry/api/v1/categories/"
        response = api_client.put(url + str(category_to_update.id), category_payload_update_name, format='json')

        assert response.status_code == status.HTTP_200_OK
        category_to_update.refresh_from_db() # Recargar el objeto desde la DB
        assert category_to_update.name == category_payload_update_name.get('name')
        assert category_to_update.description == category_payload_update_name.get('description')


    # # # --- UPDATE category (PATCH) ---
    # @pytest.mark.django_db
    # def test_patch_category_returns_ok(self, api_client, categories, category_payload_partial_update):
    #     """
    #     Verifica que se puede actualizar parcialmente una categoría existente con PATCH.
    #     """
    #     category_to_update = categories[0]
    #     original_name = category_to_update.name
    #     url = "/food_pantry/api/v1/categories/"
    #     response = api_client.patch(url + str(category_to_update.id), category_payload_partial_update, format='json')

    #     assert response.status_code == status.HTTP_200_OK
    #     category_to_update.refresh_from_db()
    #     assert category_to_update.name == original_name # El nombre no debería cambiar
    #     assert category_to_update.description == category_payload_partial_update.get('description')


    # # --- UPDATE non-existent category ---
    @pytest.mark.django_db
    def test_put_non_existing_category_returns_not_found(self, api_client, category_payload_update_name):
        """
        Verifica que intentar actualizar una categoría que no existe devuelve 404 Not Found.
        """
        non_existent_id = 9999
        url = "/food_pantry/api/v1/categories/"
        response = api_client.put(url + str(non_existent_id), category_payload_update_name, format='json')

        assert response.status_code == status.HTTP_404_NOT_FOUND
        # assert "not found" in response.data.get('detail', '').lower()


    # --- DELETE category ---
    @pytest.mark.django_db
    def test_delete_category_returns_no_content(self, api_client, categories):
        """
        Verifica que se puede eliminar una categoría existente.
        """
        category_to_delete = categories[0]
        initial_category_count = Category.objects.count()
        url = "/food_pantry/api/v1/categories/"
        response = api_client.delete(url + str(category_to_delete.id))

        assert response.status_code == status.HTTP_204_NO_CONTENT # Código 204 para DELETE exitoso
        assert Category.objects.count() == initial_category_count - 1
        assert not Category.objects.filter(id=category_to_delete.id).exists()


    # # --- DELETE non-existent category ---
    @pytest.mark.django_db
    def test_delete_non_existing_category_returns_not_found(self, api_client):
        """
        Verifica que intentar eliminar una categoría que no existe devuelve 404 Not Found.
        """
        non_existent_id = 9999
        url = "/food_pantry/api/v1/categories/"
        response = api_client.delete(url + str(non_existent_id))

        assert response.status_code == status.HTTP_404_NOT_FOUND
        # assert "not found" in response.data.get('detail', '').lower()