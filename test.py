# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest"
        self.app = app.test_client()

        # Requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # iquals a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # valor retorno da pagina
        self.assertEqual(self.result.data.decode('utf-8'), "Hello World")

if __name__ == "__main__":
    unittest.main(verbosity=2)