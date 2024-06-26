# Rewrite this in Unit Test

from caesar_cipher import caesar_cipher

# print(caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!")
# print(caesar_cipher("Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj.")
# print(caesar_cipher("Hello Zach168! Yes here.", -5) == "Czggj Uvxc168! Tzn czmz.")

def test_caesar_cipher_negative():
    assert caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!"

def test_caesar_cipher_positive():
    assert caesar_cipher("Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj."

def test_caesar_cipher_other():
    assert caesar_cipher("Hello Zach168! Yes here.", -5) == "Czggj Uvxc168! Tzn czmz."