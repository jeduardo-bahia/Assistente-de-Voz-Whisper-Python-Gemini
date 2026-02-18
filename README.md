# 🛡️ Gemini Voice Escudeiro: Assistente Virtual com IA

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Gemini](https://img.shields.io/badge/IA-Gemini%202.5%20Flash-orange)
![Whisper](https://img.shields.io/badge/Speech--to--Text-Faster--Whisper-green)

O **Gemini Voice Escudeiro** é um assistente de voz inteligente projetado para oferecer uma interação natural e rápida. Ele combina tecnologias de ponta para garantir que o processamento seja eficiente e respeite a privacidade do usuário.



## 🚀 Funcionalidades Principais

**Transcrição de Alta Performance** Utiliza o modelo `Faster-Whisper` localmente. Isso significa que sua voz é convertida em texto no seu próprio computador, garantindo maior velocidade e privacidade sem depender de nuvem para o Speech-to-Text.

**Cérebro de Nova Geração** As respostas são geradas pelo `Gemini 2.5 Flash`, um dos modelos mais rápidos e inteligentes da atualidade, capaz de entender contextos complexos e fornecer respostas úteis em segundos.

**Áudio Inteligente e Limpo** Diferente de outros assistentes, este projeto utiliza buffers de memória RAM para processar o áudio. O sistema não salva arquivos `.mp3` no seu computador, mantendo sua pasta de projeto sempre limpa e organizada.

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**: Linguagem base do projeto.
* **Faster-Whisper**: Motor de transcrição (STT) de alta eficiência.
* **Google Gemini API**: O "cérebro" do assistente (LLM).
* **gTTS & Pygame**: Responsáveis pela geração e reprodução da voz.
* **Noisereduce**: Filtro para limpeza de ruídos do microfone.

## 📦 Configuração do Ambiente

Siga os passos abaixo para preparar sua máquina:

1.  **Clonar o Projeto**:
    ```bash
    git clone [https://github.com/jeduardo-bahia/Assistente-de-Voz-Whisper-Python-Gemini.git](https://github.com/jeduardo-bahia/Assistente-de-Voz-Whisper-Python-Gemini.git)
    cd Assistente-de-Voz-Whisper-Python-Gemini
    ```

2.  **Instalar Dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Variáveis de Ambiente**:
    Crie um arquivo chamado `.env` e insira sua chave da API do Gemini:
    `GEMINI_API_KEY=SUA_CHAVE_AQUI`

## 🎮 Como Iniciar

Para começar a conversar com seu assistente, basta rodar o comando:

`python main.py`

O sistema ouvirá por 5 segundos, processará sua fala e responderá por voz. Para encerrar o programa a qualquer momento, você pode dizer as palavras-chave **"Sair"** ou **"Encerrar"**.

---
Desenvolvido por [Jhonanthan Eduardo](https://github.com/jeduardo-bahia)
