# :rat: DumpPass_RmBa :rat:
Esse código funciona nos sistemas operacionais Windows (PT-BR) e coleta senhas de WiFi já conectadas e informações críticas do navegador google chrome, como "Histórico, senhas salvas, últimas pesquisas".

Você pode usar esse código de duas maneiras. O primeiro é usar o Python para executar o código diretamente. No entanto, em ambientes que não possuem o interpretador python disponível, você pode criar um executável do Windows (.EXE).

Para criar seu arquivo executável (.EXE), você pode usar um conversor de script Python em programas executáveis do Windows que podem ser executados sem a necessidade de uma instalação Python. Alguns programas de conversão, como py2exe, cx_Freeze, PyInstaller. O PyInstaller é recomendado e será como este conversor que seguiremos este tutorial.

## PyInstaller Quickstart
Para instalar o PyInstaller, você pode usar o seguinte comando:
```
python -m pip install pyinstaller
```

Depois de instalado, use o comando abaixo no diretório do repositório atual para converter os arquivos getwifipass.py e getgooglechromedump.py em executável (.EXE).
```
pyinstaller --onefile getwifipass.py
```
```
pyinstaller --onefile getgooglechromedump.py
```

Se tudo estiver correto até agora, o pyinstaller criará algumas pastas e, dentro de "dist", você encontrará o arquivo executável pronto para uso.

![img](autorun_img.PNG)
