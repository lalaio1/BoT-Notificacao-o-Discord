# Bot de Notificação para Discord 🤖📩

---
> 🤖 Este bot de Discord foi desenvolvido para enviar notificações para todos os membros não-bots de um servidor, utilizando Embeds para exibir informações detalhadas.
---

### Instalação e Configuração ⚙

### Pré-requisitos

- Python 3.6 ou superior
- `pip` (gerenciador de pacotes do Python)

### Instalação das Dependências

Para instalar as dependências necessárias, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

Certifique-se de estar no diretório onde o arquivo `requirements.txt` está localizado.

### Configuração do Token do Bot

1. Crie um arquivo `token.txt` dentro do diretório `AL/`.
2. Coloque o token do seu bot Discord neste arquivo.
   - Você pode obter o token do seu bot na seção de desenvolvedor do Discord.

### Configuração do Canal de Logs

No arquivo `main.py`, localize a linha 16:

```python
log_channel_id = Coloque o ID aq  # canal ID logs
```

Substitua `Coloque o ID aq` pelo ID do canal de logs onde você deseja enviar as notificações. Para encontrar o ID do canal:

1. No Discord, clique com o botão direito do mouse no canal desejado e selecione "Copiar ID".
2. Cole o ID no lugar indicado no arquivo `main.py`.

## Executando o Bot

Para iniciar o bot, execute o seguinte comando:

```bash
python main.py
```


Discord: lalaio1
