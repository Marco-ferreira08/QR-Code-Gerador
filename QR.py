import qrcode

def gerar_qr(texto, nome_arquivo="qr_code.png"):
    
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_H, 
        box_size=10,  
        border=4,  
    )

    qr.add_data(texto)
    qr.make(fit=True)

    # Gera a imagem do QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Salva a imagem
    img.save(nome_arquivo)
    print(f"✅ QR Code salvo como '{nome_arquivo}'.")

if __name__ == "__main__":
    conteudo = input("Digite o texto ou link para gerar o QR Code: ")
    gerar_qr(conteudo)
