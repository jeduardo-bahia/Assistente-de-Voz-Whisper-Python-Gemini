# 🛡️ Gemini Voice: Assistente Virtual com IA

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Gemini](https://img.shields.io/badge/IA-Gemini%202.5%20Flash-orange)
![Whisper](https://img.shields.io/badge/Speech--to--Text-Faster--Whisper-green)
![License](https://img.shields.io/badge/license-MIT-blue)

Um assistente de voz inteligente desenvolvido em Python que utiliza o modelo **Faster-Whisper** para transcrição local de alta performance e a **API do Gemini** para processamento de linguagem natural.



## 🚀 Funcionalidades

- **Transcrição Local**: Utiliza o Faster-Whisper (modelo `small`) para converter fala em texto com baixa latência, sem enviar áudio para a nuvem.
- **Inteligência Artificial**: Integrado ao Gemini 2.5 Flash para respostas rápidas, precisas e contextuais.
- **Feedback de Voz**: Respostas convertidas em áudio via gTTS e reproduzidas diretamente na memória RAM.
- **Privacidade e Limpeza**: O sistema não salva arquivos residuais de áudio (`.mp3` ou `.wav`) no disco, operando via buffers de memória.
- **Redução de Ruído**: Tratamento de áudio via `noisereduce` para melhor precisão em ambientes barulhentos.

## 🛠️ Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper) (STT)
- [Google Gemini API](https://ai.google.dev/) (LLM)
- [gTTS](https://pypi.org/project/gTTS/) (TTS)
- [Pygame](https://www.pygame.org/) (Audio Playback)
- [SoundDevice](https://python-sounddevice.readthedocs.io/) (Audio Capture)

## 📦 Instalação e Configuração

### 1. Clonar o repositório
```bash
git clone [https://github.com/jeduardo-bahia/Assistente-de-Voz-Whisper-Python-Gemini.git](https://github.com/jeduardo-bahia/Assistente-de-Voz-Whisper-Python-Gemini.git)
cd Assistente-de-Voz-Whisper-Python-Gemini

### 2. Instalar Dependências
Recomenda-se o uso de um ambiente virtual (venv):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

### 3. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e adicione sua chave de API: GEMINI_API_KEY=SUA_CHAVE_AQUI

## 🎮 Como Usar
1 - Execute o script principal: python main.py
2 - O sistema aguardará 5 segundos de gravação.
3 - Fale sua pergunta ou comando.
4 - Para encerrar, basta dizer as palavras "Sair" ou "Encerrar".

🛡️ Segurança
Este projeto utiliza python-dotenv para gerenciar chaves de API. O arquivo .env está incluído no .gitignore para evitar o vazamento acidental de credenciais em repositórios públicos.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Jhonanthan Eduardo 🚀
