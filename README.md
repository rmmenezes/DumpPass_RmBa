# Get Wifi Passwords
This code collects passwords for WiFi networks already connected in the Windows operating system only (PT-BR).

Você pode usar este código de duas formas. A primeira é utilizar o Python para executar o código getwifipass.py diretamnete. Porém em ambientes que não possuam o interpretador python disponível pode você pode criar um arquivo executável do Windows (.EXE) do codigo “getwifipass.py”.

Para criar seu arquivo executável (.EXE) você pode utilizar um conversor de scripts Python em programas executáveis ​​do Windows, capazes de executar sem exigir uma instalação do Python. Alguns programas conversores como por exemplo: py2exe, cx_Freeze, PyInstaller. É recomendado o uso do PyInstaller e será como este conversor que seguiremos este tutorial.

## PyInstaller Quickstart
Para instalar o PyInstaller você pode utilizar o seguinte comando:
```
python -m pip install pyinstaller
```

Após instalado, use o comando abaixo no diretório corrente do repositório, para converter o arquivo getwifipass.py em executavel (.EXE). 
```
pyinstaller getwifipass.py
```

Se tudo estiver correto até aqui o pyinstaller irá criar algumas pastas sendo que dentro de “dist/getPass” você encontra o arquivo executável pronto para uso.

![img](autorun_img.PNG)
