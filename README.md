# Acompanhamento de pedidos - Total express

O programa executa em background, monitorando o site e enviando e-mails para modificações no texto do mesmo


## Para executar

Desenvolvido em Python 3, utilize esta versão para executar o mesmo:
```
python3 main.py "url que quer monitorar" "seu email" "sua senha do e-mail" "email que vai receber os alertas"
```
Se você assim como eu utiliza Arch é só chamar python, pois o Python 3 é o padrão nele.

* Exemplo:
```
python3 main.py 'http://tracking.totalexpress.com.br/poupup_track.php?reid=1625&pedido=333&nfiscal=555' michelsm1990@gmail.com senha michelsm1990@gmail
```
No exemplo estou monitorando uma compra ficticia e enviando qualquer alteração para meu próprio email, obviamente a minha senha não é senha XD.


* Dica: 
  Você pode adicionar o parâmetro -& em qualquer execução, assim ela executara em background sem depender do terminal


O projeto é livre use, edite, copie como quiser :)

Se gostou deixe uma estrela
