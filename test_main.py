from test_main_fake import (
	test_main_fake_is_equal_to_main_in_quant as quant,
	test_main_fake_is_equal_to_main_in_item as item
)

"""
Utilizar o return do test_main_fake para realizar
o teste do main.

O objetivo do test_main_fake é verificar se o 
main_fake está retornando o mesmo comportamento do
main original, evitando assim adulterações em
dependencias de testes que fazem retornar falso Positivo.
"""
def test_main():
	status = False
	if quant() and item():
		status = True

	assert status == True


if __name__ == "__main__":    
    test_main()
    