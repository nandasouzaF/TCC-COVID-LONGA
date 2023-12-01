import datetime
import os

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_use
from app import app
import unittest
from app import mapear_grupo_idade, calcular_probabilidade

class TestCalculoProbabilidade(unittest.TestCase):
    def test_mapear_grupo_idade(self):
        # Teste para mapear_grupo_idade()
        resultado = mapear_grupo_idade(25)
        self.assertEqual(resultado, 'Grupo 2')

        resultado = mapear_grupo_idade(55)
        self.assertEqual(resultado, 'Grupo 3')

        resultado = mapear_grupo_idade(10)
        self.assertEqual(resultado, 'Grupo 1')

        resultado = mapear_grupo_idade(150)
        self.assertEqual(resultado, 'Outro')

    def test_calcular_probabilidade(self):
        # Testes para calcular_probabilidade()
        resultado = calcular_probabilidade(
            idade=25, sexo='Masculino', raca='Branca', escolaridade='Ensino Médio',
            estado='SP', cidade='São Paulo', zona='urbana', comorbidades={},
            internacao_uti=0, sintomas={}, grupo_idade='Grupo de Risco 1'
        )
        self.assertAlmostEqual(resultado, 10.0, delta=0.1)

        resultado = calcular_probabilidade(
            idade=40, sexo='Feminino', raca='Parda', escolaridade='Ensino Superior',
            estado='RJ', cidade='Rio de Janeiro', zona='urbana', comorbidades={},
            internacao_uti=0, sintomas={}, grupo_idade='Grupo de Risco 2'
        )
        self.assertAlmostEqual(resultado, 10.0, delta=0.1)

        resultado = calcular_probabilidade(
            idade=55, sexo='Masculino', raca='Negra', escolaridade='Ensino Fundamental',
            estado='MG', cidade='Belo Horizonte', zona='rural', comorbidades={},
            internacao_uti=0, sintomas={}, grupo_idade='Grupo de Risco 3'
        )
        self.assertAlmostEqual(resultado, 10.0, delta=0.1)

        resultado = calcular_probabilidade(
            idade=30, sexo='Masculino', raca='Branca', escolaridade='Ensino Médio',
            estado='SP', cidade='São Paulo', zona='urbana', comorbidades={},
            internacao_uti=0, sintomas={}, grupo_idade='Grupo 3'
        )
        self.assertTrue(0 <= resultado <= 100, "A probabilidade está fora do intervalo válido")




#teste para a função voltar() e resultados_testes()
class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_voltar_route(self):
        # Testa a rota /voltar
        response = self.app.get('/voltar')
        self.assertEqual(response.status_code, 200)  # Verifica se o código de status é 200 (OK)

    def test_resultados_testes_route(self):
        # Testa a rota /resultados_testes
        response = self.app.get('/resultados_testes')
        self.assertEqual(response.status_code, 200)  # Verifica se o código de status é 200 (OK)





class TestPasswordReset(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_forgot_password_route(self):
        # Testa a rota /forgot_password com método POST
        response = self.app.post('/forgot_password', data={'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)  # Verifica se o código de status é 200 (OK)
        self.assertIn(b'Verifique seu e-mail para redefinir a senha.', response.data)  # Verifica se a mensagem de sucesso está presente na resposta

    def test_reset_password_route(self):
        # Testa a rota /reset_password/token com método POST
        response = self.app.post('/reset_password/token')
        self.assertEqual(response.status_code, 200)  # Verifica se o código de status é 200 (OK)
        self.assertIn(b'Senha redefinida com sucesso!', response.data)  # Verifica se a mensagem de sucesso está presente na resposta

    def test_check_email_route(self):
        # Testa a rota /check_email com método POST
        response = self.app.post('/check_email', data={'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)  # Verifica se o código de status é 200 (OK)
        self.assertEqual(response.data.decode('utf-8'), 'exists')  # Verifica se o retorno é 'exists'

    def test_recover_account_route(self):
        # Testa a rota /recover_account com método POST
        response = self.app.post('/recover_account', data={'email': 'test@example.com', 'email_exists': 'exists'})
        self.assertEqual(response.status_code, 200)  # Verifica se o código de status é 200 (OK)
        self.assertTrue('E-mail de recuperação enviado!' in response.data.decode('utf-8')) # Verifica se a mensagem de sucesso está presente na resposta




if __name__ == '__main__':
    unittest.main()
