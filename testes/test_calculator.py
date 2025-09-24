#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para calculator.py
Desenvolvido por Bruno com ajuda do Otimus (IA)
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from calculator import adicao, subtracao, multiplicacao, divisao

class TestCalculator:
    """Classe de testes para as operações da calculadora"""
    
    def test_adicao_positiva(self):
        """Testa adição com números positivos"""
        assert adicao(5, 3) == 8
        assert adicao(10, 15) == 25
        assert adicao(0, 5) == 5
    
    def test_adicao_negativa(self):
        """Testa adição com números negativos"""
        assert adicao(-5, -3) == -8
        assert adicao(-10, 5) == -5
        assert adicao(5, -3) == 2
    
    def test_subtracao_positiva(self):
        """Testa subtração com números positivos"""
        assert subtracao(10, 3) == 7
        assert subtracao(15, 5) == 10
        assert subtracao(5, 5) == 0
    
    def test_subtracao_negativa(self):
        """Testa subtração com números negativos"""
        assert subtracao(-5, -3) == -2
        assert subtracao(5, -3) == 8
        assert subtracao(-5, 3) == -8
    
    def test_multiplicacao_positiva(self):
        """Testa multiplicação com números positivos"""
        assert multiplicacao(4, 5) == 20
        assert multiplicacao(3, 7) == 21
        assert multiplicacao(0, 5) == 0
    
    def test_multiplicacao_negativa(self):
        """Testa multiplicação com números negativos"""
        assert multiplicacao(-4, 5) == -20
        assert multiplicacao(-3, -7) == 21
        assert multiplicacao(4, -5) == -20
    
    def test_divisao_normal(self):
        """Testa divisão com números normais"""
        assert divisao(10, 2) == 5
        assert divisao(15, 3) == 5
        assert divisao(7, 2) == 3.5
    
    def test_divisao_por_zero(self):
        """Testa divisão por zero - deve gerar erro"""
        with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
            divisao(10, 0)
        
        with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
            divisao(-5, 0)
    
    def test_divisao_negativa(self):
        """Testa divisão com números negativos"""
        assert divisao(-10, 2) == -5
        assert divisao(10, -2) == -5
        assert divisao(-10, -2) == 5

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
