import unittest
from unittest.mock import patch
from pet_info import coletar_informacoes_pet

class TestPetInfo(unittest.TestCase):

    @patch('builtins.input', side_effect=['Bobby', 'cao', 'm', '5', '12.5'])
    @patch('builtins.print')
    def test_coletar_informacoes_pet(self, mock_print, mock_input):
        coletar_informacoes_pet()
        
        # Verifica se a função print foi chamada com as informações corretas
        mock_print.assert_any_call("\nInformações do pet:")
        mock_print.assert_any_call("Nome: Bobby")
        mock_print.assert_any_call("Tipo: cao")
        mock_print.assert_any_call("Sexo: Masculino")
        mock_print.assert_any_call("Idade: 5 anos")
        mock_print.assert_any_call("Peso: 12.5 kg")

if _name_ == '_main_':
    unittest.main()