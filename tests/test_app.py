import falcon
from falcon import testing
import json
import pytest

from look.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_list_images(client):
    doc =b'{
            'image':[
                {
                    'href':'/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }'
    
    response = client.simulate_get('/images')
    result_doc=json.dumps(response.content,ensure_ascii=False)
    assert result_doc == doc
    assert response.status == falcon.HTTP_OK
