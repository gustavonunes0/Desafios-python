# alterar_canal = lambda cor, canal, novo_valor: [cor[i] if i != canal else novo_valor for i in range(3)]

# cor_original = [int(input("Digite o valor do canal Vermelho (0 - 255): ")),
#                 int(input("Digite o valor do canal Verde (0 - 255): ")),
#                 int(input("Digite o valor do canal Azul (0 - 255): "))]

# print(f"Cor Original: {cor_original}")

# canal = int(input("Digite o número do canal a ser alterado (0 - Vermelho, 1 - Verde, 2 - Azul): "))
# novo_valor = int(input("Digite o novo valor para o canal (0-255): "))

# nova_cor = alterar_canal(cor_original, canal, novo_valor)

# print(f"Nova Cor: {nova_cor}")

from PIL import Image

# Carregar a imagem
image_path = './q3_Gustavonunes/q3_Imagem.png'
image = Image.open(image_path)
# Solicitar ao usuário o fator de brilho
brightness_factor = float(input("Digite o fator de brilho (1.0 para manter o brilho original): "))

# Aplicar a função lambda para alterar o brilho
brightened_image = image.point(lambda p: int(p * brightness_factor))

# Salvar a imagem alterada
brightened_image.save("./q3_Gustavonunes/q3_Imagem.png")